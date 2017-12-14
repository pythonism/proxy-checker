from colorama import Fore
import requests
import urllib3

class checker(object):

    def check(self,filename):
        url='http://google.com'
        try:
            liner=filename.split('\n',1)[0]
            requests.get(url,proxies={'http':'http://'+liner},timeout=(3.05,27))
        except requests.exceptions.ConnectionError as e:
            print(Fore.RED+'Error',e)
            return e
        except requests.exceptions.ConnectTimeout as e:
            print(Fore.RED+'ERROR! Connection timeout',e)
            return e
        except requests.exceptions.HTTPError as e:
            print(Fore.RED+'Error code',e.code)
            return e.code
        except requests.exceptions.Timeout as e:
            print(Fore.RED+'Error! Connection Timeout!',e)
            return e
        except urllib3.exceptions.ProxySchemeUnknown as e:
            print(Fore.RED+'ERROR',e)
            return e
