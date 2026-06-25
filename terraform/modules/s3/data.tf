data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

# =========================================================================
# POLICY DOCUMENTS
# =========================================================================
data "aws_iam_policy_document" "data_engineer_data_lake_policy" {
    statement {
      effect = "Allow"
      resources = [ "${aws_s3_bucket.datalake.arn}/*" ]
      actions = [
        "s3:GetBucketLocation",
        "s3:GetObject",
        "s3:PutObject"
      ]
    }

    statement {
      effect = "Allow"
      resources = [aws_s3_bucket.datalake.arn]
      actions = [ "s3:ListBucket", "s3:GetBucketLocation" ]
    }

    statement {
      effect = "Allow"
      resources = [ "*" ]
      actions = [ "s3:ListAllMyBuckets" ]
    }
}

data "aws_iam_policy_document" "data_scientist_data_lake_policy" {
    statement {
      effect = "Allow"
      resources = [ 
        "${aws_s3_bucket.datalake.arn}/curated/*",
        "${aws_s3_bucket.datalake.arn}/cleaned/*",
      ]
      actions = [
        "s3:GetObject",
      ]
    }

    statement {
      effect = "Allow"
      resources = [aws_s3_bucket.datalake.arn]
      actions = [ "s3:ListBucket", "s3:GetBucketLocation" ]
      condition {
        test = "StringEquals"
        variable = "s3:prefix"
        values = [ "" ]

      }
    }

    statement {
      effect = "Allow"
      resources = [aws_s3_bucket.datalake.arn]
      actions = [ "s3:ListBucket", "s3:GetBucketLocation" ]
      condition {
        test = "StringLike"
        variable = "s3:prefix"
        values = [ 
            "curated/*",
            "cleaned/*"
            ]
        
      }
    }

    statement {
      effect = "Allow"
      resources = [ "*" ]
      actions = [ "s3:ListAllMyBuckets" ]
    }
}

data "aws_iam_policy_document" "data_analyst_data_lake_policy" {
    statement {
      effect = "Allow"
      resources = [ 
        "${aws_s3_bucket.datalake.arn}/curated/*",
        "${aws_s3_bucket.datalake.arn}/cleaned/*",
      ]
      actions = [
        "s3:GetObject",
      ]
    }

    statement {
      effect = "Allow"
      resources = [aws_s3_bucket.datalake.arn]
      actions = [ "s3:ListBucket", "s3:GetBucketLocation" ]
      condition {
        test = "StringEquals"
        variable = "s3:prefix"
        values = [ "" ]

      }
    }

    statement {
      effect = "Allow"
      resources = [aws_s3_bucket.datalake.arn]
      actions = [ "s3:ListBucket", "s3:GetBucketLocation" ]
      condition {
        test = "StringLike"
        variable = "s3:prefix"
        values = [ 
            "curated/*",
            "cleaned/*"
            ]
        
      }
    }

    statement {
      effect = "Allow"
      resources = [ "*" ]
      actions = [ "s3:ListAllMyBuckets" ]
    }
}