output "data_engineer_role_arn" {
    description = "ARN of the Data Engineer IAM role"
    value = aws_iam_role.data_engineer.arn
}

output "data_engineer_role_name" {
    description = "Name of the Data Engineer IAM role"
    value = aws_iam_role.data_engineer.name
}

output "data_scientist_role_arn" {
    description = "ARN of the Data Scientist IAM role"
    value = aws_iam_role.data_scientist.arn
}
output "data_scientist_role_name" {
    description = "Name of the Data Scientist IAM role"
    value = aws_iam_role.data_scientist.name
  
}

output "data_analyst_role_arn" {
    description = "ARN of the Data Analyst IAM role"
    value = aws_iam_role.data_analyst.arn
}

output "data_analyst_role_name" {
    description = "Name of the Data Analyst IAM role"
    value = aws_iam_role.data_analyst.name
}