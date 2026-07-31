locals {

  project = "devops-platform"

  environment = "dev"

  tags = {

    Project     = local.project
    Environment = local.environment
    ManagedBy   = "Terraform"

  }

  resource_group = {

    name = "rg-${local.project}-${local.environment}"

  }

  acr = {

    name = "acrdevopsdemo"

    sku = "Basic"

  }

}