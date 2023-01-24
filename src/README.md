# KonfiguratorFuerOSMDaten

This subfolder contains the code for the project, for more information about the
code check the "Documentation" or the "Entwurfsheft", for more information about
the project check the README.md in the parent folder.


## Development

For the develop enviroment you need to have the following tools installed:
- conda (python package managment sytem, alternatively use venv)
- git  

For how to install conda, check [this out](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).  
For what is conda, check [this out](https://conda.io/projects/conda/en/latest/user-guide/concepts/index.html).  


How to set up the develoment enviroment:
1. `git clone https://github.com/LuposX/KonfiguratorFuerOSMDaten.git`
2. `git checkout dev`
3. switch to dev branch or your feature branch with: `git branch`
4. Go to the folder `pythoncode`
5. type `conda activate base` in your terminal, to activate the base enviroment
6. There are three ways to do this Step, if one doesn't work try another one, look below for the different *ways*.
7. type `conda activate PSE` in your terminal, to activate the newly installed enviroment
8. start your favourite IDE open the project and start coding :)  
8.1 Make sure you have selected the conda enviroment as python interpreter in your IDE.


**Way1(Manually):**  
1. Update conda: `conda update conda`.
2. create the enviroment `conda create --name PSE python=3.10`.
3. activate the enviroment `conda activate PSE`.
4. `pip install osmium`, used for parsing osm data.
5. `conda install -c conda-forge osmnx`, used for downloading osm data.
6. `pip install customtkinter`, used as Graphical Interface.
7. `pip install seaborn`, used to visualize data.
8. `pip install pytest`, used for testing pythoncode.
9. `conda install sphinx`, used for documentation.
10. `pip install sphinx-book-theme `, a theme for the documentation.
11. `pip install psutil`, used to monitor system ressources.
12. `pip install tox`, used to automatize testing.
13. `pip install mypy`, used for checking static typing.
14. `pip install jupyterlab`  # only needed for libary tests.
15. `conda install -c conda-forge osmium-tool`, used to split up data.
15. `pip install pytest-cov`, used for coevrage calculation 

If you get problems with Step *4*, try the following command and then do step *6* again:
- `sudo apt-get install build-essential cmake libboost-dev libexpat1-dev zlib1g-dev libbz2-dev`

**Way2(Automatically):**  
Tested on windows 10 and 11(64Bit), might take a while.  
1. Update conda: `conda update conda`.  
2. `conda env create --name PSE --file PSE.yml`  
To update your already existing conda environment, use `conda env update --file PSE.yml --prune`

### How to check if the Installation worked  

1. navigate to the libaryTest folder 
2. execute in the terminal `jupyter-lab` a window should open up
3. on the left sidebar there are files, each file test that one libary is working correctly
4. to execute a libary test, open one of the file and execute the content by either clicking on a cell and pressing "SHIFT + ENTER" or by vlicking at the top at `Run` and then `Run all cells`.


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
