output "lambda_arn" {
  value = aws_lambda_function.glue_job_starter.arn
}

output "lambda_function_name" {
  value = aws_lambda_function.glue_job_starter.function_name
}
