variable "subscription_id" {
  description = "Azure subscription ID"
  type        = string
}

variable "app_name" {
  description = "Name of the application"
  type        = string
  default     = "securedelivery"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastus"
}