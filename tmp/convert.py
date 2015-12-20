import os
for i in range(0, 57):
    os.system("python /Users/tonghu/source/html2text/html2text.py " + str(i) + ".html > " + str(i) + ".markdown")
