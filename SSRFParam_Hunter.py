#! /usr/bin/python3

import re
import sys
from collections import defaultdict

def print_ascii_art():
    ascii_art = """
                                                                       
 _____ _____ _____ _____ _____                         _____         _           
|   __|   __| __  |   __|  _  |___ ___ ___ _____      |  |  |_ _ ___| |_ ___ ___ 
|__   |__   |    -|   __|   __| .'|  _| .'|     |     |     | | |   |  _| -_|  _|
|_____|_____|__|__|__|  |__|  |__,|_| |__,|_|_|_|_____|__|__|___|_|_|_| |___|_|  
                                                |_____|                          
                                                
 					Script By: Abdul Samad - ABStronics
 		  			Visit: https://abstronics.com
 --------------------------------------------------------------------------------
    """
    print(ascii_art)

def main(file_path):
    # Define the keywords
    keywords = [
        'dest=', 'redirect=', 'uri=', 'path=', 'continue=', 'url=', 'window=', 'next=', 'data=', 'reference=', 'site=', 'html=', 'val=', 'validate=', 'domain=', 'callback=', 'return=', 'page=', 'feed=', 'host=', 'port=', 'to=', 'out=', 'view=', 'dir=', 'link=', 'file=', 'target=', 'address=', 'resource=', 'location=', 'fetch=', 'load=', 'goto=', 'source=', 'external=', 'url_to_scan=', 'request=', 'api=', 'proxy=', 'image=', 'script=', 'iframe=', 'include=', 'ajax=', 'http=', 'https=', 'ftp=', 'smb=', 'ldap=', 'gopher=', 'dict=', 'mailto:', 'telnet://', 'ws://', 'wss://', 'javascript:', 'vbscript:', 'data:', 'about:', 'chrome:', 'ping=', 'open=', 'read=', 'write=', 'exec=', 'cmd=', 'shell=', 'img=', 'picture=', 'thumbnail=', 'icon=', 'logo=', 'file_name=', 'path_to_file=', 'file_path=', 'src=', 'href=', 'link_to=', 'target_url=', 'external_url=', 'destination=', 'remote=', 'fetch_url=', 'load_url=', 'request_url=', 'redirect_url=', 'src_url=', 'data_url=', 'url_link=', 'url_to_load=', 'url_to_fetch=', 'url_to_request=', 'url_to_redirect=', 'src_link=', 'href_link=', 'link_url=', 'request_data=', 'redirect_data=', 'source_url=', 'target_link=', 'external_link=', 'fetch_link=', 'load_link=', 'ajax_url=', 'script_url=', 'iframe_url=', 'include_url=', 'url_data=', 'target_data=', 'external_data=', 'fetch_data=', 'load_data=', 'ajax_data=', 'script_data=', 'iframe_data=', 'include_data=', 'remote_url=', 'remote_link=', 'remote_data=', 'remote_request=', 'remote_fetch=', 'remote_load=', 'remote_ajax=', 'remote_script=', 'remote_iframe=', 'remote_include=', 'server=', 'domain_name=', 'ip=', 'ip_address=', 'server_ip=', 'host_ip=', 'domain_ip=', 'ip_to_scan=', 'server_name=', 'host_name=', 'ip_address_to_scan=', 'server_address=', 'host_address=', 'domain_address=', 'port_number=', 'server_port=', 'host_port=', 'domain_port=', 'port_to_scan=', 'server_port_number=', 'host_port_number=', 'domain_port_number=', 'protocol=', 'protocol_type=', 'request_protocol=', 'redirect_protocol=', 'src_protocol=', 'data_protocol=', 'url_protocol=', 'external_protocol=', 'fetch_protocol=', 'load_protocol=', 'ajax_protocol=', 'script_protocol=', 'iframe_protocol=', 'include_protocol=', 'remote_protocol=', 'server_protocol=', 'host_protocol=', 'domain_protocol=', 'parameter=', 'param=', 'input=', 'value=', 'query=', 'form=', 'payload=', 'body=', 'content=', 'post:'


    ]

    # Compile regex for faster matching
    keywords_regex = re.compile("|".join([re.escape(keyword) for keyword in keywords]), re.IGNORECASE)

    # Read URLs from the specified file
    with open(file_path, 'r') as file:
        urls = file.readlines()

    # Dictionary to hold matched URLs grouped by keyword
    matched_urls = defaultdict(list)

    # Filter and print URLs that contain any of the keywords
    for url in urls:
        url = url.strip()
        for keyword in keywords:
            if re.search(re.escape(keyword), url, re.IGNORECASE):
                matched_urls[keyword].append(url)

    # Print the results grouped by keywords
    for keyword, urls in matched_urls.items():
        print(f"Keyword: {keyword}")
        for url in urls:
            print(f"    {url}")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_ascii_art()
        print("Usage: python CredHunter.py <urls.txt>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    print_ascii_art()
    main(file_path)
