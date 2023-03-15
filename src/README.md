````
# KonfiguratorFuerOSMDaten

This sub-folder contains the code for the project, for more information about the
code check the "Documentation" or the "Entwurfsheft", for more information about
the project check the README.md in the parent folder.


## Installation of the Development Environment

For the develop environment you need to have the following tools installed:
- Conda/Venv
- git  

To install conda, check [this out](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).  
For what is conda, check [this out](https://conda.io/projects/conda/en/latest/user-guide/concepts/index.html).  

### Installation

This project uses the command-line-tool `osmium`, If you are on Windows you can install it via pip, If you are on linux or Mac
you need to install via conda, because this project has only the binaries for winodws for `osmium`.

How to set up the development environment:
1. `git clone https://github.com/LuposX/KonfiguratorFuerOSMDaten.git`
2. `git checkout main`
3. Install the required Packaged as stated below.
4. Activate your conda/venv environment.
5. You can start the application from the file `src_test/full_application_test/execution_starting_point.py`

#### Installing via Conda 

Tested on windows 10(64Bit), might take a while.  
1. Update conda: `conda update conda`.  
2. Execute from parent directory: `conda env create --name PSE --file enviroment.yml`  

#### Installing via Pip(Only for Windows)

Tested on windows 10(64Bit), might take a while.  
1. Create a venv with the python version `3.10.10`
2. Activate your venv.
3. Install the requirements via: `pip install -r requirements.txt`

#### Manually installing the Packages

If you want to manually install the packasges, here ist a list of packages that are required to run this application:
- `pip install osmium`, used for parsing osm data.
- `pip install customtkinter`, used as Graphical Interface.
- `pip install seaborn`, used to visualize data.
- `pip install pytest`, used for testing pythoncode.
- `conda install -c conda-forge osmium-tool`, used to split up data.
- `pip install screeninfo`, used to center the window.
- `conda install geopandas`, to handle datasets.

For testing , you addtionaly need the following packages:
-` conda install sphinx`, used for documentation.
- `pip install sphinx-book-theme `, a theme for the documentation.
- `pip install tox`, used to automatize testing.
- `pip install mypy`, used for checking static typing.
- `pip install jupyterlab`, only needed for libary tests.

For how to write correct documentation, check [this out](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

## Building the Executable

In order to build the executable you need [cx_freeze](https://cx-freeze.readthedocs.io/en/latest/installation.html).
You can install it with: `pip install --upgrade cx_Freeze`.
After that you need to change the `site_packages` variable in the `setup.py` file, it needs to be set to the 
absolute path of your venv.
After that you can build the project, with the following command:  
```sh
python setup.py build
```

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

````
