#!/usr/bin/env python

import os
import json
import argparse
import sys
from classDef import *
from webBuilder import *


#########1. PROGRAM ARGUMENTS #############

#1.1 Create object for argument parsinng
parser = argparse.ArgumentParser(prog="htmlHubManager",description="HTML Hub Manager. Creates an HTML document indexing all web locations registered in a JSON database.\
                                                                    \n Allows JSON database management.")     

#1.2 Definition of input parameters
input_group = parser.add_argument_group('JSON management')
input_group.add_argument('-create-entry', dest="create_entry", action="store_true", help='Create new html entry in the JSON database.')
input_group.add_argument('-update-entry', dest="update_entry",action="store_true", help='Update html entry in the JSON database.')
input_group.add_argument('-delete-entry', dest="delete_entry",action="store_true", help='Delete html entry in the JSON database.')
input_group.add_argument('-show',dest="show", action="store_true", help='Show entry or entries in the JSON database.')
input_group.add_argument('-id', dest="entry_id", metavar="ENTRY_ID", help='Entry ID')

output_group = parser.add_argument_group('HTML document')
output_group.add_argument('-build-html',dest="build_html", action="store_true", help='Build HTML documentation')
output_group.add_argument('-file-html', dest="file_html", metavar="HTML", help='HTML file to output HTML documentation.')

#1.3 Argument parsing
args = parser.parse_args()

#########2. ARGUMENTS CHECKING #############

#2.1 Check number of commands inserted
numCommands = 0
if args.create_entry:
    numCommands = numCommands +1
if args.update_entry:
    numCommands = numCommands +1
if args.delete_entry:
    numCommands = numCommands +1
if args.show:
    numCommands = numCommands +1
if args.build_html:
    numCommands = numCommands +1

if numCommands > 1:
    raise Exception("Sorry!! More than one command introduced.Please select just one.")
elif numCommands == 0:
    raise Exception("Sorry!! No commands inserted.")

#2.2 Check binary arguments
if args.build_html:
    if args.file_html == "":
        raise Exception("Sorry!! Build html was selected but no file-html was provided.")

JSON_FILE = os.path.abspath(os.path.dirname(sys.argv[0])) + "/db.json"

if not os.path.isfile(JSON_FILE):
    open(JSON_FILE, 'a').close()

#########3. SELECT ORDER TO DO #############

if args.create_entry:
    createEntry = JSONEdit() 
    createEntry.setJsonFile(JSON_FILE)
    createEntry.loadJson()
    createEntry.setEditType("CREATE")
    createEntry.run()
elif args.update_entry:
    updateEntry = JSONEdit() 
    updateEntry.setJsonFile(JSON_FILE)
    updateEntry.loadJson()

    if not updateEntry.checkId(args.entry_id):
        raise Exception("Sorry!! " + args.entry_id + " is not a valid entry ID!!")
    
    updateEntry.setEntry(args.entry_id)
    updateEntry.setEditType("UPDATE")
    updateEntry.run()
elif args.delete_entry:
    deleteEntry = JSONDelete() 
    deleteEntry.setJsonFile(JSON_FILE)
    deleteEntry.loadJson()

    if not deleteEntry.checkId(args.entry_id):
        raise Exception("Sorry!! " + args.entry_id + " is not a valid entry ID!!")

    deleteEntry.setEntry(args.entry_id)
    deleteEntry.run()
elif args.show:
    showEntry = JSONShow() 
    showEntry.setJsonFile(JSON_FILE)
    showEntry.loadJson()
    
    if args.entry_id:
        if not showEntry.checkId(args.entry_id):
            raise Exception("Sorry!! " + args.entry_id + " is not a valid entry ID!!")
        else:
            #Show a given entry
            showEntry.setEntry(int(args.entry_id))
            showEntry.setTypeShow("ONE")
            showEntry.run()
    else:
        showEntry.setTypeShow("ALL")
        showEntry.run()

elif args.build_html:
    json = JSONManager()
    json.setJsonFile(JSON_FILE)
    json.loadJson()

    buildHtml = WebBuilder(json.getJsonDict(),args.file_html)   
    buildHtml.buildStyleSheet()
    buildHtml.buildHtml()
    buildHtml.saveHtmlCss() 

























