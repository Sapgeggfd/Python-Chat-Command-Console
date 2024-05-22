import os

from setuptools import find_packages, setup

# Get the version from the environment variable
version = os.getenv("VERSION", "0.0.0")

setup(
    name="pygchat",
    version=version,
    description="Your package description",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/your-repo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Your package dependencies
    ],
)
