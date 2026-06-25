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
# ===============================================================
# S3
# ===============================================================
module "s3" {
  source = "../../modules/s3"
  environment = "dev"
  kms_key_arn = module.security.kms_key_arn
  data_engineer_role_name = module.iam.data_engineer_role_name
  data_scientist_role_name = module.iam.data_scientist_role_name
  data_analyst_role_name = module.iam.data_analyst_role_name
}

module "security" {
  source = "../../modules/security"

  environment = "dev"
}

# ===============================================================
# IAM
# ===============================================================

module "iam" {
  source = "../../modules/iam"
  environment = "dev"
}
