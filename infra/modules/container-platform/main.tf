# Resource Group
resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location

  tags = {
  environment = var.environment
  managed_by  = "terraform"
  project     = var.app_name
  owner       = "matthew.raphael"
  team        = "platform-engineering"
  }
}

# Azure Container Registry
resource "azurerm_container_registry" "main" {
  name                = replace("${var.app_name}${var.environment}acr", "-", "")
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "Basic"
  admin_enabled       = false

  tags = {
  environment = var.environment
  managed_by  = "terraform"
  project     = var.app_name
  owner       = "matthew.raphael"
  team        = "platform-engineering"
  }
}

# Container Apps Environment
resource "azurerm_container_app_environment" "main" {
  name                = "${var.app_name}-${var.environment}-env"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  tags = {
  environment = var.environment
  managed_by  = "terraform"
  project     = var.app_name
  owner       = "matthew.raphael"
  team        = "platform-engineering"
  }
}

# Container App
resource "azurerm_container_app" "main" {
  name                         = "${var.app_name}-${var.environment}"
  container_app_environment_id = azurerm_container_app_environment.main.id
  resource_group_name          = azurerm_resource_group.main.name
  revision_mode                = "Single"

  template {
    container {
      name   = var.app_name
      image  = var.container_image
      cpu    = 0.25
      memory = "0.5Gi"
    }
  }

  ingress {
    external_enabled = true
    target_port      = 5000

    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }

  tags = {
  environment = var.environment
  managed_by  = "terraform"
  project     = var.app_name
  owner       = "matthew.raphael"
  team        = "platform-engineering"
  }
}