resource "aws_kms_key" "platform" {
  description             = "CVM ${var.environment} platform encryption key"
  deletion_window_in_days = 7
  enable_key_rotation     = true

  tags = {
    Name        = "cvm-${var.environment}-platform-key"
    Environment = var.environment
  }
}

resource "aws_kms_alias" "platform" {
  name          = "alias/cvm-${var.environment}-platform-key"
  target_key_id = aws_kms_key.platform.key_id
}
