resource "aws_glue_catalog_database" "cvm" {
  name = "cvm_${var.environment}"

  description = "Glue Data Catalog for CVM platform"
} 

resource "aws_iam_role" "glue" {
  name = "cvm-${var.environment}-glue-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "glue.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
} 

resource "aws_iam_role_policy_attachment" "glue_service" {
  role       = aws_iam_role.glue.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
} 

resource "aws_iam_role_policy" "glue_s3" {
  name = "cvm-${var.environment}-glue-s3-policy"
  role = aws_iam_role.glue.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:ListBucket",
          "s3:PutObject",
          "s3:DeleteObject"
        ]
        Resource = [
          var.bucket_arn,
          "${var.bucket_arn}/*"
        ]
      }
    ]
  })
} 

resource "aws_iam_role_policy" "glue_kms" {
  name = "cvm-${var.environment}-glue-kms-policy"
  role = aws_iam_role.glue.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "kms:Decrypt",
          "kms:Encrypt",
          "kms:GenerateDataKey"
        ]
        Resource = var.kms_key_arn
      }
    ]
  })
}


resource "aws_glue_crawler" "raw" {
  name          = "cvm-${var.environment}-raw-crawler"
  role          = aws_iam_role.glue.arn
  database_name = aws_glue_catalog_database.cvm.name

  s3_target {
    path = "s3://${var.bucket_name}/raw/"
  }
}
resource "aws_glue_job" "subscribers_etl" {
  name     = "cvm-${var.environment}-subscribers-etl"
  role_arn = aws_iam_role.glue.arn

  command {
    name            = "glueetl"
    script_location = "s3://${var.bucket_name}/scripts/subscribers_etl.py"
    python_version  = "3"
  }

  glue_version      = "4.0"
  worker_type       = "G.1X"
  number_of_workers = 2

  default_arguments = {
    "--SOURCE_PATH"  = "s3://${var.bucket_name}/raw/"
    "--TARGET_PATH"  = "s3://${var.bucket_name}/curated/subscribers/"
    "--job-language" = "python"
  }
} 
resource "aws_glue_crawler" "curated_subscribers" {
  name          = "cvm-${var.environment}-curated-subscribers-crawler"
  role          = aws_iam_role.glue.arn
  database_name = aws_glue_catalog_database.cvm.name

  s3_target {
    path = "s3://${var.bucket_name}/curated/subscribers/"
  }
}
