#!/usr/bin/env python3
from yaml import dump, load, FullLoader
import base64

SECRET_API_VERSION = 'v1'


def create_secrets(pod_yaml):
    env_vars = []
    b64_secrets = []
    with open(pod_yaml) as f:
        data = load(f, Loader=FullLoader)
        secret_name = f"secrets-{data['metadata']['name']}"
        containers = data['spec']['template']['spec']['containers']

        for container in containers:
            container_name = container['name']
            pod_environment_variables = container['env']
            for env_var in pod_environment_variables:
                env_var_name = env_var['name']
                env_var_value = env_var['value'].encode('ascii')
                b64_encoded_value = base64.b64encode(
                    env_var_value).decode('ascii')
                b64_secrets.append(
                    {env_var_name: b64_encoded_value})
                secret_item = {'name': env_var_name,
                               'valueFrom': {'secretKeyRef': {'name': secret_name, 'key': env_var_name}}}
                env_vars.append(secret_item)
    result = {'secret': {'name': secret_name,
                         'b64_secrets': b64_secrets}, 'env_vars': env_vars}
    return result


def create_container_env_vars(env_vars):
    secret_yaml = {'env': env_vars}
    return dump(secret_yaml)


def create_secret_yaml(secret_unique_name, secrets):
    yaml = {'apiVersion': SECRET_API_VERSION,
            'kind': 'Secret', 'metadata': {'name': secret_unique_name}, 'type': 'Opaque', 'data': secrets}
    return dump(yaml)
