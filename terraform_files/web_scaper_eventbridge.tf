resource "aws_scheduler_schedule" "cron" {
  name       = "my-schedule"
  group_name = "default"

  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "cron(0 1 * * ? *)"

  target {
    arn      = aws_ecs_cluster.peaks_cluster.arn
    role_arn = aws_iam_role.scheduler.arn

    ecs_parameters {
      task_definition_arn = aws_ecs_task_definition.service.arn
      launch_type         = "FARGATE"

      network_configuration {
        assign_public_ip = true
        security_groups  = [data.aws_security_group.default.id]
        subnets          = data.aws_subnets.default.ids
      }
    }

    retry_policy {
      maximum_retry_attempts       = 0
      maximum_event_age_in_seconds = 60
    }

  }
}

resource "aws_iam_role" "scheduler" {
  name = "cron-scheduler-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = ["scheduler.amazonaws.com"]
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "scheduler" {
  policy_arn = aws_iam_policy.scheduler.arn
  role       = aws_iam_role.scheduler.name
}

resource "aws_iam_policy" "scheduler" {
  name = "cron-scheduler-policy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        "Effect" : "Allow",
        "Action" : [
          "ecs:RunTask"
        ],
        "Resource" : [
          aws_ecs_task_definition.service.arn,
          "${aws_ecs_task_definition.service.arn}:*"
        ],
        "Condition" : {
          "ArnLike" : {
            "ecs:cluster" : aws_ecs_cluster.peaks_cluster.arn
          }
        }
      },
      {
        "Effect" : "Allow",
        "Action" : "iam:PassRole",
        "Resource" : [
          "*"
        ],
        "Condition" : {
          "StringLike" : {
            "iam:PassedToService" : "ecs-tasks.amazonaws.com"
          }
        }
      }
    ]
  })
}