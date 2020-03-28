import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bjack-pkg-RICH-MAIALE",
    version="0.0.1",
    author="R Maiale",
    author_email="richm1123@gmail.com",
    description="module that creates a random card value for a blackjack game",
    long_description="module that creates a random card value for a blackjack game",
   long_description_content_type="Markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
