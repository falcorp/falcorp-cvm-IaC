resource "aws_iam_role" "data_engineer" {
  name               = "data-engineer-${var.environment}"
  assume_role_policy = data.aws_iam_policy_document.data_roles_policy.json

  tags = merge(var.tags, {
    Name        = "data-engineer-${var.environment}"
    Environment = var.environment
    Purpose     = "Data Engineering"
  })
}

resource "aws_iam_role" "data_scientist" {
  name               = "data-scientist-${var.environment}"
  assume_role_policy = data.aws_iam_policy_document.data_roles_policy.json

  tags = merge(var.tags, {
    Name        = "data-scientist-${var.environment}"
    Environment = var.environment
    Purpose     = "Data Scientist"
  })
}

resource "aws_iam_role" "data_analyst" {
  name               = "data-analyst-${var.environment}"
  assume_role_policy = data.aws_iam_policy_document.data_roles_policy.json

  tags = merge(var.tags, {
    Name        = "data-analyst-${var.environment}"
    Environment = var.environment
    Purpose     = "Data Analyst"
  })
}
