"""
Once the project is set up, run the following command on the console
to make use of the entry-points:
>>> pip install -e .

This will enable the user to run the module from the command line
as follows:
>>> xyz
"""

from setuptools import find_packages, setup

PACKAGE_VERSION = "0.1.0"

requirements = [
    "pandas",
    "matplotlib",
    "seaborn",
    "python-dotenv",
    "autopep8",
    "pylint"
]

setup(
    name="travel-insurance-claim",
    version=PACKAGE_VERSION,
    packages=find_packages(where=".", exclude=["tests", "tests.*"]),
    install_requires=requirements,
    python_requires="==3.10.22",
    keywords="travel-insurance",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "xyz = travel_insurance_claim.cli:main"
        ]
    }
)
