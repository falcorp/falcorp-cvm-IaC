output "lambda_arn" {
  value = aws_lambda_function.crawler_starter.arn
}

output "lambda_function_name" {
  value = aws_lambda_function.crawler_starter.function_name
}
