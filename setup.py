from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    description="Math quiz game",
    author="Nilufar Estiry",
    author_email="nilu.estiry@fau.de",
    url="https://github.com/NiluEst/dsss_homework_2.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)