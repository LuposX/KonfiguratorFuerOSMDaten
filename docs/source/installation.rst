Installation
============

Installation for local development
----------------------------------

To install KonfiguratorFuerOSMDaten for local devlopment, clone the package from Github::

    $ git clone https://github.com/LuposX/KonfiguratorFuerOSMDaten.git
    $ cd KonfiguratorFuerOSMDaten

For development, use of a virtual environment is strongly recommended. For example
using ``venv``:

.. code-block:: console

    $ python3 -m PSE .
    $ pip install -r requirements.txt
    (PSE) $ 

Or using ``conda``:

.. code-block:: console

    $ conda env create --file enviroment2.yml
    $ conda activate PSE
    (PSE) $ 

.. note 
   correct enviroment.yaml
   
Testing KonfiguratorFuerOSMDaten
--------------------------------

To test hat the installed libaries are working correctly
the tests in the ``test`` folder can be used:  

.. code-block:: console

    $ cd pythoncode
    $ cd tests
    $ cd libaryTests

Each file is a test for one functionality of a libary that is needed in our project,
to test ``.py`` files:

.. code-block:: console

    $ python script_name.py
    
To test ``.ipynb`` files:

.. code-block:: console

    $ jupyter-lab

and run the files in jupyter-lab. If the libaries are correctly installed you shouldn't
get any errors, when running a file.

