from setuptools import setup

setup(name='snnm',
      version='0.1.2',
      author='Gabriel Lima',
      author_email='ewilazarus@gmail.com',
      description='Naming aid',
      license='MIT',
      keywords='synonym',
      url='https://github.com/ewilazarus/snnm',
      packages=['snnm'],
      install_requires=['beautifulsoup4',],
      download_url='https://github.com/ewilazarus/snnm/tarball/0.1.2',
      entry_points={
          'console_scripts': [
              'snnm = snnm.cli:main'
          ]
      })
