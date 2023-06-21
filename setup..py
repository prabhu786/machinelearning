from setuptools import find_packages,setup
from typing import list
HYPEN_E_DOT='-e .'
def get_requirements(file_paths:str)->list[str]:
    '''
       this file will resturn ths list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='machine_learning',
    version='0.0.1',
    author='prabhu_dayal',
    author_email='yadavnsiprabu958@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)