data "archive_file" "crawler_starter" {
  type        = "zip"
  source_file = "${path.module}/crawler_starter.py"
  output_path = "${path.module}/crawler_starter.zip"
}

resource "aws_iam_role" "lambda_role" {
  name = "cvm-${var.environment}-crawler-starter-role"

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
  name = "cvm-${var.environment}-crawler-starter-policy"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "glue:StartCrawler"
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

resource "aws_lambda_function" "crawler_starter" {
  function_name = "cvm-${var.environment}-crawler-starter"
  role          = aws_iam_role.lambda_role.arn
  handler       = "crawler_starter.lambda_handler"
  runtime       = "python3.12"
  timeout       = 30

  filename         = data.archive_file.crawler_starter.output_path
  source_code_hash = data.archive_file.crawler_starter.output_base64sha256

  environment {
    variables = {
      CRAWLER_NAME = var.crawler_name
    }
  }

  tags = {
    Name        = "cvm-${var.environment}-crawler-starter"
    Environment = var.environment
  }
}
