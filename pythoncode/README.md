# KonfiguratorFuerOSMDaten

This subfolder contains the code for the project, for more information about the
code check the "Documentation" or the "Entwurfsheft", for more information about
the project check the README.md in the parent folder.


## Development

For the develop enviroment you need to have the following tools installed:
- conda
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
8.1 Make sure you have selected the conda enviroment as python interpreter in your ide.


Way3 works proably the best.

**Way1:**  
Install the new enviroment via `conda env create --file environment.yml`  
or    
Install the new enviroment via `conda env create --file environment2.yml`    


**Way2:**  
1. Create environment with `conda create --name PSE python=3.11`  
2. Execute in the terminal `conda install -c anaconda pip`  
3. Execute in the terminal `pip install -r requirements.txt`


**Way3(Manually):**  
1. Create environment with `conda create --name PSE python=3.11`  
1.1 if python 3.11 doesn't work use python version 3.9.15
2. activate the enviroment with `conda activate PSE`  
2. Execute the following command in the exact order:  
- `conda install -c anaconda pip`  
- `conda install -c anaconda cmake`  
- `conda install osmium-tool`  
- `conda install seaborn -c conda-forge`  
- `conda install geopandas`  
- `conda install -c conda-forge osmnx`  
- `pip install sphinx`  
- `pip install sphinx-book-theme `  
- `pip install psutil`  
- `pip install osmium`  
- `pip install customtkinter`  
- `pip install jupyterlab` # only needed for libary tests

> **_NOTE:_** Strictly speaking, you could also use a python version lower than `3.11` for development, but the deployment python version should be `3.11`, since python `3.11` is up to [60% faster](https://docs.python.org/3/whatsnew/3.11.html) than `3.10`.
 
### How to check if the Installation worked  

For the test that end with `.ipynb` do:  
1. navigate to the libaryTest folder 
2. execute in the terminal `jupyter-lab` a window should open up
3. on the left sidebar there are files, each file test that one libary is working correctly
4. to execute a libary test, open one of the file and execute the content by either clicking on a cell and pressing "SHIFT + ENTER" or by vlicking at the top at `Run` and then `Run all cells`.

For the test that end with `.py` do:  
1. run in the terminal `python script_name.py`

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
