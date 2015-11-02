#!/usr/bin/env python

import os
import json

class JSONManager(object):

    def __init__(self):
        """Class Constructor"""
        self.jsonContent = {}  #Dictionary to represent json database
        self.id_entry = -1     #Identification entry for Update, Delete, Show ID
        self.json_file = None  #JSON File Name

    def setEntry(self,newEntry):
        """Update id entry"""
        self.id_entry = newEntry

    def getEntry(self):
        """Get entry id"""
        return self.id_entry

    def setJsonFile(self,jsonFile):
        """Update Json file"""
        self.json_file = jsonFile

    def checkId(self,idTocheck):
        """Check if id exists in the dictionary"""
        if idTocheck in self.jsonContent:
            return True
        return False


    def loadJson(self):
        if os.stat(self.json_file).st_size == 0:
           return
    
        with open(self.json_file) as json_file:
            self.jsonContent =json.load(json_file)
            
    def saveJson(self):
        with open(self.json_file, 'w') as of:
            json.dump(self.jsonContent, of, indent=2)

    def getJsonDict(self):
        """Get json dictionary"""
        return self.jsonContent


class JSONEdit(JSONManager):
    """JSON Derived class for edit the json database"""
    def __init__(self):
        """Class Constructor"""
        self.type_edit = None    #Create or Update json edition
        JSONManager.__init__(self)

    def setEditType(self,edit="CREATE"):
        """Update edit mode. CREATE or UPDATE"""
        self.type_edit = edit

    def showEntryEdited(self):
        """Show last entry edited"""
        message = "Entry created successfully :"
        if self.type_edit == "UPDATE":
            message = "Entry updated successfully :"

        print message
        print "  ID: %s " % self.id_entry 
        print "  title: %s " % self.jsonContent[str(self.id_entry)]["title"] 
        print "  web_location: %s " % self.jsonContent[str(self.id_entry)]["web_location"]



    def editJson(self,title,webLocation):
        """Edit json file"""
        if self.type_edit == "CREATE":
            newID = -1
            if self.jsonContent:
                newID = int(sorted([int(numeric_string) for numeric_string in self.jsonContent.keys()])[-1])


            
            newID = newID + 1
            self.jsonContent[str(newID)] = {"title":title,"web_location":webLocation}   
            self.id_entry = newID
        elif self.type_edit == "UPDATE":
            self.jsonContent[str(self.id_entry)] = {"title":title,"web_location":webLocation}
           
        #Save JSON File
        self.saveJson()

        self.showEntryEdited()
      

    def run(self):
        """Ask to user for title and web location to create or update"""
        messageTitle = "Insert title: "
        messageWebLocation = "Insert web location: "
        title = ""
        webLocation = ""
        
        if self.type_edit == "UPDATE":
            messageTitle = "Insert new title: "
            messageWebLocation = "Insert new web location: "
         
        #Get title
        while title == "":
            title = raw_input(messageTitle) 
            if title == "":
                print "Sorry!! Title can not be empty!!"

        #Get web location
        while webLocation == "":
            webLocation = raw_input(messageWebLocation)
            if webLocation == "":
                print "Sorry!! web location can not be empty!!"

        #Update JSON
        self.editJson(title,webLocation)      


class JSONDelete(JSONManager):
    """JSON Derived class for deleting records"""
    def __init__(self):
        """Class Constructor"""
        JSONManager.__init__(self)

    def run(self):
        #Confirm entry removal
        toConfirm = True
        
        while toConfirm :
            confirmation = raw_input("Do you want to delete entry %s title %s and web_location %s (Y/N):" \
                           %(self.id_entry,self.jsonContent[self.id_entry]["title"],self.jsonContent[self.id_entry]["web_location"]) )
            
            if confirmation == "Y" or confirmation == "y" or confirmation == "N" or confirmation == "n": 
                toConfirm = False
                
                if confirmation == "Y" or confirmation == "y":
                    self.jsonContent.pop(self.id_entry, None)
                    #Save Json file
                    self.saveJson()
                    print "Entry %s was successfully deleted!!" %self.id_entry
            else:
                print "Sorry!! No correct answer was inserted. You must answer Y or N!!"


class JSONShow(JSONManager):
    """JSON derived class for showing records"""
    def __init__(self):
        """Class Constructor"""
        JSONManager.__init__(self)
        self.type_show = None    #Show ALL records or just ONE

    def setTypeShow(self,newType):
        """Update type of show ALL or ONE"""
        self.type_show = newType
    
    def run(self):
        """Run JSON show"""
        if self.type_show == "ALL":
            print "ID ENTRY \t WEB TITLE \t WEB LOCATION"
            for id_entry in sorted(self.jsonContent):
                print "%s \t %s \t %s" %(id_entry,self.jsonContent[id_entry]["title"],self.jsonContent[id_entry]["web_location"])
        else:
            print "ID ENTRY \t WEB TITLE \t WEB LOCATION"
            print "%s \t %s \t %s"  %(self.id_entry,self.jsonContent[str(self.id_entry)]["title"],self.jsonContent[str(self.id_entry)]["web_location"])


                
            





























        
