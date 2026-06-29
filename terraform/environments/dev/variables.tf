variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "tags" {
  description = "Additional tags for resource"
  type        = map(string)

  default = {
    Environment = "dev"
    ManagedBy   = "Terraform"
    Project     = "Falcorp CVM"
    Owner       = "Falcorp"
  }
}
