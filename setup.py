# Read the contents of your README file
from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pygchat",  # This is the name of your package
    version="0.1.0",  # Update this for new versions
    author="Sapge",
    author_email="sapge.ggfd@gmail.com",
    description="A Chat System to Use in Python games",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-repo",  # Replace with your GitHub repo URL
    packages=find_packages(),  # Automatically find your packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Creative Commons Attribution 4.0 International License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    entry_points={  # If your package has command-line scripts
        "console_scripts": [],
    },
)
