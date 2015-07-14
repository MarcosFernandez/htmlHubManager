.. HTML Web Hub documentation master file, created by
   sphinx-quickstart on Mon Jul 13 16:10:56 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

HTML Web Hub
============

HTML Hub Manager creates an HTML document indexing all web locations registered in a JSON database. This JSON database could be managed through a set of commands
to create, update, remove and show entries.

JSON Database Management
------------------------

Create new register
```````````````````
To insert a new html entry you must use ``-create-entry`` command. Insert an appropiate *title name* and *web location*. It can be an url or a path to some html document.

::

    htmlHubManager.py -create-entry
    Insert title: NCBI          
    Insert web location: http://www.ncbi.nlm.nih.gov/

    htmlHubManager.py -create-entry
    Insert title: MyWeb           
    Insert web location: ./mydirectory/myWeb.html


Update register
```````````````
To update a given register you must know its ID (``see show registers``) and use ``-update-entry`` command.

::

    htmlHubManager.py -update-entry -id 0
    Insert new title: Genome Browser
    Insert new web location: http://genome.ucsc.edu/
    Entry updated successfully :
        ID: 0 
        title: Genome Browser 
        web_location: http://genome.ucsc.edu/ 


Remove register
```````````````
For removing an entry use ``-delete-entry`` command. You must know the register ID to remove an entry (``see show registers``).

::

    htmlHubManager.py -delete-entry -id 2
    Do you want to delete entry 2 title UAB and web_location http://www.uab.cat (Y/N):Y
    Entry 2 was successfully deleted!!


Show registers
``````````````
To show all registers just run ``-show`` and to show a given register use the register id.

::

    All registers:
    htmlHubManager.py -show

    Register 0
    htmlHubManager.py -show -id 0

HTML Building
-------------
To create a web document with a table indexing a set of web sites, just run the command ``-build-html``.

::

    htmlHubManager.py -build-html -file-html mySite.html 

This command will output a html file (mySite.html) and a cascade style sheet file (style.css) located at the same directory of mySite.html.



















