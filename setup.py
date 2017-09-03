from setuptools import setup

setup(name='snnm',
      version='0.2.4',
      author='Gabriel Lima',
      author_email='gvclima@gmail.com',
      description='Naming helper',
      license='MIT',
      keywords='synonym',
      url='https://github.com/ewilazarus/snnm',
      download_url='https://github.com/ewilazarus/snnm/tarball/0.2.4',
      install_requires=[
          'beautifulsoup4==4.6.0',
          'click==6.7',
          'requests==2.18.4'
      ],
      entry_points={
          'console_scripts': ['snnm=snnm:main']
      })
