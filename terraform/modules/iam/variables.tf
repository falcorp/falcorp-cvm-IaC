variable "environment" {
    description = "Environment name"
    type = string
  
}
variable "tags" {
    description = "Additional tags for resource"
    type = map(string)
    default = {}
}