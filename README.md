# paranoYa
application for pseudorandom number generators testing


# Project status:
* Documentation can be found in <em>documentation/</em> folder, it includes chapters from analysis to application implementation,
* GUI implementation is in progress, latest changes can be found in <em>src/</em> folder,
* set of tests such as NIST, FIPS, Diehard will be part of application testing, implementation is currently in early stages. 



# GUI instructions: 
**convert .ui file to Python code**

`pyuic5 <path>/<file_from> -o <path>/<file_to>`

**convert .ui file to Python code with included main func**

`pyuic5 -x <path>/<file_from> -o <path>/<file_to>`

**update packages from requirements file**

`pip freeze > <path>/requirements.txt`

**install packages from requirements file**

`pip install -r <path>/requirements.txt`
