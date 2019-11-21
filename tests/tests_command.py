import unittest
from yaml import load, dump, FullLoader

from k8s_secret_gen.lib import create_secrets, create_container_env_vars, create_secret_yaml


class TestGenerator(unittest.TestCase):

    def test_create_secret_yaml(self):
        data = create_secrets('test.yaml')
        yaml = create_secret_yaml(
            data['secret']['name'], data['secret']['b64_secrets'])
        loaded_yaml = load(yaml, Loader=FullLoader)
        self.assertEqual(
            len(data['secret']['b64_secrets']), len(loaded_yaml['data']))
        self.assertEqual(data['secret']['b64_secrets'], loaded_yaml['data'])

    def test_create_container_env_vars(self):
        data = create_secrets('test.yaml')
        yaml = create_container_env_vars(data['env_vars'])
        loaded_yaml = load(yaml, Loader=FullLoader)
        self.assertEqual(len(loaded_yaml['env']), len(data['env_vars']))


if __name__ == '__main__':
    unittest.main()
