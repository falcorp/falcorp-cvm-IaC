resource "aws_s3_bucket" "datalake" {
  bucket = "falcorp-cvm-${var.environment}-datalake"

  tags = {
    Name        = "falcorp-cvm-${var.environment}-datalake"
    Environment = var.environment
  }
}
