##exposing the VPC ID so other modules can use it later, i.e DB

output "vpc_id" {
  value = aws_vpc.this.id
}
