import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dispy_markdown",
    version="0.0.1",
    author="EJH2",
    description="discord-markdown, but Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EJH2/dispy-markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'pygments==2.7.2',
        'simpy_markdown @ git+https://github.com/EJH2/simpy-markdown.git'
    ]
)
