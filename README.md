# AKS DevOps Platform

## Overview

This repository demonstrates a production-ready DevOps platform for deploying a highly available microservice application onto Azure Kubernetes Service (AKS).

The platform includes:

- Auth Service (Java)
- Main Application (NodeJS)
- Cleanup Job (Python CronJob)

## Architecture

- Azure Kubernetes Service (Existing)
- Azure Container Registry
- Azure PostgreSQL Flexible Server
- Azure Key Vault
- GitHub Actions
- ArgoCD
- Helm
- Prometheus
- Grafana
- Loki
- Alertmanager

## CI/CD

GitHub Actions is responsible for:

- Validating Terraform
- Linting Helm Charts
- Building Docker Images
- Pushing Images to Azure Container Registry
- Packaging Helm Charts

Deployment is performed by ArgoCD using GitOps.

## Assumptions

- AKS Cluster already exists
- Azure Container Registry is provisioned by Terraform
- Images are deployed using Helm
- Secrets are stored in Azure Key Vault (already exists)