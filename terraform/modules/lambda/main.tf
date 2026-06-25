data "archive_file" "schema_validator" {
  type        = "zip"
  source_file = "${path.module}/schema_validator.py"
  output_path = "${path.module}/schema_validator.zip"
}

resource "aws_iam_role" "lambda_role" {
  name = "cvm-${var.environment}-schema-validator-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "lambda_policy" {
  name = "cvm-${var.environment}-schema-validator-policy"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject"
        ]
        Resource = "arn:aws:s3:::${var.bucket_name}/*"
      },

    {
       Effect = "Allow"
       Action = [
       "s3:ListBucket"
     ]
      Resource = "arn:aws:s3:::${var.bucket_name}"
   },
      {
        Effect = "Allow"
        Action = [
          "kms:Decrypt",
          "kms:Encrypt",
          "kms:GenerateDataKey"
        ]
        Resource = var.kms_key_arn
      },
      {
        Effect = "Allow"
        Action = [
          "sns:Publish"
        ]
        Resource = var.sns_topic_arn
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "*"
      }
    ]
  })
}
resource "aws_lambda_function" "schema_validator" {
  function_name = "cvm-${var.environment}-schema-validator"
  role          = aws_iam_role.lambda_role.arn
  handler       = "schema_validator.lambda_handler"
  runtime       = "python3.12"

  filename         = data.archive_file.schema_validator.output_path
  source_code_hash = data.archive_file.schema_validator.output_base64sha256

  environment {
    variables = {
      BUCKET_NAME   = var.bucket_name
      SNS_TOPIC_ARN = var.sns_topic_arn
    }
  }

  tags = {
    Name        = "cvm-${var.environment}-schema-validator"
    Environment = var.environment
  }
}

resource "aws_cloudwatch_log_group" "schema_validator" {
  name              = "/aws/lambda/cvm-${var.environment}-schema-validator"
  retention_in_days = 30

  tags = {
    Environment = var.environment
    Name        = "cvm-${var.environment}-schema-validator"
  }
}

