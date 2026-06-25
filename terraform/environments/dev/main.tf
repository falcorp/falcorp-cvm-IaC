# ===============================================================
# VPC
# ===============================================================
module "networking" {
  source = "../../modules/networking"

  environment = "dev"
  vpc_cidr    = "10.0.0.0/16"

  public_subnets = [
    "10.0.1.0/24",
    "10.0.2.0/24"
  ]

  private_subnets = [
    "10.0.11.0/24",
    "10.0.12.0/24"
  ]
}

module "security" {
  source = "../../modules/security"

  environment = "dev"
}

module "iam" {
  source = "../../modules/iam"

  environment = "dev"
}

module "s3" {
  source = "../../modules/s3"

  environment              = "dev"
  kms_key_arn              = module.security.kms_key_arn
  data_engineer_role_name  = module.iam.data_engineer_role_name
  data_scientist_role_name = module.iam.data_scientist_role_name
  data_analyst_role_name   = module.iam.data_analyst_role_name
}

module "sns" {
  source = "../../modules/sns"

  environment = "dev"
}

module "lambda" {
  source = "../../modules/lambda"

  environment   = "dev"
  bucket_name   = module.s3.bucket_name
  sns_topic_arn = module.sns.topic_arn
  kms_key_arn   = module.security.kms_key_arn
}

module "eventbridge" {
  source = "../../modules/eventbridge"

  environment          = "dev"
  bucket_name          = module.s3.bucket_name
  lambda_arn           = module.lambda.lambda_arn
  lambda_function_name = module.lambda.lambda_function_name
}

module "glue" {
  source = "../../modules/glue"

  environment = "dev"
  bucket_name = module.s3.bucket_name
  bucket_arn  = module.s3.bucket_arn
  kms_key_arn = module.security.kms_key_arn
}