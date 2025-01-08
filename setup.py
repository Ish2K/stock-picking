from setuptools import setup, find_packages

setup(
    name="stock-picking",  # Replace with your package name
    version="0.1.0",       # Version of your package
    description="A stock-picking system based on Warren Buffett's principles and the Piotroski score.",
    long_description=open("README.md").read(),  # Ensure you have a README.md
    long_description_content_type="text/markdown",
    author="Ishaan Gupta",
    author_email="ishaan.gupta04@hotmail.com",
    url="https://github.com/Ish2K/stock-picking.git",
    packages=find_packages(),  # Automatically finds submodules
    install_requires=[
        "pandas",
        "numpy",
        "yfinance"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",  # Minimum Python version
)
