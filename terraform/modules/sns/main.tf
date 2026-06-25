resource "aws_sns_topic" "validation_alerts" {
  name = "cvm-${var.environment}-validation-alerts"

  tags = {
    Name        = "cvm-${var.environment}-validation-alerts"
    Environment = var.environment
  }
}
