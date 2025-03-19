from setuptools import find_packages, setup

from typing import List
def get_requirements(file_path:str)->List[str]:
    '''This fuction will return the requirements'''

    HYPEN_E_DOT='-e.'

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n",' ')for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlProject',
    version='0.0.1',
    author='Ashish Bharti',
    author_email='ashishbharti61841@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')
    

)