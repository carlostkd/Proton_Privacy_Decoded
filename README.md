# Proton-Privacy-Decoded
# Script to Explore ProtonMail and Vpn

<p align="center">

  <img src="https://raw.githubusercontent.com/carlostkd/Proton_Privacy_Decoded/master/proton.svg">

</p>


### Introducing PPD Proton-Privacy-Decoded

## Feel free to contribute

## What This Script Does?:

- ⚡ Check ProtonMail for valid accounts
- ⚡ Check User PGP Key, creation date and Key Type
- ⚡ Download PGP Keys
- ⚡ Check if the IP address is from ProtonVPN and from which Country
- ⚡ ProtonMail User Footprints DEEP and DARK WEB


[Getting Starting <g-emoji class="g-emoji" alias="footprints" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f463.png">👣</g-emoji>](#getting-started-)

## Instalation
```
git clone https://github.com/carlostkd/Proton_Privacy_Decoded.git
```
## Install the dependencies
```
pip3 install requests
pip3 install bs4
pip3 install ipaddress
pip3 install google
pip3 install json
```

## Run the script
```
python3 proton.py
```

### Screenshot 

<p align="center">

  <img src="https://raw.githubusercontent.com/carlostkd/Proton_Privacy_Decoded/master/ppd2.png">

</p>








## Known Issues that you shouldt report to me:

- :shipit: Account Creation date refers only to the date of the Encrypted Key

```
The user can have more email addresss or change the key every day?? :)
You should compare with "traces" or do a more extensive OSINT.
```
```
    That's it!
```
    





- :shipit: For some weird reason if you abuse from ProtonMail API the API always returns all queried emails as True even if the Email is not a ProtonMail Email.
```
do not abuse and everything runs fine
```

- :shipit: IP Address City Region Country etc returns values as "None"
```
reason 1 -The script uses a public api from ipapi with a limit of 30.000 queries a month
reason 2 -If you are using some vpn its possible that your vpn IP are blacklisted
```
- :shipit: solution
```
Use another api 
Change your VPN IP
```
- 👯 Did you found a Bug? Do you have any Sugestions?
```
Get in Touch
```

<p align="center">

<img src="https://raw.githubusercontent.com/carlostkd/EHR/master/ehr-sophie.svg">

</p>


<p align="center">

<img src="https://raw.githubusercontent.com/carlostkd/EHR/master/ehr-sophie-2022.svg">
</p>
