resource "aws_lakeformation_resource" "datalake" {
  arn = var.datalake_bucket_arn
}

resource "aws_lakeformation_permissions" "data_engineer_database" {
  principal   = var.data_engineer_role_arn
  permissions = ["ALL"]

  database {
    name = var.database_name
  }
} 

resource "aws_lakeformation_permissions" "data_scientist_database" {
  principal   = var.data_scientist_role_arn
  permissions = ["ALL", "DESCRIBE"]

  database {
    name = var.database_name
  }
}

resource "aws_lakeformation_permissions" "data_analyst_database" {
  principal   = var.data_analyst_role_arn
  permissions = ["ALL", "DESCRIBE"]

  database {
    name = var.database_name
  }
}
