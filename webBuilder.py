#!/usr/bin/env python

import os


class WebBuilder(object):
    """Class which manage web building """

    def __init__(self,dictValues,outputHtml):
        """Constructor Class
           dictValues  Dictionary of entries to be printed as HTML TABLE"""
        self.webToPrint = dictValues  #Dictionary of values to be printed in a HTML web table
        self.fileHtml = outputHtml
        
        self.vCss = []            #Vector to be printed as web file
        self.vHTML = []           #Vector of HTML contents
        


    def buildStyleSheet(self):
        ''' Add HTML header to a given vector '''
        self.vCss.append(" #title\n")
        self.vCss.append(" {\n")
        self.vCss.append("   font-family: \"Sans-Serif\";\n")
        self.vCss.append("   font-size: 20px;\n")
        self.vCss.append("   text-align: center;\n")
        self.vCss.append("   color: #039;\n")
        self.vCss.append("   border-collapse: collapse;\n")
        self.vCss.append(" }\n")
        self.vCss.append(" #section\n")
        self.vCss.append(" {\n")
        self.vCss.append("   font-family: \"Sans-Serif\";\n")
        self.vCss.append("   font-size: 18px;\n")
        self.vCss.append("   text-align: center;\n")
        self.vCss.append("   color: #039;\n")
        self.vCss.append("   border-collapse: collapse;\n")
        self.vCss.append(" }\n")
        #LINKS TABLE
        self.vCss.append("#linksTable-b\n")
        self.vCss.append("{\n")
        self.vCss.append("   font-family: \"Sans-Serif\";\n")
        self.vCss.append("	font-size: 12px;\n")
        self.vCss.append("	background: #fff;\n")
        self.vCss.append("	margin: 5px;\n")
        self.vCss.append("	width: 200px;\n")
        self.vCss.append("	border-collapse: collapse;\n")
        self.vCss.append("	text-align: left;\n")
        self.vCss.append("}\n")
        self.vCss.append("#linksTable-b th\n")
        self.vCss.append("{\n")
        self.vCss.append("	font-size: 14px;\n")
        self.vCss.append("	font-weight: normal;\n")
        self.vCss.append("	color: #039;\n")
        self.vCss.append("	padding: 10px 8px;\n")
        self.vCss.append("	border-bottom: 2px solid #6678b1;\n")
        self.vCss.append("}\n")
        self.vCss.append("#linksTable-b td\n")
        self.vCss.append("{\n")
        self.vCss.append("	border-bottom: 1px solid #ccc;\n")
        self.vCss.append("	color: #669;\n")
        self.vCss.append("	padding: 6px 8px;\n")
        self.vCss.append("}\n")
        self.vCss.append("linksTable-b tbody tr:hover td\n")
        self.vCss.append("{\n")
        self.vCss.append("	color: #009;\n")
        self.vCss.append("}\n")
        #BLUE TABLE
        self.vCss.append(" #hor-zebra\n")
        self.vCss.append(" {\n")
        self.vCss.append("   font-family: \"Sans-Serif\";\n")
        self.vCss.append("   font-size: 12px;\n")
        self.vCss.append("   margin: 0px;\n")
        self.vCss.append("   width: 100%;\n")
        self.vCss.append("   text-align: left;\n")
        self.vCss.append("   border-collapse: collapse;\n")
        self.vCss.append(" }\n")
        self.vCss.append(" #hor-zebra th\n")
        self.vCss.append(" {\n")
        self.vCss.append("   font-size: 14px;\n")
        self.vCss.append("   font-weight: normal;\n")
        self.vCss.append("   padding: 10px 8px;\n")
        self.vCss.append("   color: #039;\n")
        self.vCss.append("   border-bottom: 2px solid #6678b1;\n")
        self.vCss.append("   border-right: 1px solid #6678b1; \n")
        self.vCss.append("	border-left: 1px solid #6678b1;\n")
        self.vCss.append(" }\n")
        self.vCss.append(" #hor-zebra td\n")
        self.vCss.append(" {\n")
        self.vCss.append("   padding: 8px;\n")
        self.vCss.append("   color: #669;\n")
        self.vCss.append("   border-right: 1px solid #6678b1; \n")
        self.vCss.append("	border-left: 1px solid #6678b1;\n")
        self.vCss.append(" }\n")
        self.vCss.append(" #hor-zebra .odd\n")
        self.vCss.append(" {\n")
        self.vCss.append("   background: #e8edff;\n")
        self.vCss.append("   border-right: 1px solid #6678b1; \n")
        self.vCss.append("	border-left: 1px solid #6678b1;\n")
        self.vCss.append(" }\n")
        #GREEN TABLE
        self.vCss.append(" #green \n")
        self.vCss.append(" {\n")
        self.vCss.append("   font-family: \"Sans-Serif\";\n")
        self.vCss.append("   font-size: 12px;\n")
        self.vCss.append("   margin: 0px;\n")
        self.vCss.append("   width: 100%;\n")
        self.vCss.append("   text-align: left;\n")
        self.vCss.append("   border-collapse: collapse;\n")
        self.vCss.append(" }\n")
        self.vCss.append(" #green th\n")
        self.vCss.append(" {\n")
        self.vCss.append("   font-size: 14px;\n")
        self.vCss.append("   font-weight: normal;\n")
        self.vCss.append("   padding: 10px 8px;\n")
        self.vCss.append("   color: #2b9900;\n")
        self.vCss.append("   border-bottom: 2px solid #66b16f;\n")
        self.vCss.append("   border-right: 1px solid #66b16f; \n")
        self.vCss.append("	border-left: 1px solid #66b16f;\n")
        self.vCss.append(" }\n")
        self.vCss.append(" #green td\n")
        self.vCss.append(" {\n")
        self.vCss.append("   padding: 8px;\n")
        self.vCss.append("   color: #578055;\n")
        self.vCss.append("   border-right: 1px solid #66b16f; \n")
        self.vCss.append("	border-left: 1px solid #66b16f;\n")
        self.vCss.append(" }\n")
        self.vCss.append(" #green .odd\n")
        self.vCss.append(" {\n")
        self.vCss.append("   background: #eaffe8;\n")
        self.vCss.append("   border-right: 1px solid #66b16f; \n")
        self.vCss.append("	border-left: 1px solid #66b16f;\n")
        self.vCss.append(" }\n")
        #LINKS
        self.vCss.append("a.link:link {font-family: \"Sans-Serif\";font-size: 14px;color: #039;text-decoration:none;}")
        self.vCss.append("a.link:visited {font-family: \"Sans-Serif\";font-size: 14px;color: #039;text-decoration:none;}")
        self.vCss.append("a.link:hover {font-family: \"Sans-Serif\";font-size: 14px;color: #039;text-decoration:underline;}")
        #P BLUE
        self.vCss.append(" #descriptionBlue \n")
        self.vCss.append(" {\n")
        self.vCss.append("   font-family: \"Sans-Serif\";\n")
        self.vCss.append("   font-size: 14px;\n")
        self.vCss.append("   text-align: left;\n")
        self.vCss.append("   color: #039;\n")
        self.vCss.append("   border-collapse: collapse;\n")
        self.vCss.append(" }\n")
        #P GREEN
        self.vCss.append(" #descriptionGreen \n")
        self.vCss.append(" {\n")
        self.vCss.append("   font-family: \"Sans-Serif\";\n")
        self.vCss.append("   font-size: 14px;\n")
        self.vCss.append("   text-align: left;\n")
        self.vCss.append("   color: #009900;\n")
        self.vCss.append("   border-collapse: collapse;\n")
        self.vCss.append(" }\n")
        #P SUBTITLE BLUE
        self.vCss.append(" #subtitleBlue \n")
        self.vCss.append(" {\n")
        self.vCss.append("   font-family: \"Sans-Serif\";\n")
        self.vCss.append("   font-size: 16px;\n")
        self.vCss.append("   font-weight: bold;\n")
        self.vCss.append("   text-decoration:underline;\n")
        self.vCss.append("   text-align: left;\n")
        self.vCss.append("   color: #039;\n")
        self.vCss.append("   border-collapse: collapse;\n")
        self.vCss.append(" }\n")
        #P SUBTITLE GREEN
        self.vCss.append(" #subtitleGreen \n")
        self.vCss.append(" {\n")
        self.vCss.append("   font-family: \"Sans-Serif\";\n")
        self.vCss.append("   font-size: 16px;\n")
        self.vCss.append("   font-weight: bold;\n")
        self.vCss.append("   text-decoration:underline;\n")
        self.vCss.append("   text-align: left;\n")
        self.vCss.append("   color: #009900;\n")
        self.vCss.append("   border-collapse: collapse;\n")
        self.vCss.append(" }\n")


    def buildHtml(self):
        ''' Add HTML Report Header to a given vector'''
        self.vHTML.append("<HTML>\n")

        self.vHTML.append(" <HEAD>\n")
        self.vHTML.append(" <STYLE TYPE=\"text/css\">\n")

        self.vHTML.append("  <!--\n")
        self.vHTML.append("   @import url(\"style.css\"); \n")
        self.vHTML.append("  -->\n")

        self.vHTML.append(" </STYLE>\n")
        self.vHTML.append(" </HEAD>\n")

        self.vHTML.append(" <BODY>\n")

        self.vHTML.append("  <H1 id=\"title\"> <U> WEB HUB TABLE </U> </H1>\n")

        self.vHTML.append("  <TABLE id=\"hor-zebra\">\n")
        self.vHTML.append("   <TR>\n")
	self.vHTML.append("    <TH scope=\"col\"> WEB LINKS </TH>\n")
	self.vHTML.append("   </TR>\n")

        #Loop over dictionary <title,html> 
        isOdd = False
        for entry in sorted(self.webToPrint):
            '''Add Entries'''
            if isOdd == True: 
                self.vHTML.append("   <TR class=\"odd\">\n")
            else:
                self.vHTML.append("   <TR>\n")
	
            self.vHTML.append("     <TD> <a class=link target=\"_blank\" href=\"" + self.webToPrint[entry]["web_location"] + "\">" + self.webToPrint[entry]["title"]  + "</a> </TD> \n")
	    self.vHTML.append("   </TR>\n")
            isOdd = not isOdd

        #Close Table and HTML
        self.vHTML.append("  </TABLE>\n")
        self.vHTML.append("\n")
        self.vHTML.append(" </BODY>\n")
        self.vHTML.append("</HTML>\n")

    def saveHtmlCss(self):
        '''Save HTML and CSS files
        file_name: File path to store the document
        '''
        dirOut = os.path.dirname(self.fileHtml)
        file_css = dirOut + "./style.css"
        
        with open(self.fileHtml, 'w') as fileDocument:
            for line in self.vHTML:
                fileDocument.write(line)

        with open(file_css, 'w') as fileDocument:
            for line in self.vCss:
                fileDocument.write(line)

        
    

