terraform {
  required_version = ">= 1.6"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
  backend "s3" {
    bucket = "falcorp-cvm-terraform-state-dev"
    key = "infra-team-lakehouse/terraform.tfstate"
    region = "af-south-1"
    encrypt = true
    use_lockfile = true
    
  }
}

provider "aws" {
  region = "af-south-1"
  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy = "Terraform"
      Project = "Falcorp CVM"
      Owner = "Falcorp"
    }
  }
}


