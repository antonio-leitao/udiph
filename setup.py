import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="udiph", 
    version="0.0.2",
    author="Antonio Leitao",
    author_email="aleitao@novaims.unl.pt",
    description="Uniform distributed persistent homology.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Antonio-Leitao/udiph",
    packages=setuptools.find_packages(),
    install_requires=['numpy','scipy','sklearn'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
