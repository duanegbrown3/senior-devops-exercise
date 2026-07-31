# DevOps Automation

This directory contains operational automation scripts used to support the platform.

## Scripts

### update_manifests.py

Updates Kubernetes deployment manifests with the latest container image tag.

Example:

```bash
python automation/update_manifests.py \
  --registry acrdevopsdemo.azurecr.io \
  --tag a1b2c3d