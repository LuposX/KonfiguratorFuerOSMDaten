# KonfiguratorFuerOSMDaten

This subfolder contains the code for the project, for more information about the
code check the "Documentation" or the "Entwurfsheft", for more information about
the project check the README.md in the parent folder.


## Development

For the develop enviroment you need to have:
- conda
- git

How to set up the develoment enviroment:
1. `git clone https://github.com/LuposX/KonfiguratorFuerOSMDaten.git`
2. `git checkout dev`
3. switch to dev branch or your feature branch with: `git branch`
4. Go to the folder `pythoncode`
5. install requirements.yml via `conda env create --file requirement.yml`
6. start your favourite IDE open the project and start coding :)

For how to write correct documentation, check [this out](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

## Documentation

To build the Documentation from the source code, execute the following commands:
```sh
sphinx-apidoc -f -o source ../modules
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
