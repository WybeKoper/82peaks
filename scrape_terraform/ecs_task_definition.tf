resource "aws_ecs_task_definition" "service" {
  family                   = "peaks-service"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = 256
  memory                   = 512
  execution_role_arn       = aws_iam_role.s3_role.arn
  container_definitions = jsonencode([
    {
      name      = "peaks-scraper-image"
      image     = "docker.io/9923/peakscraper:3"
      cpu       = 256
      memory    = 512
      essential = true
      environment = [
        { "name" : "S3_BUCKET", "value" : "${aws_s3_bucket.peaks-data-bucket.id}" }
      ]
      portMappings = [
        {
          containerPort = 80
          hostPort      = 80
        }
      ]
    },
  ])
}