from setuptools import setup

setup(name='http-server-pytest-fixtures',
      version='0.0.1',
      install_requires=['requests', 'pytest'],
      entry_points={'pytest11': [
          'http_server = http_server_pytest_fixtures.fixtures']},
      package_data={'http_server_pytest_fixtures': ['gencert.sh']},
      packages=['http_server_pytest_fixtures'])
