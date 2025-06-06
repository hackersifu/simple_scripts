import requests
import sys
import logging

def lookup_arin_ip(ip):
    """Function to look up an IP address using ARIN's REST API."""
    url = f'https://whois.arin.net/rest/ip/{ip}'
    headers = {
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        net = data.get('net', {})
        org_ref = net.get('orgRef', {}).get('@name', 'N/A')
        handle = net.get('handle', 'N/A')
        name = net.get('name', 'N/A')
        registration_date = net.get('registrationDate', 'N/A')

        print(f"IP Address: {ip}")
        print(f"Network Name: {name}")
        print(f"Network Handle: {handle}")
        print(f"Organization: {org_ref}")
        print(f"Registration Date: {registration_date}")

    except requests.exceptions.HTTPError as e:
        logging.error(f"[!] HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"[!] Request failed: {e}")
    except ValueError:
        logging.error("[!] Failed to parse JSON response.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.info("Usage: python arin_lookup.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]
    lookup_arin_ip(ip_address)