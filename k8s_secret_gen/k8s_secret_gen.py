#!/usr/bin/env python3
import yaml
import base64
import argparse
import pathlib

from lib import create_secrets, create_container_env_vars, create_secret_yaml


def main():
    parser = argparse.ArgumentParser(
        description='Simple cli command to convert Kubernetes container environment variables to secrets')
    parser.add_argument('-f', '--file', help='Deployment YAML',
                        required=True, type=pathlib.Path)
    args = parser.parse_args()
    yaml_data = create_secrets(args.file)
    secret_yaml = create_secret_yaml(
        yaml_data['secret']['name'], yaml_data['secret']['b64_secrets'])
    deployment_env_vars = create_container_env_vars(yaml_data['env_vars'])
    print(secret_yaml)
    print("---")
    print(deployment_env_vars)
    print("---")


if __name__ == '__main__':
    main()
