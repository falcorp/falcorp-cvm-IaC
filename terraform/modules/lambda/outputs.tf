output "lambda_arn" {
  value = aws_lambda_function.schema_validator.arn
}

output "lambda_function_name" {
  value = aws_lambda_function.schema_validator.function_name
}
