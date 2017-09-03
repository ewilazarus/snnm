from setuptools import setup
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

requirements = convert_deps_to_pip(Project().parsed_pipfile['packages'], r=False)

setup(name='snnm',
      version='0.2.2',
      author='Gabriel Lima',
      author_email='gvclima@gmail.com',
      description='Naming helper',
      license='MIT',
      keywords='synonym',
      url='https://github.com/ewilazarus/snnm',
      download_url='https://github.com/ewilazarus/snnm/tarball/0.2.2',
      install_requires=requirements,
      entry_points={
          'console_scripts': ['snnm=snnm:main']
      })
