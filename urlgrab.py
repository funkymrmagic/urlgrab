#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup
import socket
 
html = urllib2.urlopen("http://www.ephotozine.co.uk")
soup = BeautifulSoup(html)
file1 = open("urls.txt", "w")
file2 = open("urls.txt", "r")
urllist = []
 
for link in soup.find_all('a') :
        file1.write(link.get('href')+"\n")
file1.close()
 
for line in file2.readlines() :
        line1 = line.strip()
        if len(line1.split('/')) >= 2 :
                chop = line1.split('/')[2]
                urllist.append(chop)
 
urllist = list(set(urllist))
for url in urllist:
        address = socket.gethostbyname(url)
        print "%s has address %s" % (url, address)
