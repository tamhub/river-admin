import os
import sys

from setuptools import setup, find_packages

readme_file = os.path.join(os.path.dirname(__file__), 'README.rst')
try:
    long_description = open(readme_file).read()
except IOError as err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
                     "``long_description`` (%s)\n" % readme_file)
    sys.exit(1)

setup(
    name='river-admin',
    version='0.7.0',
    author='Ahmet DAL',
    author_email='ceahmetdal@gmail.com',
    packages=find_packages(),
    url='https://github.com/javrasya/river-admin.git',
    description='Administration For django-river',
    long_description=long_description,
    install_requires=[
        "Django",
        "mock",
        "django",
        "djangorestframework",
        "djangorestframework-simplejwt",
        "django-cors-headers",
        "django-river>=3.0.0",
    ],
    include_package_data=True,
    zip_safe=False,
    license='BSD',
    platforms=['any'],
)
