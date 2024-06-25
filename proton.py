#!/usr/bin/env python3
# File name          : proton.py
# Author             : @carlostkd - @sophie -@7L3E1T
# last update 25.06.24 


from bs4 import BeautifulSoup
import re
import requests
import ipaddress
import datetime
from datetime import datetime
from googlesearch import search
import webbrowser
import readline



print("- Proton Privacy Decoded can be used to:")
print("- Check for ProtonMail accounts existence & Creation date")
print("- Check User PGP Key, creation date, Key Type: RSA 4096 or ECC Curve25519")
print("- Download PGP Keys to send encrypted emails to another Proton users")
print("- Check if the IP address is a ProtonVPN ")
print("- ProtonMail User Digital Footprints (clear & Dark Web)\n\n")


# Proton  banner
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
                                                                       
                                                                       
                                                                       


                                                             
___________________________________________________________________ \033[0m\n""")


# Proton API Check/Verification
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
\u001b[31m\U0001F575\033[1m  Privacy Decoded METHOD: \n

\u001b[32m\U0001F50D \033[1mEMAIL\033[0m\u001b[32m: Type email to check if a ProtonMail account exists

\u001b[32m\U0001F4E1 \033[1mTRACE\033[0m\u001b[32m: Type trace to run a search on Deep WEb

\u001b[32m\U0001F3F4 \033[1mWEB\033[0m\u001b[32m: Type web to run a Dark Web search of the Proton Email

\u001b[32m\U0001F511 \033[1mKEYS\033[0m\u001b[32m: Type keys to get ProtonMail user PGP Key and Key creation date

\u001b[32m\U0001F4BB \033[1mVPN\033[0m\u001b[32m: Type vpn to verify if an IP address belongs to the ProtonVPN
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
    TRACE : Check Email Traces with Google Dork
    """

    print("\U0001F4AC Checking server status/ ")
    response = requests.get('https://google.com')
    print(response)
    if response.status_code == 200:
        print('[+] Status: Success!\n')
    elif response.status_code == 404:
        print('Not Found.')

    searchfor = input(
        """\U0001F4AC Enter Target Email (Example:"root@protonmail.com") """)
    print("\n\U0001F4AC Processing request please wait... ")
    for result in search(searchfor, tld="com", num=200, stop=200, pause=2):
        print(result)


# Run a DarkWeb search on the email address
def darkwebtraces():
    """
    WEB : Dark Web Email Traces
    """

    print("\U0001F4AC Checking server status ")
    response = requests.get('https://ahmia.fi')
    print(response)
    if response.status_code == 200:
        print('[+] Status: Success!\n')

    elif response.status_code == 404:
        print('Not Found.')

    choice = input(
        """\U0001F4AC View results in Browser ("B") or Terminal ("T")? """)

    if choice in  ["B", "b"]:
        darkwebbrowser()

    if choice in ["T", "t"]:
        darkwebterminal()


# Search with the Dark Web Browser opening automatically
def darkwebbrowser():
    """
    Dark Web Browser Open

    """
    query = input("""\U0001F4AC Input Target email or any query to search the Dark Web: """)
    webbrowser.open("https://ahmia.fi/search/?q=%s" % query)


# Search from Terminal with search results displayed within the terminal

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




# Get ProtonMail User PGP Key
def pgpkeyinformation():
    """
	KEYS: Get the ProtonMail user PGP Key and info

	"""
    choice = input(
        """\U0001F4AC View PGP Key in Terminal ("T") or Download Key("D")? """)

    if choice in ["T", "t"]:
        pgpkeyview()

    if choice in ["D", "d"]:
        pgpkeydirectdownload()


def pgpkeydirectdownload():
    """
    Download PGP Key

    """

    query = input(
        """\n\U0001F4ACInput Target email to Download PGP Key """)
    webbrowser.open("https://api.protonmail.ch/pks/lookup?op=get&search=" + query)


def pgpkeyview():
    """
    View PGP Key in Terminal

    """

    invalidEmail = True
    regexEmail = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    print(
        "\U0001F4AC Input the ProtonMail user email address to get the user PGP Key ")
    while invalidEmail:

        mail = input("\U0001F4AC ProtonMail Email: ")

        if (re.search(regexEmail, mail)):
            invalidEmail = False
        else:
            print("\U0001F4AC ProtonMail user does not exist\u001b[32m")
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

        # Get the USER PGP Key
        invalidResponse = True

        print("\U0001F4AC Get User PGP Key?  ")
        while invalidResponse:
            # Input
            responseFromUser = input("""\033[1m "\033[1mY"/"N":\033[0m """)
            # Text if the input is valid
            if responseFromUser in ["Y", "y"]:
                invalidResponse = False
                requestProtonPublicKey = requests.get('https://api.protonmail.ch/pks/lookup?op=get&search=' + str(mail))
                bodyResponsePublicKey = requestProtonPublicKey.text
                print(bodyResponsePublicKey)
            elif responseFromUser in ["N", "n"]:
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
    if str(ip) in bodyResponse:
        print(
            "\U0001F4AC This IP is from a ProtonVPN. \U0001F7E2 ")
    else:
        print(
            "\U0001F4AC This IP address is not from ProtonVPN. \U0001F534 ")


def main():
    printprotonbanner()
    choice = input(
        """\U0001F4AC Type "c" to check API Status first or "go" or "g" to start anyway: """)
    if choice in  ["c", "C"]:
        checkprotonapistatus()
        if choice in ["go", "GO", "g", "G"]:
            printprotonintro()
    choice = input("""\U0001F4AC View Modules? / "Y" or "N":\033[0m\u001b[32m """)
    if choice in ["Y", "y"]:
        printprotonintro()

    while True:
        choice = input(
            """\U0001F4AC Make your choice (Example:"E for email"): [E/e] EMAIL | [T/t] TRACE | [W/w] WEB | [K/k] - KEYS | [V/v] - VPN : \033[0m\u001b[32m""")
        if choice in ["E", "e"]:
            protonmailaccountcheck()
        if choice in ["T", "t"]:
            emailtraces()
        if choice in ["W", "w"]:
            darkwebtraces()
        if choice in ["K", "k"]:
            pgpkeyinformation()
        if choice in ["V", "v"]:
            protonvpnipsearch()

        inp = input("\U0001F4AC Continue Y/N: ")
        if inp in ["N", "n"]:
        #if inp.lower() == 'n':
            break



if __name__ == '__main__':
    main()
