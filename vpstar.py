'''
    VrahProxyStar - utility for checking proxy in terminal under the GNU GPL V3.0 Licensy
    AUTHORS: G0rillaz
    Version: 0.1
'''

from sys import argv
import urllib3
from os import system as terminal
import requests
from colorama import Fore,Style

URL = "http://google.com"
CMD_CLEAR_TERM = "clear"
TIMEOUT = (3.06, 28)

def check_proxy(proxy):
    '''
        Funktion zum Proxy checken return ERROR wenn der Proxy schlecht ist ansonsten None
        TODO:: online Blacklist checker
    '''
    try:
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        session.max_redirects = 300
        proxy = proxy.split('\n',1)[0]
        print(Fore.LIGHTYELLOW_EX + 'Prüfe ' + proxy)
        session.get(URL, proxies={'http':'http://' + proxy}, timeout=TIMEOUT,allow_redirects=True)
    except requests.exceptions.ConnectionError as error:
        print(Fore.LIGHTRED_EX + 'Error!')
        return error
    except requests.exceptions.ConnectTimeout as error:
        print(Fore.LIGHTRED_EX + 'Error,Timeout!')
        return error
    except requests.exceptions.HTTPError as error:
        print(Fore.LIGHTRED_EX + 'HTTP ERROR!')
        return error
    except requests.exceptions.Timeout as error:
        print(Fore.LIGHTRED_EX + 'Error! Connection Timeout!')
        return error
    except urllib3.exceptions.ProxySchemeUnknown as error:
        print(Fore.LIGHTRED_EX + 'ERROR unkown Proxy Scheme!')
        return error
    except requests.exceptions.TooManyRedirects as error:
        print(Fore.LIGHTRED_EX + 'ERROR! Too many redirects!')
        return error
    
def print_help():
    terminal(CMD_CLEAR_TERM)
    print(Fore.LIGHTGREEN_EX + 'VrahProxyStar v0.1 - Tool zum überprüfen von Proxys im Terminal')
    print(Fore.LIGHTGREEN_EX + 'Author: G0rillaz')
    print(Fore.LIGHTCYAN_EX)
    print('Usage -> vpstar -f <filename> - check eine Datein mit Proxys')
    print('vpstar -p <proxy> - check nur ein Proxy')
    print('vpstar --help - zeige dieses Menü')

if len(argv) > 1:
    commands = ['--help','-h','-f','-p','/?','--file','-file','--proxy','-proxy']
    if argv[1] in commands:
        if argv[1] in ('--help','-help','/?','--?'):
            print_help()
        elif argv[1] in ('-f','--file','-file'):
            try:
                file = open(argv[2])
                proxies = list(file)
                goods = 0
                terminal(CMD_CLEAR_TERM)
                print(Fore.LIGHTCYAN_EX + '===========================================')
                for proxy in proxies:
                    try:
                        if check_proxy(proxy):
                            print(Fore.LIGHTRED_EX + 'schlechter Proxy ' + proxy)
                        else:
                            print(Fore.LIGHTGREEN_EX + 'gute Proxy ' + proxy)
                            file_with_goods = open('good.txt','a')
                            file_with_goods.write(proxy)
                            goods += 1
                        print(Fore.LIGHTCYAN_EX + '=================================================')
                    except KeyboardInterrupt:
                        print(Fore.LIGHTGREEN_EX + '\nExit.')
                        exit()
                print(Fore.LIGHTGREEN_EX + 'Total ' + str(goods) + ' good proxies found')
                print(Fore.LIGHTRED_EX + 'And ' + str(len(proxies) - goods) + ' is bad')
                print(Fore.LIGHTYELLOW_EX + 'Have nice day! :)')
                print()
            except FileNotFoundError:
                print(Fore.LIGHTRED_EX + 'Error!\nFile Not found!')
            except IndexError:
                print(Fore.LIGHTRED_EX + 'Error!\nMissing filename!')
        elif argv[1] in ('-p','--proxy','-proxy'):
            try:
                argv[2] = argv[2].split(' ')[0]
                if check_proxy(argv[2]):
                    print(Fore.LIGHTRED_EX + 'BAD PROXY ' + argv[2])
                else:
                    print(Fore.LIGHTGREEN_EX + 'GOOD PROXY ' + argv[2])
            except IndexError:
                print(Fore.LIGHTRED_EX + 'Error! Missing proxy!')
    else:
        print(Fore.LIGHTRED_EX + 'Unknown option \"' + argv[1] + '\"')
else:
    print_help()
