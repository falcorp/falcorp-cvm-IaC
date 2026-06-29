data "archive_file" "glue_job_starter" {
  type        = "zip"
  source_file = "${path.module}/glue_job_starter.py"
  output_path = "${path.module}/glue_job_starter.zip"
}

resource "aws_iam_role" "lambda_role" {
  name = "cvm-${var.environment}-glue-starter-role"

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
  name = "cvm-${var.environment}-glue-starter-policy"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "glue:StartJobRun"
        ]
        Resource = "*"
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

resource "aws_lambda_function" "glue_job_starter" {
  function_name = "cvm-${var.environment}-glue-job-starter"
  role          = aws_iam_role.lambda_role.arn
  handler       = "glue_job_starter.lambda_handler"
  runtime       = "python3.12"

  filename         = data.archive_file.glue_job_starter.output_path
  source_code_hash = data.archive_file.glue_job_starter.output_base64sha256

  environment {
    variables = {
      GLUE_JOB_NAME = var.glue_job_name
    }
  }

  tags = {
    Name        = "cvm-${var.environment}-glue-job-starter"
    Environment = var.environment
  }
}
