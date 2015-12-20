import urllib2
baseurl = "http://learnvimscriptthehardway.onefloweroneworld.com/chapters/{:0>2}.html"
for i in range(0, 57):
    url = baseurl.format(i)
    html = urllib2.urlopen(url).read()
    f = open("tmp/" + str(i) + ".markdown", "w")
    f.write(html)
