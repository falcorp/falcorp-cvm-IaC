data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

# Generic policy for Data Engineer, Anlyst, and Scientist
data "aws_iam_policy_document" "data-roles-policy" {
    statement {
      effect = "Allow"
      actions = [ "sts:AssumeRole" ]
      resources = [ "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root" ]
    }
}

