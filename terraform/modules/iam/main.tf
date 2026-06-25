data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

# Data Engineer Role - Full access to sensitive and general data
resource "aws_iam_role" "data_engineer" {
    name = "data-engineer-${var.environment}"
    assume_role_policy = data.aws_iam_policy_document.data-roles-policy.json
    tags = merge(
        var.tags,
        {
            Name = "data-engineer-${var.environment}"
            Environment = var.environment
            Purpose = "Data Engineering"
        }
    )
}

# Data Scientist - Accesss to general data for ML/Analytics
resource "aws_iam_role" "data_scientist" {
    name = "data-scientist-${var.environment}"
    assume_role_policy = data.aws_iam_policy_document.data-roles-policy.json
    tags = merge(
        var.tags,
        {
            Name = "data-scientist-${var.environment}"
            Environment = var.environment
            Purpose = "Data Scientist"
        }
    )
}

# Data Analyst - Access to Curated Data Only
resource "aws_iam_role" "data_analyst" {
    name = "data-analyst-${var.environment}"
    assume_role_policy = data.aws_iam_policy_document.data-roles-policy.json
    tags = merge(
        var.tags,
        {
            Name = "data-analyst-${var.environment}"
            Environment = var.environment
            Purpose = "Data Analyst"
        }
    )
}
