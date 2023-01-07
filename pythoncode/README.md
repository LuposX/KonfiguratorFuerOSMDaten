# KonfiguratorFuerOSMDaten

This subfolder contains the code for the project, for more information about the
code check the "Documentation" or the "Entwurfsheft", for more information about
the project check the README.md in the parent folder.


## Development

For the develop enviroment you need to have the following tools installed:
- conda
- git  

For how to install conda, check [this out](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

How to set up the develoment enviroment:
1. `git clone https://github.com/LuposX/KonfiguratorFuerOSMDaten.git`
2. `git checkout dev`
3. switch to dev branch or your feature branch with: `git branch`
4. Go to the folder `pythoncode`
5. type `conda activate base` in your terminal, to activate the base enviroment
6. There are three ways to do this, if one doesn't work try another one, look below fore more details.
7. type `conda activate PSE` in your terminal, to activate the newly installed enviroment
8. start your favourite IDE open the project and start coding :)
8.1 Make sure you have selected the conda enviroment as python interpreter in your ide.

**Way1:**  
Install the new enviroment via `conda env create --file environment.yml`  
or    
Install the new enviroment via `conda env create --file environment2.yml`    


**Way2:**  
1. Create environment with `conda create --name PSE python=3.9.15`  
2. Execute in the terminal `conda install -c anaconda pip`  
3. Execute in the terminal `pip install -r requirements.txt`


**Way3(Manually):**  
1. Create environment with `conda create --name PSE python=3.9.15`  
2. activate the enviroment with `conda activate PSE`  
2. Execute the following command in the exact order:  
- `conda install -c anaconda pip`  
- `conda install -c anaconda cmake`  
- `conda install osmium-tool`  
- `pip install seaborn`  
- `pip install geopandas`  
- `pip install sphinx`  
- `pip install sphinx-book-theme `  
- `pip install psutil`  
- `pip install osmium`  
- `pip install osmnx`  
- `pip install customtkinter`  


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
