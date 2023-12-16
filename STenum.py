import argparse
import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Your API KEY here, Visit https://securitytrails.com/app/account/credentials to get it.
APIKEY = "PUT YOUR OWN API KEY HERE" 

def collect(domain,exportfile):
	subdomainURL = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0","apikey":APIKEY}
	response = requests.get(subdomainURL, headers=headers, verify=False)
	resString = response.text
	resArray = json.loads(resString)
	#~Maakthon
	# Save result to file in current dir called securitytrails_subdomains.txt
	subdomainLength = len(resArray['subdomains'])
	for num in range(subdomainLength):
		with open(exportfile,"a") as f:
			subdomain = str(resArray['subdomains'][num]+"."+domain)
			f.write(subdomain)
			f.write("\n")
	f.close()
	print(f"[+] Successfully Subdomains Collected {subdomainLength} from SecurityTrails in file {exportfile}")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='SecurityTrails Subdomain Enum tool.')

	parser.add_argument('-d', '--domain',required=True, help='The domain name ex:apple.com')
	parser.add_argument('-f', '--file', required=True, help='The output file name ex:subdomain.txt')

	args = parser.parse_args()

	domain = str(args.domain)
	exportfile = str(args.file)
	try:

		collect(domain,exportfile)
	except Exception as err:
		print(err)

