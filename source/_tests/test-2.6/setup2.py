from distutils.core import setup

try:
    readme = open('docs/README.txt', 'rt').read()
    changes = open('docs/CHANGES.txt', 'rt').read()
except IOError:
    readme = ""
    changes = ""

setup(name='Supporting Python 3 examples',
      version="1.0",
      packages=['test'],
      package_dir={'test': 'src2'},
      description="The example project for Supporting Python 2",
      long_description=readme + '\n' + changes,
      classifiers=[
          "Programming Language :: Python :: 2",
          "Topic :: Software Development :: Documentation"],
      keywords='python3 porting documentation examples',
      author='Lennart Regebro',
      author_email='regebro@gmail.com',
      license='GPL')
