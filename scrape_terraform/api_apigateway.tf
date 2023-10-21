resource "aws_apigatewayv2_api" "peaks-api" {
  name          = "peaks"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_stage" "example" {
  api_id = aws_apigatewayv2_api.peaks-api.id
  auto_deploy = "true"
  name   = "example-stage"
}

resource "aws_apigatewayv2_route" "peaks-route" {
  api_id    = aws_apigatewayv2_api.peaks-api.id
  route_key = "GET /bestpeaks"
  target    = "integrations/${aws_apigatewayv2_integration.peaksintegration.id}"
}

resource "aws_apigatewayv2_integration" "peaksintegration" {
  api_id             = aws_apigatewayv2_api.peaks-api.id
  integration_type   = "AWS_PROXY"
  description        = "Lambda integration"
  integration_uri = aws_lambda_function.peaks_lambda.invoke_arn
}

resource "aws_lambda_function" "peaks_lambda" {
  filename      = "lambdacode.zip"
  function_name = "get-peaks-function"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.10"
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


resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.peaks_lambda.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_apigatewayv2_api.peaks-api.execution_arn}/*/*"
}