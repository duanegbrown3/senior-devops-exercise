# Darktrace Architectural Design Submission

## Overview

This repository contains my proposed cloud-native architecture and supporting implementation for the Senior DevOps Engineering design exercise. The solution demonstrates a modern Azure-based application delivery platform built using Infrastructure as Code (IaC), CI/CD, GitOps and Kubernetes principles.

## Contents

### 📁 Architectural Sample Codebase

Contains the implementation supporting the proposed architecture, including:

* Terraform Infrastructure as Code
* GitHub Actions CI/CD workflows
* Kubernetes manifests
* ArgoCD configuration
* Application source code
* Python automation scripts
* Monitoring and operational configuration

### 📄 Darktrace Architectural Design Breakdown.pdf

Provides a detailed explanation of the overall solution, architectural decisions, design assumptions, technology selection and how the platform components integrate to satisfy the exercise requirements.

### 📄 Darktrace Architectural RFC.pdf

Documents the proposed architecture in RFC format, outlining the purpose, context, assumptions, design approach and the rationale behind the selected technologies and implementation.

### 🖼️ Illustration 1.png

High-level architecture diagram showing the end-to-end platform, including Azure infrastructure, CI/CD, GitOps workflow, Kubernetes, networking, security and observability.

### 🖼️ Illustration 2.png

Infrastructure-focused diagram illustrating the Azure environment, networking, authentication, application hosting and supporting platform services.

### 🖼️ Illustration 3.png

Application delivery and GitOps workflow illustrating the complete software delivery lifecycle from source control through CI/CD, container publishing, GitOps deployment and runtime monitoring.

## Notes

The solution assumes an existing enterprise Azure platform (including AKS, networking, identity and monitoring services) and focuses on demonstrating how the application platform integrates with these shared services using secure, scalable and maintainable engineering practices.
