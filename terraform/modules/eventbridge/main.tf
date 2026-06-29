resource "aws_cloudwatch_event_rule" "s3_object_created" {
  name        = "cvm-${var.environment}-s3-object-created"
  description = "Trigger Lambda when a new object is uploaded to landing/"

  event_pattern = jsonencode({
    source      = ["aws.s3"]
    detail-type = ["Object Created"]

    detail = {
      bucket = {
        name = [var.bucket_name]
      }

      object = {
        key = [{
          prefix = "landing/"
        }]
      }
    }
  })

  tags = {
    Name        = "cvm-${var.environment}-s3-object-created"
    Environment = var.environment
  }
}

resource "aws_cloudwatch_event_target" "lambda" {
  rule      = aws_cloudwatch_event_rule.s3_object_created.name
  target_id = "schema-validator-lambda"
  arn       = var.lambda_arn
}

resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = var.lambda_function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.s3_object_created.arn
}

resource "aws_cloudwatch_event_rule" "raw_object_created" {
  name        = "cvm-${var.environment}-raw-object-created"
  description = "Detect when a validated file lands in raw/"

  event_pattern = jsonencode({
    source      = ["aws.s3"]
    detail-type = ["Object Created"]

    detail = {
      bucket = {
        name = [var.bucket_name]
      }

      object = {
        key = [{
          prefix = "raw/"
        }]
      }
    }
  })

  tags = {
    Name        = "cvm-${var.environment}-raw-object-created"
    Environment = var.environment
  }
}
resource "aws_cloudwatch_event_target" "glue_starter_lambda" {
  rule      = aws_cloudwatch_event_rule.raw_object_created.name
  target_id = "glue-starter-lambda"
  arn       = var.glue_starter_lambda_arn
}

resource "aws_lambda_permission" "allow_eventbridge_to_start_glue" {
  statement_id  = "AllowExecutionFromRawEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = var.glue_starter_lambda_function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.raw_object_created.arn
}

resource "aws_cloudwatch_event_rule" "glue_job_succeeded" {
  name        = "cvm-${var.environment}-glue-job-succeeded"
  description = "Trigger crawler starter when Glue ETL job succeeds"

  event_pattern = jsonencode({
    source      = ["aws.glue"]
    detail-type = ["Glue Job State Change"]

    detail = {
      jobName = [var.glue_job_name]
      state   = ["SUCCEEDED"]
    }
  })

  tags = {
    Name        = "cvm-${var.environment}-glue-job-succeeded"
    Environment = var.environment
  }
}

resource "aws_cloudwatch_event_target" "crawler_starter_lambda" {
  rule      = aws_cloudwatch_event_rule.glue_job_succeeded.name
  target_id = "crawler-starter-lambda"
  arn       = var.crawler_starter_lambda_arn
}

resource "aws_lambda_permission" "allow_eventbridge_to_start_crawler" {
  statement_id  = "AllowExecutionFromGlueSuccessEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = var.crawler_starter_lambda_function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.glue_job_succeeded.arn
}
