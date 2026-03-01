from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    '''this function will return the list of requirements'''
    requirement_lst: List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            # read lines from file
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e.
                if requirement and not requirement.startswith('-e .'):
                    requirement_lst.append(requirement)
    except Exception as e:
        print(f"Error reading requirements.txt: {e}")
    return requirement_lst
print(get_requirements())

setup(
    name='network_sec_model',
    version='0.1.0',
    author='Rajvansh Malhotra',
    packages=find_packages(),
    install_requires=get_requirements(),
)



# (file_path: str) -> List[str]:
#     with open(file_path, 'r') as file:
#         return [line.strip() for line in file if line.strip() and not line.startswith('#')]