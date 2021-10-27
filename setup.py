from setuptools import setup, find_packages

setup(
    name="analyze-example-custom-data-source",
    version="0.1.0",
    description="Meltano project file bundle of Matatika datasets used in our Getting Started Tutorial - Adding a Custom Data Source",
    packages=find_packages(),
    package_data={"bundle": [
        "analyze/datasets/tap-example-custom-data-source/*.yml",
        "analyze/datasets/tap-example-custom-data-source/*.yaml"        
        ]}
)