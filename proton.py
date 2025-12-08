#!/usr/bin/env python3
import os
import re
import time
import json
import base64
import requests
import webbrowser
from bs4 import BeautifulSoup
from datetime import datetime

def print_proton_banner():
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
--------------------------------------------------------------------\033[0m""")

def print_proton_intro():
    intro = """
\u001b[31m\U0001F575\033[1m  Privacy Decoded METHOD: \n

\u001b[32m\U0001F50D \033[1mEMAIL\033[0m\u001b[32m: Type email to check if a ProtonMail account exists

\u001b[32m\U0001F4E1 \033[1mTRACE\033[0m\u001b[32m: Type trace to run a search on DuckDuckGo (fallback to Bing)

\u001b[32m\U0001F3F4 \033[1mWEB\033[0m\u001b[32m: Type web to run a Dark Web search of the Proton email

\u001b[32m\U0001F511 \033[1mKEYS\033[0m\u001b[32m: Type keys to get ProtonMail user PGP Key and Key creation date
"""
    print(intro)

DDG_ENDPOINT = "https://api.duckduckgo.com/"
BING_ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"
BING_KEY = os.getenv("BING_API_KEY")
PAUSE = 5

def _ddg_json(query, max_results=5):
    params = {"q": query, "format": "json", "no_redirect": 1, "skip_disambig": 1}
    try:
        time.sleep(PAUSE)
        r = requests.get(DDG_ENDPOINT, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        urls = []
        for item in data.get("RelatedTopics", []):
            if isinstance(item, dict) and "FirstURL" in item:
                urls.append(item["FirstURL"])
            if len(urls) >= max_results:
                break
        return urls
    except Exception:
        return []

def _bing_search(query, max_results=5):
    if not BING_KEY:
        return []
    headers = {"Ocp-Apim-Subscription-Key": BING_KEY}
    params = {"q": query, "count": max_results}
    try:
        time.sleep(PAUSE)
        r = requests.get(BING_ENDPOINT, headers=headers, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        return [v["url"] for v in data.get("webPages", {}).get("value", [])]
    except Exception:
        return []

def search_engine_query(query, max_results=5):
    results = _ddg_json(query, max_results)
    if results:
        return results
    return _bing_search(query, max_results)

def email_traces():
    try:
        requests.get("https://duckduckgo.com", timeout=5).raise_for_status()
    except Exception:
        print("[-] No internet or DuckDuckGo unreachable")
        return
    target = input("\U0001F4AC Enter target email (e.g. root@protonmail.com): ")
    print("\U0001F4AC Primary search")
    for u in search_engine_query(target, max_results=10):
        print(u)
    extra = [
        f'site:github.com "{target}"',
        f'site:twitter.com "{target}"',
        f'site:linkedin.com "{target}"',
        f'site:pastebin.com "{target}"',
        f'site:haveibeenpwned.com "{target}"'
    ]
    for q in extra:
        print(f"\n--- {q} ---")
        for u in search_engine_query(q, max_results=3):
            print(u)

def check_proton_api():
    r = requests.get("https://api.protonmail.ch/pks/lookup?op=index&search=admin@protonmail.com")
    if r.status_code == 200:
        print("\U0001F4AC ProtonMail API is ONLINE \U0001F7E2")
    else:
        print("\U0001F4AC ProtonMail API appears OFFLINE \U0001F534")

def proton_mail_account_check():
    rgx = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    while True:
        mail = input("\U0001F4AC Enter the target Email: ")
        if re.search(rgx, mail):
            break
        print("\U0001F4AC Invalid email format \U0001F534")
    r = requests.get(f"https://api.protonmail.ch/pks/lookup?op=index&search={mail}")
    txt = r.text
    if "info:1:0" in txt:
        print("\U0001F4AC ProtonMail account is NOT VALID. \U0001F534")
    if "info:1:1" in txt:
        print("\U0001F4AC ProtonMail Account is VALID. \U0001F7E2")

DARK_WEB_SOURCES = [
    ("Ahmia", "https://ahmia.fi/search/", lambda html: [a["href"] for a in BeautifulSoup(html, "html.parser").select("a[href]") if a["href"].startswith("http")]),
    ("OnionSearch", "https://onionsearchengine.com/search", lambda html: [a["href"] for a in BeautifulSoup(html, "html.parser").select("div.result a") if a["href"].startswith("http")]),
    ("Torch", "https://torchsearch.net/search", lambda html: [a["href"] for a in BeautifulSoup(html, "html.parser").select("table tr td a") if a["href"].startswith("http")]),
    ("NotEvil", "https://notevil.net/search", lambda html: [a["href"] for a in BeautifulSoup(html, "html.parser").select("ul.results li a") if a["href"].startswith("http")])
]

def _fetch_dark_web(name, base_url, extractor, query):
    try:
        resp = requests.get(base_url, params={"q": query}, timeout=12)
        resp.raise_for_status()
        return extractor(resp.text)
    except Exception as exc:
        print(f"[{name}] request failed: {exc}")
        return []

def dark_web_search(query, max_per_source=5):
    seen = set()
    aggregated = []
    for name, url, extractor in DARK_WEB_SOURCES:
        print(f"\n⛓️  Querying {name} …")
        results = _fetch_dark_web(name, url, extractor, query)
        if results:
            for r in results[:max_per_source]:
                if r not in seen:
                    seen.add(r)
                    aggregated.append(r)
            break
        else:
            print(f"[{name}] returned no usable results – trying next source…")
        time.sleep(4)
    return aggregated

def dark_web_traces():
    query = input("\U0001F4AC Input target email or any dark‑web query: ").strip()
    if not query:
        print("⚠️  Empty query – aborting.")
        return
    results = dark_web_search(query, max_per_source=10)
    if not results:
        print("\n❌  All public dark‑web indexes failed – you may need a Tor exit node or a VPN.")
        return
    choice = input("\U0001F4AC View results in Browser (B) or Terminal (T)? ").lower()
    if choice == "b":
        webbrowser.open(results[0])
        print("🔗 Opened first result in your default browser.")
    else:
        print("\n--- Dark‑Web Search Results ---")
        for idx, url in enumerate(results, 1):
            print(f"{idx}. {url}")

def dark_web_browser():
    query = input("\U0001F4AC Input target email or any dark‑web query: ").strip()
    results = dark_web_search(query, max_per_source=1)
    if results:
        webbrowser.open(results[0])
    else:
        print("❌  No results – all indexes failed.")

def dark_web_terminal():
    query = input("\U0001F4AC Input target email or any dark‑web query: ").strip()
    results = dark_web_search(query, max_per_source=10)
    if results:
        print("\n--- Dark‑Web Search Results ---")
        for idx, url in enumerate(results, 1):
            print(f"{idx}. {url}")
    else:
        print("❌  No results – all indexes failed.")

def pgp_key_information():
    choice = input("\U0001F4AC View PGP Key in Terminal (T) or Download Key (D)? ")
    if choice.lower() == "t":
        pgp_key_view()
    else:
        pgp_key_download()

def pgp_key_download():
    q = input("\U0001F4AC Input target email to download PGP key: ")
    webbrowser.open(f"https://api.protonmail.ch/pks/lookup?op=get&search={q}")

def pgp_key_view():
    rgx = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    while True:
        mail = input("\U0001F4AC ProtonMail Email: ")
        if re.search(rgx, mail):
            break
        print("\U0001F4AC Invalid email format")
    r = requests.get(f"https://api.protonmail.ch/pks/lookup?op=index&search={mail}")
    txt = r.text
    if "info:1:0" in txt:
        print("\U0001F4AC ProtonMail account is NOT VALID \U0001F534")
        return
    print("\U0001F4AC ProtonMail Account PGP Key Found. \U0001F7E2")
    patterns = [("2048:", "RSA 2048-bit"), ("4096:", "RSA 4096-bit"), ("22::", "ECC Curve25519")]
    for pat, label in patterns:
        m = re.search(pat + r"(.*)::", txt)
        if m:
            ts = int(m.group(1))
            dt = datetime.fromtimestamp(ts)
            print(f"\nPGP Key Date and Creation Time: {dt}")
            print(f"Encryption Standard : {label}")
            break
    while True:
        ans = input('\033[1m"Y"/"N":\033[0m ')
        if ans.lower() == "y":
            pub = requests.get(f"https://api.protonmail.ch/pks/lookup?op=get&search={mail}")
            print(pub.text)
            break
        if ans.lower() == "n":
            break

def main():
    print_proton_banner()
    start = input('\U0001F4AC Type "c" to check API status or "go" to start: ')
    if start.lower() == "c":
        check_proton_api()
    view = input('\U0001F4AC View Modules? (Y/N): ')
    if view.lower() == "y":
        print_proton_intro()
    while True:
        cmd = input('\U0001F4AC Choose [E]mail, [T]race, [W]eb, [K]eys: ').lower()
        if cmd == "e":
            proton_mail_account_check()
        elif cmd == "t":
            email_traces()
        elif cmd == "w":
            dark_web_traces()
        elif cmd == "k":
            pgp_key_information()
        cont = input("\U0001F4AC Continue? (Y/N): ").lower()
        if cont != "y":
            break

if __name__ == "__main__":
    main()
