import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="viewdns-python",
    version="0.0.1",
    author="Michael Scribellito",
    author_email="mscribellito@gmail.com",
    description="Python module to interact with ViewDNS.info API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mscribellito/viewdns-python",
    project_urls={
        "Bug Tracker": "https://github.com/mscribellito/viewdns-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "viewdns"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)