terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}

module "container_platform" {
  source = "../../modules/container-platform"

  resource_group_name = "${var.app_name}-dev-rg"
  location            = var.location
  environment         = "dev"
  app_name            = var.app_name
}