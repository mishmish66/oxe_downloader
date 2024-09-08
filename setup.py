from setuptools import setup, find_packages

setup(
    name="oxe_downloader",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer",
        "google-cloud-storage",
        "tqdm",
        "typing-extensions",
    ],
    entry_points={
        "console_scripts": [
            "oxe_download=oxe_downloader:app",
        ],
    },
    py_modules=["download"],
    python_requires=">=3.6",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to download and sync datasets from Google Cloud Storage",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dataset-downloader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
