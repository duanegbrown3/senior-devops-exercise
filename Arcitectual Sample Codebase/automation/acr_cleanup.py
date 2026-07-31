#!/usr/bin/env python3

import argparse

try:
    from azure.identity import DefaultAzureCredential
    from azure.containerregistry import ContainerRegistryClient
except ImportError:
    print("Install requirements first:")
    print("pip install -r automation/requirements.txt")
    raise


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--registry", required=True)

    parser.add_argument("--keep", type=int, default=10)

    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()

    endpoint = f"https://{args.registry}.azurecr.io"

    credential = DefaultAzureCredential()

    client = ContainerRegistryClient(endpoint, credential)

    print(f"Connected to {endpoint}")

    for repository in client.list_repository_names():

        print(f"\nRepository: {repository}")

        artifacts = list(client.list_manifest_properties(repository))

        artifacts.sort(key=lambda x: x.last_updated_on, reverse=True)

        keep = artifacts[: args.keep]

        remove = artifacts[args.keep :]

        print(f"Keeping {len(keep)} images")

        for manifest in remove:

            print(f"Deleting {manifest.digest}")

            if not args.dry_run:
                client.delete_manifest(repository, manifest.digest)


if __name__ == "__main__":
    main()