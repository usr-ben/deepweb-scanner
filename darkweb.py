import urllib2
import mechanize
import webbrowser
import re

def Space(j):
    i = 0
    while i<=j:
        print(" "),
        i+=1
def Credit():
    Space(9); print("#####################################")
    Space(9); print("#    +[DEEP WEB URL SCANNER]+       #")
    Space(9); print("#     Scripted by CYBA TIGER        #")
    Space(9); print("#         GHOSTFLEET.ORG            #")
    Space(9); print("#####################################")

Credit()
print "\nENTER THE SITE TO SCAN\n"
site=raw_input("ex:(safedeepweb.onion) $:> ")
site=site+".to"
url="http://scanurl.net/?u="+site+"&uesb=Check+This+URL#results"
br=mechanize.Browser()
br.set_handle_robots(False)
br.addheaders=[{'User-agent','chrome'}]

raw=br.open(url).read()
safe=re.search("unsafe",str(raw))
if not safe:
    print " The url is SAFE to open " 
    print " The author will not be responsible for any thing "
    a=raw_input("press c to continue or q to quit $:> ")
    if a== "q":
        print "Thanx for using the service"
    else:
        e="http://"+site
        webbrowser.open(e)
