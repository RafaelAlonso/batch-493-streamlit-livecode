from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'streamlit==0.65.2',

    'numpy==1.18.4',
    'pandas==0.24.2',
    'joblib==0.14.1',
    'scikit-learn==0.20.4',
    'scipy==1.2.2',
    'xgboost==1.1.1',
    'mlflow==1.8.0',
    'google-cloud-storage==1.26.0',
    'gcsfs==0.6.0',
    'pygeohash',
    'category_encoders',
    'psutil==5.7.0',
    'pygeohash==1.2.0',
    'termcolor==1.1.0',
    'memoized-property==1.0.3',
    'category_encoders==2.2.2']

setup(
    name='TaxiFareModelAPI',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='taxi fare model api'
)
