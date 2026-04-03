output "acr_login_server" {
  description = "ACR login server URL"
  value       = azurerm_container_registry.main.login_server
}

output "acr_name" {
  description = "ACR resource name"
  value       = azurerm_container_registry.main.name
}

output "container_app_url" {
  description = "Public URL of the container app"
  value       = "https://${azurerm_container_app.main.latest_revision_fqdn}"
}

output "resource_group_name" {
  description = "Resource group name"
  value       = azurerm_resource_group.main.name
}