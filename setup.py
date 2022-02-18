from os.path import join, dirname
from typing import List
from setuptools import setup, find_packages
from pkg_resources import parse_requirements

from plataurus import __version__, __package_name__, __author__, __email__, __doc__, __url__


def load_requirements(filename: str) -> List:
    requirements = []

    with open(filename, 'r') as file:
        for requirement in parse_requirements(file.read()):
            extras = '[{}]'.format(','.join(requirement.extras)) if requirement.extras else ''
            requirements.append('{}{}{}'.format(requirement.name, extras, requirement.specifier))

    return requirements


setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    long_description=open(join(dirname(__file__), "README.md")).read(),
    url=__url__,
    description=__doc__,
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.8",
    install_requires=load_requirements("requirements.txt"),
    extras_require={'dev': load_requirements('requirements.dev.txt')},
    entry_points={
        'console_scripts': [
            '{0}-app = {0}.__main__:main'.format(__package_name__),
        ]
    },
    include_package_data=True

)