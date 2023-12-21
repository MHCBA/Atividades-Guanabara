import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except:
    print('DEU RUIM')
else:
    print('TUDO OK')
    print(site.read())
finally:
    print('volte sempre')