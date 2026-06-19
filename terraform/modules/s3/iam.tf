# Data Engineer
resource "aws_iam_policy" "data_engineer_data_lake_policy" {
  name = "Falcorp-CVM-data-engineer-data-lake-${var.environment}"
  description = "Policy to govern data engineer access to S3 data lake."
  policy = data.aws_iam_policy_document.data_engineer_data_lake_policy.json
}
resource "aws_iam_role_policy_attachment" "data_engineer_data_lake_policy_attachment" {
    role = var.data_engineer_role_name
    policy_arn = aws_iam_policy.data_engineer_data_lake_policy.arn
}

# Data Scientist
resource "aws_iam_policy" "data_scientist_data_lake_policy" {
    name = "Falcorp-CVM-data-scientist-data-lake-policy-${var.environment}"
    description = "Policy to govern data scientist access to S3 data lake."
    policy = data.aws_iam_policy_document.data_scientist_data_lake_policy.json
}

resource "aws_iam_role_policy_attachment" "data_scientist_data_lake_policy_attachment" {
    role = var.data_scientist_role_name
    policy_arn = aws_iam_policy.data_scientist_data_lake_policy.arn
}

# Data Analyst
resource "aws_iam_policy" "data_analyst_iam_policy" {
    name = "Falcorp-CVM-data-analyst-data-lake-policy-${var.environment}"
    description = "Policy to govern data analyst access to S3 data lake."
    policy = data.aws_iam_policy_document.data_analyst_data_lake_policy.json
}
resource "aws_iam_role_policy_attachement" "data_analyst_data_lake_policy_attachment" {
    role = var.data_analyst_role_name
    policy_arn = aws_iam_policy.data_analyst_data_lake_policy.arn
}

