resource "aws_apigatewayv2_api" "peaks-api" {
  name          = "peaks"
  protocol_type = "HTTP"
  cors_configuration {
    allow_origins = ["*"]
    allow_methods = ["GET"]
  }
}

resource "aws_apigatewayv2_stage" "example" {
  api_id      = aws_apigatewayv2_api.peaks-api.id
  auto_deploy = "true"
  name        = "example-stage"

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.main_api_gw.arn

    format = jsonencode({
      requestId               = "$context.requestId"
      sourceIp                = "$context.identity.sourceIp"
      requestTime             = "$context.requestTime"
      protocol                = "$context.protocol"
      httpMethod              = "$context.httpMethod"
      resourcePath            = "$context.resourcePath"
      routeKey                = "$context.routeKey"
      status                  = "$context.status"
      responseLength          = "$context.responseLength"
      integrationErrorMessage = "$context.integrationErrorMessage"
      }
    )
  }
}

resource "aws_cloudwatch_log_group" "main_api_gw" {
  name = "/aws/api-gw/${aws_apigatewayv2_api.peaks-api.name}"

  retention_in_days = 1
}

resource "aws_apigatewayv2_route" "peaks-route" {
  api_id    = aws_apigatewayv2_api.peaks-api.id
  route_key = "GET /bestpeaks"
  target    = "integrations/${aws_apigatewayv2_integration.peaksintegration.id}"
}

resource "aws_apigatewayv2_integration" "peaksintegration" {
  api_id           = aws_apigatewayv2_api.peaks-api.id
  integration_type = "AWS_PROXY"
  description      = "Lambda integration"
  integration_uri  = aws_lambda_function.peaks_lambda.invoke_arn
}

resource "aws_lambda_function" "peaks_lambda" {
  filename      = "lambdacode.zip"
  function_name = "get-peaks-function"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.10"
  layers        = ["arn:aws:lambda:eu-central-1:336392948345:layer:AWSSDKPandas-Python310:5"]
  timeout       = 15
  environment {
    variables = {
      S3_BUCKET = aws_s3_bucket.peaks-data-bucket.id
    }
  }
}

resource "aws_cloudwatch_log_group" "handler_lambda" {
  name              = "/aws/lambda/${aws_lambda_function.peaks_lambda.function_name}"
  retention_in_days = 1

}

data "archive_file" "lambda" {
  type        = "zip"
  source_file = "lambda_function.py"
  output_path = "lambdacode.zip"
}

resource "aws_iam_role" "lambda_exec" {
  name = "serverless_example_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "handler_lambda_policy" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "lambda_s3_access" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = aws_iam_policy.s3_access_policy.arn
}



resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.peaks_lambda.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_apigatewayv2_api.peaks-api.execution_arn}/*/*"
}

