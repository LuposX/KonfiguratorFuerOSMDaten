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
5. Install the new enviroment via `conda env create --file requirement.yml`
6. type `conda activate PSE` in your terminal, to activate the newly installed enviroment
7. start your favourite IDE open the project and start coding :)
7.1 Make sure you have selected the conda enviroment as python interpreter in your ide.

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
