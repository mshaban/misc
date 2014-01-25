
import urllib2
from bs4 import BeautifulSoup
page = urllib2.urlopen("http://met.guc.edu.eg/Courses/Material.aspx?crsEdId=431")
soup = BeautifulSoup(page.read())

f = open("bla.txt", "w")
links = soup.findAll("a")
for link in links:
    f.write(str(link)+"\n")
f.close()