"""
This is the build script for setuptools. It tells setuptools about your
package (such as the name and version) and any packages it depends on.
"""

from setuptools import setup, find_packages

setup(
    name="Your-Project-Name",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    license="MIT",
    description="A short description of your project",
    long_description=open("README.md").read(),
    install_requires=["numpy"],  # add your project dependencies here
    url="https://github.com/yourusername/your-project",
    author="Your Name",
    author_email="your.email@example.com",
)
