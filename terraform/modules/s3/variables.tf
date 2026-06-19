variable "environment" {
  type = string
}

variable "data_engineer_role_name" {
  description = "The name of the Data Engineer IAM role."
  type = string
}

variable "data_scientist_role_name" {
  description = "The name of the Data Scientist IAM role"
  type = string
}
variable "data_analyst_role_name" {
  description = "The name of the Data Analyst IAM role"
  type = string
}