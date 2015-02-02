from setuptools import setup, find_packages

readme = open('docs/README.txt', 'rt').read()
changes = open('docs/CHANGES.txt', 'rt').read()

setup(name='Supporting Python 3 examples',
      version="1.0",
      description="An example project for Supporting Python 3",
      long_description=readme + '\n' + changes,
      classifiers=[
          "Programming Language :: Python :: 2",
          "Topic :: Software Development :: Documentation"],
      keywords='python3 porting documentation examples',
      author='Lennart Regebro',
      author_email='regebro@gmail.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True)
