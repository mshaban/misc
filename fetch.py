
import urllib2
u = urllib2.urlopen('http://met.guc.edu.eg/Courses/Material.aspx?crsEdId=431')
localFile = open('file.html', 'w')
localFile.write(u.read())
localFile.close()