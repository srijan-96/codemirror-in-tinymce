# Author : Ashutosh Sathe
# Parses the html to remove/add some part of the htmlContent received 
# from the tinymce

def convertHTML(htmlContent):
    ret = htmlContent.encode('ascii', 'ignore')
    ret.replace("\\n", "\n")
    return ret