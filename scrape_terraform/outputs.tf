output "bucket_name_created" {
  value = aws_s3_bucket.peaks-data-bucket.id
}

output "api_endpoint" {
  value = "${aws_apigatewayv2_stage.example.invoke_url}/bestpeaks"
}