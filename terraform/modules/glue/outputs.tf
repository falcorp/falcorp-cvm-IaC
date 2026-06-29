output "database_name" {
  value = aws_glue_catalog_database.cvm.name
}

output "subscribers_etl_job_name" {
  value = aws_glue_job.subscribers_etl.name
}
