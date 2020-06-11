# paranoYa
* [Overview](#overview)
* [Project status](#ps)
* [System requirements](#sr)
* [Development](#dev)
* [Installation](#ins)
* [History](#his)
# Overview

Application for pseudorandom number generators testing. It implements tests suite NIST. NIST tests are a battery of statistical tests for measuring the quality of a random number generator. It contains 15 statistical tests. In addition to testing, also enables other methodologies to estimate the tested sequences.


# <a id="ps"></a>Project status
* Documentation can be found in respective folder, it includes detail view on application and its development,
* GUI is implemented using PyQt Designer and saved as .ui files which can be anytime remodeled and then generated to .py files,
* the application supports testing of pseudo-random sequences using NIST battery of statistical tests,
* tests results are written in .csv files in which user can explore tests details and check whether tests are valid.
 

# <a id="sr"></a>System requirements
* Applications developed by PyQt are cross-platform,
* NIST battery of tests require Python 2.7 version to run. 

# <a id="dev"></a>Development
To obtain application 

`git clone git@github.com:matusjokay/paranoYa.git`

### Application requirements

In order to continue development, application needs certain packages for its proper start. Every plugin needed is registered in requirements.txt file

`pip install -r <path>/requirements.txt`

### Generate files

Another needed step is to generate graphic windows from whose GUI is composed. Convert .ui to .py files

`pyuic5 <path>/<file_from> -o <path>/<file_to>`


### Useful tips

To update requirements file with new added packages

`pip freeze > <path>/requirements.txt`

Convert .ui file to Python code with included main function

`pyuic5 -x <path>/<file_from> -o <path>/<file_to>`

# <a id="ins"></a>Installation
To obtain application 

`git clone git@github.com:matusjokay/paranoYa.git`

User needs to be located in src/ folder and have installed Python interpreter, then following command will run application

`python main.py`


# <a id="his"></a>History
This software is yet incomplete remake of its older version. Before paranoYa existed as a project, developed using Qt framework powered by C++. Todays application is developed using PyQt framework powered by Python.
