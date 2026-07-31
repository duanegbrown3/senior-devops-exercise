module "resource_group" {

  source = "../../components/resource-group"

  name     = local.resource_group.name
  location = var.location
  tags     = local.tags

}

module "acr" {

  source = "../../components/acr"

  name = local.acr.name

  location = var.location

  resource_group_name = module.resource_group.name

  sku = local.acr.sku

  tags = local.tags

}