#!/usr/bin/env python3
# File name          : proton.py
# Author             : @carlostkd - @sophie -@7L3E1T
# Updated 08/04/2022
from bs4 import BeautifulSoup
import re
import requests
import ipaddress
import datetime
from datetime import datetime
from googlesearch import search
import webbrowser
import json
import readline


def printprotonbanner():
    """
    proton banner
    """
    print("""\u001b[32m\033[1m
 ███████████                      █████                                
░░███░░░░░███                    ░░███                                 
 ░███    ░███ ████████   ██████  ███████    ██████  ████████           
 ░██████████ ░░███░░███ ███░░███░░░███░    ███░░███░░███░░███          
 ░███░░░░░░   ░███ ░░░ ░███ ░███  ░███    ░███ ░███ ░███ ░███          
 ░███         ░███     ░███ ░███  ░███ ███░███ ░███ ░███ ░███          
 █████        █████    ░░██████   ░░█████ ░░██████  ████ █████         
░░░░░        ░░░░░      ░░░░░░     ░░░░░   ░░░░░░  ░░░░ ░░░░░          
                                                                       
                                                                       
                                                                       
 ███████████             ███                                           
░░███░░░░░███           ░░░                                            
 ░███    ░███ ████████  ████  █████ █████  ██████    ██████  █████ ████
 ░██████████ ░░███░░███░░███ ░░███ ░░███  ░░░░░███  ███░░███░░███ ░███ 
 ░███░░░░░░   ░███ ░░░  ░███  ░███  ░███   ███████ ░███ ░░░  ░███ ░███ 
 ░███         ░███      ░███  ░░███ ███   ███░░███ ░███  ███ ░███ ░███ 
 █████        █████     █████  ░░█████   ░░████████░░██████  ░░███████ 
░░░░░        ░░░░░     ░░░░░    ░░░░░     ░░░░░░░░  ░░░░░░    ░░░░░███ 
                                                              ███ ░███ 
                                                             ░░██████  
                                                              ░░░░░░   
 ██████████                                  █████              █████  
░░███░░░░███                                ░░███              ░░███   
 ░███   ░░███  ██████   ██████   ██████   ███████   ██████   ███████   
 ░███    ░███ ███░░███ ███░░███ ███░░███ ███░░███  ███░░███ ███░░███   
 ░███    ░███░███████ ░███ ░░░ ░███ ░███░███ ░███ ░███████ ░███ ░███   
 ░███    ███ ░███░░░  ░███  ███░███ ░███░███ ░███ ░███░░░  ░███ ░███   
 ██████████  ░░██████ ░░██████ ░░██████ ░░████████░░██████ ░░████████  
░░░░░░░░░░    ░░░░░░   ░░░░░░   ░░░░░░   ░░░░░░░░  ░░░░░░   ░░░░░░░░   
- Proton Privacy Decoded can be used to:
- Check for ProtonMail accounts and creation date
- Check User PGP Key, creation date and Key Type
- Download PGP Keys 
- Check if the IP address is from ProtonVPN and from which Country
- ProtonMail User Footprints DEEP  and Dark Web
                          READY?
                          
                    ---  Lets Start ---                                                                       
___________________________________________________________________ \033[0m\n""")




def checkprotonapistatus():
    """
    Proton API Online Check
    """
    requestprotonmailstatus = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=admin@protonmail.com')
    if requestprotonmailstatus.status_code == 200:
        print(
            "\U0001F4AC ProtonMail API is ONLINE \U0001F7E2")
    else:
        print(
            "\U0001F4AC Protonmail API seems like is OFFLINE try again later \U0001F534   ")



def printprotonintro():
    protonintro = """
\u001b[31m\U0001F575\033[1m  Privacy Decoded Options: \n
\u001b[32m\U0001F50D \033[1mEMAIL\033[0m\u001b[32m: Type email to check if a ProtonMail account exists
\u001b[32m\U0001F4E1 \033[1mTRACE\033[0m\u001b[32m: Type trace to run a search on Deep WEB
\u001b[32m\U0001F3F4 \033[1mWEB\033[0m\u001b[32m: Type web to run a Dark Web search of the Proton Email
\u001b[32m\U0001F511 \033[1mKEYS\033[0m\u001b[32m: Type keys to get ProtonMail user PGP Key and Key date
\u001b[32m\U0001F4BB \033[1mVPN\033[0m\u001b[32m: Type vpn to verify if an IP address is from ProtonVPN
"""
    print(protonintro)



def protonmailaccountcheck():
    """
    EMAIL : Check if ProtonMail account exists
    """
    invalidEmail = True
    regexEmail = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    print(
        " \U0001F4AC Check if ProtonMail account exists: ")
    while invalidEmail:

        mail = input("\U0001F4AC Enter the target Email: ")

        if (re.search(regexEmail, mail)):
            invalidEmail = False
        else:
            print("\U0001F4AC ProtonMail user does not exist \U0001F534 ")
            invalidEmail = True
    requestProton = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=' + str(mail))
    bodyResponse = requestProton.text

    protonmailaccountdoesnotexist = "info:1:0"
    protonmailaccountexists = "info:1:1"
    if protonmailaccountdoesnotexist in bodyResponse:
        print("\U0001F4AC ProtonMail account is NOT VALID. \U0001F534")

    if protonmailaccountexists in bodyResponse:
        print("\U0001F4AC ProtonMail Account is VALID. \U0001F7E2 ")



def emailtraces():
    """
    TRACE : Check Email Traces on DEEP WEB
    """
    print("\U0001F4AC Checking server status please wait... ")
    response = requests.get('https://google.com')
    print(response)
    if response.status_code == 200:
        print('[+][+] Status: Success!\n')
    elif response.status_code == 404:
        print('Not Found.')

    searchfor = input(
        """\U0001F4AC Enter Target Email (Example:"root@protonmail.com") """)
    print("\n\U0001F4AC Processing request please wait... ")
    for result in search(searchfor, tld="com", num=200, stop=200, pause=2):
        print(result)



def darkwebtraces():
    """
    WEB : Dark Web Email Traces
    """
    print("\U0001F4AC Checking server status please wait... ")
    response = requests.get('https://ahmia.fi')
    print(response)
    if response.status_code == 200:
        print('[+][+] Status: Success!\n')

    elif response.status_code == 404:
        print('Not Found.')

    choice = input(
        """\U0001F4AC View results in Browser ("B") or Terminal ("T")? """)

    if choice == "B":
        darkwebbrowser()

    if choice == "T":
        darkwebterminal()



def darkwebbrowser():
    """
    Dark Web Browser Open
    """
    query = input("""\U0001F4AC Input Target email or any query to search the DARK WEB: """)
    webbrowser.open("https://ahmia.fi/search/?q=%s" % query)




def darkwebterminal():
    """
    Dark Web Terminal
    """
    query = input("\U0001F4AC Input target email: ")
    URL = ("https://ahmia.fi/search/?q=%s" % query)
    page = requests.get(URL)
    request = requests.get(URL)

    if request.status_code == 200:
        print("\n\nRequest went through\n")

    soup = BeautifulSoup(page.content, "html.parser")
    for a_href in soup.find_all("a", href=True):
        print(a_href["href"])





def pgpkeyinformation():
    """
   KEYS: Get the ProtonMail user PGP Key and info
   """
    choice = input(
        """\U0001F4AC View PGP Key in Terminal ("T") or Download Key("D")? """)

    if choice == "T":
        pgpkeyview()

    if choice == "D":
        pgpkeydirectdownload()


def pgpkeydirectdownload():
    """
    Download PGP Key
    """
    query = input(
        """\n\U0001F4ACInput Target email to Download PGP Key: """)
    webbrowser.open("https://api.protonmail.ch/pks/lookup?op=get&search=" + query)


def pgpkeyview():
    """
    View PGP Key in Terminal
    """
    invalidEmail = True
    regexEmail = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    print(
        "\U0001F4AC Input the ProtonMail target email to get the PGP Key ")
    while invalidEmail:

        mail = input("\U0001F4AC ProtonMail Email: ")

        if (re.search(regexEmail, mail)):
            invalidEmail = False
        else:
            print("\U0001F4AC ProtonMail user does not exist\u001b[32m\U0001F534")
            invalidEmail = True
    requestProton = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=' + str(mail))
    bodyResponse = requestProton.text

    protonmailaccountdoesnotexist = "info:1:0"
    protonmailaccountexists = "info:1:1"
    if protonmailaccountdoesnotexist in bodyResponse:
        print("\U0001F4AC ProtonMail account is NOT VALID \U0001F534")

    if protonmailaccountexists in bodyResponse:
        print("\U0001F4AC ProtonMail Account PGP Key Found. \U0001F7E2")

        regexPattern1 = "2048:(.*)::"  # RSA 2048-bit (Older but faster)
        regexPattern2 = "4096:(.*)::"  # RSA 4096-bit (Secure but slow)
        regexPattern3 = "22::(.*)::"  # X25519 (Modern, fastest, secure)
        try:
            timestamp = int(re.search(regexPattern1, bodyResponse).group(1))
            dtObject = datetime.fromtimestamp(timestamp)
            print("\nPGP Key Date and Creation Time:", dtObject)
            print("Encryption Standard : RSA 2048-bit")
        except:
            try:
                timestamp = int(re.search(regexPattern2, bodyResponse).group(1))
                dtObject = datetime.fromtimestamp(timestamp)
                print("PGP Key Date and Creation Time:", dtObject)
                print("Encryption Standard : RSA 4096-bit ")
            except:
                timestamp = int(re.search(regexPattern3, bodyResponse).group(1))
                dtObject = datetime.fromtimestamp(timestamp)
                print("PGP Key Date and Creation Time:", dtObject)
                print("Encryption Standard : ECC Curve25519 ")


        invalidResponse = True
        print("\U0001F4AC Get User PGP Key?  ")
        while invalidResponse:

            responseFromUser = input("""\033[1m "\033[1mY"/"N":\033[0m """)

            if responseFromUser == "Y":
                invalidResponse = False
                requestProtonPublicKey = requests.get('https://api.protonmail.ch/pks/lookup?op=get&search=' + str(mail))
                bodyResponsePublicKey = requestProtonPublicKey.text
                print(bodyResponsePublicKey)
            elif responseFromUser == "N":
                invalidResponse = False
            else:
                print("Input Not Valid")
                invalidResponse = True
def protonvpnipsearch():
    """
   VPN : Find  if the IP address is from ProtonVPN
   """
    while True:
        try:
            ip = ipaddress.ip_address(input(
                '\U0001F4AC Enter Target IP address:  '))
            break
        except ValueError:
            continue
    requestProton_vpn = requests.get('https://api.protonmail.ch/vpn/logicals')
    bodyResponse = requestProton_vpn.text
    def get_location():
        ip_address = get_ip()
        enter = ip
        response = requests.get(f'https://ipapi.co/{enter}/json/').json()
        location_data = {
            "\U0001F4AC ip": ip_address,
            "\U0001F4AC city": response.get("city"),
            "\U0001F4AC region": response.get("region"),
            "\U0001F4AC country": response.get("country_name"),
            "\U0001F4AC in_eu": response.get("in_eu"),
            "\U0001F4AC asn": response.get("asn"),
        }
        return location_data



    if str(ip) in bodyResponse:
        print(
            "\U0001F4AC This IP is from a ProtonVPN. \U0001F7E2 ")
        print(get_location())
    else:
        print(
            "\U0001F4AC This IP address is not from ProtonVPN. \U0001F534 ")

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]








def main():
    printprotonbanner()
    choice = input(
        """\U0001F4AC Type "c" to check API Status first or "go" to start anyway: """)
    if choice == "c":
        checkprotonapistatus()
        if choice == "go":
            printprotonintro()
    choice = input("""\U0001F4AC View Options and Continue? / "Y" or "N":\033[0m\u001b[32m """)
    if choice == "Y":
        printprotonintro()
    elif choice == "N":
        print("\U0001F4AC Take Care Bye Bye")
        exit()

    while True:
        choice = input(
            """\U0001F4AC Select a Option: (Example:"E for email"): [E] EMAIL | [T] TRACE | [W] WEB | [K] - KEYS | [V] - VPN : \033[0m\u001b[32m""")
        if choice == "E":
            protonmailaccountcheck()
        if choice == "T":
            emailtraces()
        if choice == "W":
            darkwebtraces()
        if choice == "K":
            pgpkeyinformation()
        if choice == "V":
            protonvpnipsearch()

        inp = input("\U0001F4AC Continue Y/N: ")
        if inp.lower() == 'n':
            print("\U0001F4AC Take Care Bye Bye")
            break
if __name__ == '__main__':
    main()
