resource "aws_iam_role" "s3_role" {
  name = "s3_access_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy" "s3_access_policy" {
  name        = "s3_access_policy"
  description = "Policy for S3 bucket access"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket"
        ],
        Effect = "Allow",
        Resource = [
          "arn:aws:s3:::${aws_s3_bucket.peaks-data-bucket.id}",  # Bucket resource
          "arn:aws:s3:::${aws_s3_bucket.peaks-data-bucket.id}/*" # Objects within the bucket
        ]
      }
    ]
  })
}

resource "aws_iam_policy" "cloudwatch_logs_policy" {
  name        = "CloudWatchLogsPolicy"
  description = "IAM policy for writing to CloudWatch Logs"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Resource = ["${aws_cloudwatch_log_group.ecs_logs.arn}*"]

      }
    ]
  })
}


resource "aws_iam_policy_attachment" "log_attachement" {
  name       = "log-attachment"
  roles      = [aws_iam_role.s3_role.name]
  policy_arn = aws_iam_policy.cloudwatch_logs_policy.arn
}


resource "aws_iam_policy_attachment" "example_attachment" {
  name       = "example-attachment"
  roles      = [aws_iam_role.s3_role.name]
  policy_arn = aws_iam_policy.s3_access_policy.arn
}

