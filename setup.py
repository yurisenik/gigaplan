from setuptools import setup

setup(name='gigaplan',
      version='0.1',
      description='Simple Python wrapper for Megaplan API',
      author='Ivanov Ivan',
      author_email='i.ivanov@zebra-group.ru',
      license='MIT',
      install_requires=['requests'],
      packages=['gigaplan'],
      zip_safe=False)
