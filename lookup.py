# Author: Pari Malam

import argparse
import requests
import sys
from sys import stdout
from colorama import Fore, Style

def banners():
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI PARI-MALAM                               "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   HTTPS://GITHUB.COM/PARI-MALAM                 "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL FORUM     "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   HTTPS://DRAGONFORCE.IO                        "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL TELEGRAM  "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   HTTPS://TELEGRAM.ME/DRAGONFORCEIO             "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{Fore.YELLOW}[HackerTarget] - {Fore.GREEN}Perform With DNS Emuration & Reverse Lookup\n")
banners()

parser = argparse.ArgumentParser(description='Perform a DNS & ReverseIP lookup on a domain using the Hackertarget')
parser.add_argument('-D', '--domain', help='The domain name to lookup', required=True)
parser.add_argument('-R', '--reverse', action='store_true', help='')
parser.add_argument('-O', '--output', help='The output file name', default=None)
args = parser.parse_args()



if args.output is not None:
    f = open(args.output, 'w')
    sys.stdout = f

try:
    if args.subdomains:
        check_url = f'https://api.hackertarget.com/reverseiplookup/?q={args.domain}'
    else:
        check_url = f'https://api.hackertarget.com/dnslookup/?q={args.domain}'
    r = requests.get(check_url)
    r.raise_for_status()

    result_lines = r.text.split('\n')
    for line in result_lines:
        if line.startswith('#'):
            print(Fore.LIGHTBLACK_EX + line + Style.RESET_ALL)
        elif not line:
            continue
        else:
            parts = line.split()
            if len(parts) == 4:
                text = ' '.join(parts[1:])
                if parts[3] == 'CNAME':
                    print(Fore.GREEN + f'{parts[0]} {parts[3]} -> {text}' + Style.RESET_ALL)
                elif parts[3] == 'MX':
                    print(Fore.YELLOW + f'{parts[0]} {parts[3]} -> {text}' + Style.RESET_ALL)
                else:
                    print(Fore.WHITE + f'{parts[0]} {parts[3]} -> {text}' + Style.RESET_ALL)
            else:
                print(Fore.WHITE + line + Style.RESET_ALL)

except requests.exceptions.RequestException as e:
    print(Fore.RED + f'Error: {e}' + Style.RESET_ALL)

except IndexError:
    print(Fore.RED + f'Error: No data returned for domain {args.domain}' + Style.RESET_ALL)

if args.output is not None:
    f.close()
    sys.stdout = sys.__stdout__
    print(f'Results saved to {args.output}')
