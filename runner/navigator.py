import sys
from datetime import datetime
import requests
import re
import urllib.parse
from urllib3.exceptions import InsecureRequestWarning
from utils import colors


color = colors.Colors()
animation = color.animation
reset = color.reset
yellow = color.yellow
white = color.white
red = color.red
dark_grey = color.dark_grey
light_grey = color.light_grey
blue = color.blue
bold = color.bold
green = color.green
magenta = color.magenta
purple = color.purple
pink = color.pink
cyan = color.cyan

class Navigator:

    def __init__(self):
        self.url = ''
        self.typeResponse = ''
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        self.sessionRequest = requests.Session()
        self.sessionRequest.verify = False
        self.header = {'accept-language': 'en-GB,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,en-US;q=0.6',
                                'cache-control': 'no-cache',
                                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36)'}

    def downloadResponse(self, url, typeResponse, method, header=False):
        if header:
            self.sessionRequest.headers.update(header)

        if typeResponse == 'JSON':

            try:
                return self.sessionRequest.get(url).json()
            except:
                return self.sessionRequest.get(url)

        elif typeResponse == 'HTML':

            return self.sessionRequest.get(url).text

        elif typeResponse == 'HEAD':

            return self.sessionRequest.head(url).text

        elif typeResponse == 'TITLE':
            try:
                res = self.sessionRequest.get(url, timeout=10).text
                return re.search('(?<=<title>).+?(?=</title>)', res, re.DOTALL).group().strip()
            except:
                return ''
        else:
            return self.sessionRequest.get(url, timeout=5)  # status_code


    def filterUrl(self, url):
        urlClean = url
        if url == None:
            return url
        if "*." in url:
            urlClean = url.replace('*.', '')
        if '\\n' in url:
            urlClean = url.replace('\\n', '')
        return urlClean

    def Hostname(self, url):
        parsed = urllib.parse.urlsplit(url)
        return parsed.hostname

    def ModuleLoaded(self, Module, DOMAINS_LIST):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        sys.stdout.flush()


        if Module == 'wayback':
            sys.stdout.writelines(
            '\r[' + magenta + current_time + reset + '] ['+blue + " " + '🔎' + reset + ']:' + cyan + " " + Module + pink + " " + str(
                len(DOMAINS_LIST)) +  reset + " assets founded! ✅                                             \n")
            sys.stdout.flush()
        else:
            sys.stdout.writelines(
                '\r[' + magenta + current_time + reset + '] ['+blue + " " + '🔎' + reset + ']:' + cyan + " " + Module + pink + " " + str(
                    len(DOMAINS_LIST)) +  reset + " domains founded! ✅                                             \n")
            sys.stdout.flush()

