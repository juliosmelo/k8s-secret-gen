#!/usr/bin/env python3
import yaml
import base64
from .lib import create_secrets

if __name__ == '__main__':
    create_secrets('test.yaml')
