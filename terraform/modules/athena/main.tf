resource "aws_s3_bucket" "athena_results" {
  bucket = "falcorp-cvm-${var.environment}-athena-results"

  tags = merge(var.tags, {
    Name        = "falcorp-cvm-${var.environment}-athena-results"
    Environment = var.environment
  })
}

resource "aws_s3_bucket_public_access_block" "athena_results" {
  bucket = aws_s3_bucket.athena_results.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "athena_results" {
  bucket = aws_s3_bucket.athena_results.id

  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = var.kms_key_arn
      sse_algorithm     = "aws:kms"
    }
  }
}

resource "aws_s3_bucket_versioning" "athena_results" {
  bucket = aws_s3_bucket.athena_results.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_athena_workgroup" "cvm" {
  name = "cvm-${var.environment}"

  configuration {
    enforce_workgroup_configuration = true

    result_configuration {
      output_location = "s3://${aws_s3_bucket.athena_results.bucket}/"

      encryption_configuration {
        encryption_option = "SSE_KMS"
        kms_key_arn       = var.kms_key_arn
      }
    }
  }

  tags = merge(var.tags, {
    Name        = "cvm-${var.environment}-athena-workgroup"
    Environment = var.environment
  })
}
