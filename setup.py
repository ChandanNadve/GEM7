from setuptools import find_packages,setup
from typing import List

HYPHON_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
    return requirements

setup(
    name='Gem Stone Price Prediction',
    version='0.0.1',
    author='chandan',
    author_email='chandannadve@gmail.com',
    install_requires =['numpy','pandass'],
    packages=find_packages()
)