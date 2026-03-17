from setuptools import setup, find_packages


setup(
    name="bacon_distance",
    version="0.1.0",
    packages=find_packages(),
    requires=["json", "csv", "flask", "flask_cors"]
)
