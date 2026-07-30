variable "name" {}

variable "location" {}

variable "resource_group_name" {}

variable "sku" {
  default = "Basic"
}

variable "tags" {
  type = map(string)
}