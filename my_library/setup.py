from setuptools import setup, find_packages

setup(
    name="p",  # Add a comma here
    version="0.1.0",  
    packages=find_packages(),
    description="A Python package for calculating perimeters, circumferences, volumes, and surface areas",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="dhejeshananthandhejesh@gmail.com",
    url="https://github.com/dhejesh926/p",  # Link to your GitHub repository
    install_requires=[  # Any dependencies your package requires
        "numpy",  # If you're using numpy, list it here
    ],
    python_requires=">=3.8",  # Specify Python version compatibility
)
