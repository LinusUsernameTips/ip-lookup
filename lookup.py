import requests
import colorama
from colorama import Fore
import json
import os
os.system('clear')
iptolook = input(Fore.BLUE + "Enter IP to lookup : ")
data = {'action': 'get_user_info_data',
        'ip': iptolook}
r = requests.get(f'https://nordvpn.com/wp-admin/admin-ajax.php?action=get_user_info_data&ip={iptolook}', data=data)
ipinf = json.loads(r.text)
print(Fore.BLUE +f'                      ↓ INFO ON {iptolook} ↓\n')
print(Fore.LIGHTMAGENTA_EX +'                        ISP:', ipinf['isp'])
print(Fore.LIGHTMAGENTA_EX +'                        COUNTRY:', ipinf['country'])
print(Fore.LIGHTMAGENTA_EX +'                        REGION:', ipinf['region'])
print(Fore.LIGHTMAGENTA_EX +'                        CITY:', ipinf['city'] )
print(Fore.LIGHTMAGENTA_EX +'                        AREA CODE:', ipinf['area_code'])
input("")
