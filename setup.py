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
    "pandas==1.3.3",
    "matplotlib==3.4.3",
    "seaborn==0.11.2",
    "python-dotenv==1.0.0",
    "autopep8==1.6.0",
    "pylint==2.14.5"
]

setup(
    name="travel-insurance-claim",
    version=PACKAGE_VERSION,
    packages=find_packages(where=".", exclude=["tests", "tests.*"]),
    install_requires=requirements,
    python_requires="==3.10.6",
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
