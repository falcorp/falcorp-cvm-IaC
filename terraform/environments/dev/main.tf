module "networking" {
  source = "../../modules/networking"

  environment = "dev"
  vpc_cidr    = "10.0.0.0/16"
}
