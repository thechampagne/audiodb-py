import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="audiodb",
    version="1.0.0",
    author="XXIV",
    description="TheAudioDB API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thechampagne/audiodb-py",
    project_urls={
        "Bug Tracker": "https://github.com/thechampagne/audiodb-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)