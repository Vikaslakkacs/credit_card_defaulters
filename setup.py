from setuptools import setup 
from typing import List
##Declaring variabled for setup
PROJECT_NAME="credit-card-defaulter"
VERSION="0.0.1"
AUTHOR="Vikas Laka"
PACKAGES=["credit"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """This function returns list of packages that are required for project
        Considers all the packages that are present in requirements.txt file

    Returns:
        List: List of packages
    """
    with open(REQUIREMENTS_FILE_NAME,"r") as requirements:
        return requirements.readlines().remove("-e .")

## Defining the variables for setup function
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description="Project to find out defaulters of credit card by given data",
    packages=PACKAGES,## Specify the root package to install
    install_requires=get_requirements_list()## Function returns list of all packages to install
)