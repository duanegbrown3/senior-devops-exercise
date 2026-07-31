# Cloud Native DevOps Platform

> **Senior DevOps Engineering Exercise**

A cloud-native reference implementation demonstrating Infrastructure as Code, CI/CD, containerisation, Kubernetes, GitOps, observability and operational automation on **Microsoft Azure**.

---

## Solution Overview

This solution implements a highly available microservice-based platform designed around modern DevOps and Site Reliability Engineering practices.

The platform provisions Azure infrastructure using **Terraform**, builds multiple applications using **GitHub Actions**, stores container images within **Azure Container Registry (ACR)**, and deploys workloads to an existing **Azure Kubernetes Service (AKS)** cluster using a **GitOps** workflow managed by **ArgoCD**.

The architecture has been intentionally designed to be modular, scalable and maintainable while assuming an enterprise Azure platform already exists.

---

## Architecture

<p align="center">
    <img src="docs/diagrams/architecture-overview.png" width="100%">
</p>

---

# Features

- Infrastructure as Code using Terraform
- Modular Terraform architecture
- Azure Resource Group provisioning
- Azure Container Registry provisioning
- GitHub Actions CI/CD
- OIDC authentication to Azure
- Multi-language application builds
- Docker image build and publishing
- Kubernetes deployments
- GitOps deployment using ArgoCD
- Prometheus monitoring
- Grafana dashboards
- Loki log aggregation
- Alertmanager alert routing
- Slack notifications
- Trivy security scanning
- Renovate dependency management
- Python operational automation

---

# Technology Stack

| Category | Technology |
|------------|------------|
| Cloud | Microsoft Azure |
| Infrastructure as Code | Terraform |
| CI/CD | GitHub Actions |
| Container Runtime | Docker |
| Container Registry | Azure Container Registry |
| Container Orchestration | Kubernetes (AKS) |
| GitOps | ArgoCD |
| Monitoring | Prometheus |
| Dashboards | Grafana |
| Logging | Loki |
| Alerting | Alertmanager |
| Notifications | Slack |
| Security Scanning | Trivy |
| Dependency Management | Renovate |
| Authentication | Microsoft Entra ID (OIDC) |
| Java Service | Java 21 |
| Main Application | Node.js |
| Scheduled Tasks | Python |

---

# Repository Structure

```text
.
├── apps
│   ├── auth-service
│   ├── main-app
│   └── cleanup-job
│
├── automation
│   ├── update_manifests.py
│   ├── health_check.py
│   └── acr_cleanup.py
│
├── terraform
│   ├── environments
│   └── modules
│
├── k8s
│
├── argocd
│
├── monitoring
│
├── docs
│
└── .github
    └── workflows
```

---

# Applications

## Auth Service

A Java microservice responsible for authentication and authorisation of inbound HTTP requests before traffic reaches downstream applications.

### Responsibilities

- Authentication
- Authorisation
- Request validation
- PostgreSQL lookups
- Health endpoint

---

## Main Application

A Node.js application responsible for servicing requests from mobile clients.

### Responsibilities

- Business logic
- Cassandra read/write operations
- REST API
- Health endpoint

---

## Cleanup Job

A scheduled Python application responsible for archiving historical data from Cassandra.

### Responsibilities

- Scheduled execution
- Data archival
- Cassandra maintenance
- Operational housekeeping

---

# Infrastructure

Infrastructure is provisioned using reusable Terraform modules.

Current modules include:

- Resource Group
- Azure Container Registry

The modular design allows future infrastructure components to be added without impacting existing deployments.

---

# Continuous Integration

GitHub Actions is used as the CI platform.

The pipeline performs:

- Checkout source
- Terraform validation
- Security scanning
- Java build
- Node build
- Python validation
- Docker image creation
- Image publishing
- Artifact generation

Images are versioned using immutable Git commit SHAs.

---

# Continuous Delivery

Deployment follows a GitOps workflow.

ArgoCD continuously monitors Kubernetes manifests stored in Git and reconciles the desired state into the Kubernetes cluster.

No manual deployments are performed.

---

# Kubernetes

Each application is deployed using Kubernetes resources.

## Auth Service

- Deployment
- Service
- ReplicaSet
- Pods
- Startup Probe
- Readiness Probe
- Liveness Probe

## Main Application

- Deployment
- Service
- ReplicaSet
- Pods
- Startup Probe
- Readiness Probe
- Liveness Probe

## Cleanup Job

- Kubernetes CronJob

---

# Monitoring & Observability

The platform has been designed around operational visibility.

## Metrics

Prometheus collects application and infrastructure metrics.

## Dashboards

Grafana visualises application and platform health.

## Logging

Loki centralises application logs.

## Alerting

Alertmanager routes alerts to Slack for operational awareness.

Observability is treated as a first-class concern to improve troubleshooting, incident response and operational visibility.

---

# Security

The platform incorporates multiple security controls.

- GitHub OIDC authentication
- Microsoft Entra ID federation
- Azure RBAC
- Private container registry
- Container image scanning using Trivy
- Principle of Least Privilege
- Kubernetes health probes
- GitOps deployment model
- Dependency management using Renovate

Long-lived Azure credentials are intentionally avoided through OpenID Connect (OIDC).

---

# Automation

Operational automation is implemented using Python.

## update_manifests.py

Updates Kubernetes image tags during release processes.

## health_check.py

Performs service health validation.

## acr_cleanup.py

Removes stale images from Azure Container Registry.

---

# Assumptions

This exercise intentionally focuses on application delivery rather than provisioning an enterprise Azure platform.

The following components are assumed to already exist.

| Component | Status |
|------------|--------|
| Azure Subscription | Existing |
| Microsoft Entra ID | Existing |
| OIDC Federation | Configured |
| AKS Cluster | Existing |
| Virtual Network | Existing |
| Public Subnet | Existing |
| Private Subnet | Existing |
| Database Subnet | Existing |
| Azure Firewall | Existing |
| Network Security Groups | Existing |
| Azure DNS | Existing |
| Ingress Controller | Existing |
| PostgreSQL | Existing |
| Cassandra | Existing |
| Prometheus | Existing |
| Grafana | Existing |
| Loki | Existing |
| Alertmanager | Existing |
| Slack Workspace | Existing |

---

# Design Principles

This solution was designed around the following principles.

- Infrastructure as Code
- Immutable Infrastructure
- GitOps
- Automation First
- Observability by Design
- Secure by Default
- Modular Infrastructure
- Operational Simplicity

---

# Considerations

## Security

Authentication to Azure uses OIDC to eliminate long-lived credentials.

Infrastructure is managed declaratively through Terraform while deployments are controlled through GitOps, reducing manual intervention and configuration drift.

Container images are scanned using Trivy before publication.

---

## Scalability

Applications are deployed as stateless Kubernetes workloads allowing horizontal scaling through replica expansion.

Azure Kubernetes Service provides orchestration while Azure Container Registry provides scalable image distribution.

---

## Maintainability

Reusable Terraform modules, GitHub Actions workflows and Python automation reduce duplication and improve maintainability.

Repository organisation separates infrastructure, applications and operational tooling into clearly defined domains.

---

## Cost Effectiveness

The solution provisions only the resources required for the exercise.

Existing enterprise platform services such as networking, AKS, monitoring and databases are assumed to already exist.

Automation reduces operational overhead while Renovate assists with ongoing dependency maintenance.

---

# Future Improvements

Potential future enhancements include:

- Helm chart packaging
- Multi-environment promotion
- Argo Rollouts
- Blue/Green deployments
- Canary deployments
- Azure Key Vault integration
- External Secrets Operator
- OpenTelemetry
- Horizontal Pod Autoscaler
- Cluster Autoscaler
- Cosign image signing
- Software Bill of Materials (SBOM)
- Policy enforcement using Kyverno or Gatekeeper

---


# Author

Duane Brown