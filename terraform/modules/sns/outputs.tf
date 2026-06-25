output "topic_arn" {
  description = "ARN of the SNS validation alerts topic"
  value       = aws_sns_topic.validation_alerts.arn
}

output "topic_name" {
  description = "Name of the SNS validation alerts topic"
  value       = aws_sns_topic.validation_alerts.name
}
