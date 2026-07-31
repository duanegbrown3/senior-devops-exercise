.PHONY: lint validate helm terraform

lint:
	yamllint .

helm:
	helm lint helm/*

terraform:
	terraform -chdir=terraform fmt -recursive
	terraform -chdir=terraform validate

validate: terraform helm