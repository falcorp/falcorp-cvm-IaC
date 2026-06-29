output "workgroup_name" {
  value = aws_athena_workgroup.cvm.name
}

output "results_bucket_name" {
  value = aws_s3_bucket.athena_results.bucket
}

output "results_bucket_arn" {
  value = aws_s3_bucket.athena_results.arn
}
