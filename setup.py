from setuptools import setup, find_packages

setup(name='find_contact',
      version='0.2.0',
      description='Command line app for JSON contact list',
      url='https://github.com/jdoid/find_contact',
      author='Dean Kirby',
      author_email='jdoid@fastmail.us',
      license='MIT',
      keywords='cli contacts json csv',
      packages=find_packages(),
      package_data={'data': ['data/*.json']},
      include_package_data=True,
      zip_safe=False)