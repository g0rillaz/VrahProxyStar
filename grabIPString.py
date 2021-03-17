
import requests
from bs4 import BeautifulSoup
import os
from colorama import Fore,Style
import subprocess
import re

def grabStringFromHtmlObject(site="https://sslproxies.org/"):
    response = requests.get(site)
    soup = BeautifulSoup(response.content, 'html5lib')
    iPString = list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8])))
    for i in iPString:
        #print("{0}:{1}".format(i[0],i[1]))
        test = subprocess.Popen(["ping","-W","2","-c", "1", "192.168.188.12"], stdout=subprocess.PIPE)
        output = test.communicate()[0]
        

def grabRegExpressonHtmlObject(site="85.173.165.36:46330"):
    response = requests.get(site)
    soup = BeautifulSoup(response.content, 'html5lib')
    soup = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
    test = soup.match()
    if test:
        print("Kompatible IP address")
    else:
        print("Unkompatible IP address")
    #os.system("python vpstar.py -p {0}:{1}".format(i[0],i[1]))
    ## check_proxy("{0}:{1}".format(i[0],i[1]))

def main():
    grabRegExpressonHtmlObject()

if __name__ == '__main__':
    main()