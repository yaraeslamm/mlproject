from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        # requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Yara',
    author_email='yaraelshehawi@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirement.txt')

)