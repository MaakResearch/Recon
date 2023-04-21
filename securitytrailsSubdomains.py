import requests
import urllib3
import json
import sys

if len(sys.argv) != 2:
	print(f"\n[+] Usage: python {sys.argv[0]} domain\n\nEx: python {sys.argv[0]} apple.com")
	exit()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

domain = sys.argv[1]
# Your API KEY here, Visit https://securitytrails.com/app/account/credentials to get it.
APIKEY = "1KikdQkjao35iC2zP1DtcKGl60PzQmsA" 

def collect(domain):
	subdomainURL = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0","apikey":APIKEY}
	response = requests.get(subdomainURL, headers=headers, verify=False)
	resString = response.text
	resArray = json.loads(resString)
	#~Maakthon
	# Save result to file in current dir called securitytrails_subdomains.txt
	subdomainLength = len(resArray['subdomains'])
	for num in range(subdomainLength):
		with open("securitytrails_subdomains.txt","a") as f:
			subdomain = str(resArray['subdomains'][num]+"."+domain)
			f.write(subdomain)
			f.write("\n")
	f.close()
	print(f"[+] Successfully Subdomains Collected {subdomainLength} from SecurityTrails in file securitytrails_subdomains.txt")

if __name__ == "__main__":
	collect(domain)


