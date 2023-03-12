# KonfiguratorFuerOSMDaten

This subfolder contains the code for the project, for more information about the
code check the "Documentation" or the "Entwurfsheft", for more information about
the project check the README.md in the parent folder.


## Installation of the Development Enviroment

For the develop enviroment you need to have the following tools installed:
- conda (python package managment sytem, alternatively use venv)
- git  

To install conda, check [this out](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).  
For what is conda, check [this out](https://conda.io/projects/conda/en/latest/user-guide/concepts/index.html).  

### Installation

How to set up the develoment enviroment:
1. `git clone https://github.com/LuposX/KonfiguratorFuerOSMDaten.git`
2. `git checkout main`
3. type `conda activate base` in your terminal, to activate the base enviroment
4. Install the required Packaged as stated below.
5. type `conda activate PSE` in your terminal, to activate the newly installed enviroment
6. You can start the application from the file `src_test/full_application_test/execution_starting_point.py`

### Automatically installing the Packages
Tested on windows 10(64Bit), might take a while.  
1. Update conda: `conda update conda`.  
2. Execute from parent directory: `conda env create --name PSE --file enviroment.yml`  

### Manually installing the Packages
1. Update conda: `conda update conda`.
2. create the enviroment `conda create --name PSE python=3.10`.
3. activate the enviroment `conda activate PSE`.
4. `pip install osmium`, used for parsing osm data.
5. `pip install customtkinter`, used as Graphical Interface.
6. `pip install seaborn`, used to visualize data.
7. `pip install pytest`, used for testing pythoncode.
8. `conda install sphinx`, used for documentation.
9. `pip install sphinx-book-theme `, a theme for the documentation.
10. `pip install tox`, used to automatize testing.
11. `pip install mypy`, used for checking static typing.
12. `pip install jupyterlab`  # only needed for libary tests.
13. `conda install -c conda-forge osmium-tool`, used to split up data.
14. `pip install screeninfo`, used to center the window

If you get problems with Step *4*, try the following command and then do step *6* again:
- `sudo apt-get install build-essential cmake libboost-dev libexpat1-dev zlib1g-dev libbz2-dev`

For how to write correct documentation, check [this out](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

## Documentation

To build the Documentation from the source code, execute the following commands:
```sh
sphinx-apidoc -f -o source/apidoc ../src/
```
For html:
```sh
make html
```
For latex:
```sh
make latex
```
For latexPDF:
```sh
make latexpdf
```

The results will then be in the folder `docs/build`.
