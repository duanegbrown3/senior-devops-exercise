- name: Update Kubernetes manifests
  run: |
    python automation/update_manifests.py \
      --registry ${{ vars.ACR_NAME }}.azurecr.io \
      --tag ${{ github.sha }}