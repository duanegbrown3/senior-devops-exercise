output "resource_group_name" {
  description = "Resource Group Name"

  value = module.resource_group.name
}

output "acr_login_server" {
  description = "Azure Container Registry Login Server"

  value = module.acr.login_server
}