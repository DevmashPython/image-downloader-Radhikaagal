import urllib2
import re




response = urllib2.urlopen("https://en.wikipedia.org/wiki/Harry_Styles")
page_source = response.read()

pattern=('<img [^>]*src="([^"]*)"[^>]*>')
pattern=re.compile(pattern)
a= re.findall(pattern,page_source)

l=open("imageproject","w")
for i in a:
	l.write(i +'\n')
l.close