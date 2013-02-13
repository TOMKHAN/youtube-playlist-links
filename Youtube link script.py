import urllib2
import xml.etree.ElementTree as et
import re
import os

more = 1
id_playlist = raw_input("Enter youtube playlist id: ")
number_of_iteration  = input("How much video links: ")
number = number_of_iteration / 50
number2 = number_of_iteration % 50
if (number2 != 0):
     number3 = number + 1
else:
     number3 = number
start_index = 1

while more <= number3:
     #reading youtube playlist page
     if (more != 1):
          start_index+=50
          
     str_start_index = str(start_index)
     req = urllib2.Request('http://gdata.youtube.com/feeds/api/playlists/'+ id_playlist + '?v=2&&start-index=' + str_start_index + '&max-results=50')
     response = urllib2.urlopen(req)
     the_page = response.read()

     #writing page in .xml
     dat = open("web_content.xml","w")
     dat.write(the_page)
     dat.close()

     #searching page for links
     tree = et.parse('web_content.xml')
     all_links = tree.findall('*/{http://www.w3.org/2005/Atom}link[@rel="alternate"]')

     #writing links + attributes to .txt
     if (more == 1):
          till_links = 50
     else:
          till_links = start_index + 50
          
     str_till_links = str(till_links)
     dat2 = open ("links-"+ str_start_index +"to"+ str_till_links +".txt","w")
     for links in all_links:
          str1 = (str(links.attrib) + "\n")
          dat2.write(str1)     
     dat2.close()

     #getting only links
     f = open ("links-"+ str_start_index +"to"+ str_till_links +".txt","r")
     link_all = f.read()
     new_string = link_all.replace("{'href': '","")
     new_string2 = new_string.replace("', 'type': 'text/html', 'rel': 'alternate'}","")
     f.close()

     #writing links to .txt
     f = open ("links-"+ str_start_index +"to"+ str_till_links +".txt","w")
     f.write(new_string2)
     f.close()
     
     more+=1
     
os.remove('web_content.xml')
print "Finished!"
          
