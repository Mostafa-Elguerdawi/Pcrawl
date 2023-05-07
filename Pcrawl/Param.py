import argparse
import requests
from bs4 import BeautifulSoup as bs
from colors import red, green, blue, yellow
import threading

parser = argparse.ArgumentParser(description='Crawl URLs and extract parameters')
parser.add_argument('-f', '--input_file', type=str, required=True, help='Path to the file containing URLs')
parser.add_argument('-o', '--output_file', type=str, required=True, help='Path to the output file')
parser.add_argument('-t', '--threads', type=int, default=1, help='Number of threads to use for crawling URLs')
args = parser.parse_args()

class Param:
    def __init__(self, url, method, param):
        self.url = url
        self.method = method
        self.param = param
        
    def getParams(self):
        req = requests.get(self.url, timeout=3).text
        soup = bs(req, "html.parser")
        print(" ")
        print(red(f"[+]Crawling {self.url}"))
        print(" ")
        for form in soup.findAll("form"):
            self.method += form.get("method")
            if len(self.method) > 0:
                print(blue(f"Method is {self.method}"))
                print(" ")
                for input in soup.findAll("input"):
                    self.param += f"{input.get('name')}=FUZZ&"
                if len(self.param) > 0:
                    print(yellow(f"Params is {self.param}"))
                    print(" ")
    
    def Save(self, output):
        with open(output, 'a') as fil:
            content = '\n' + self.url + '\n' + f"Method is {self.method}" + '\n' + f"Params : {self.param}" + '\n' + '\n' + ("#"*50) + '\n' + " "
            fil.write(content)

def crawl_url(url):
    try:
        crawl = Param(url, "", "")
        crawl.getParams()
        print(" ")
        print("#"*50)
        crawl.Save(args.output_file)
    except requests.exceptions.Timeout:
        print(" ")
        print(red(f"Time Out ===> {url}"))
        print(" ")
        print("#"*50)
    except Exception as e:
        pass

with open(args.input_file, 'r') as f:
    urls = f.read().splitlines()

banner = open("banner.txt", 'r').read()
print(blue(banner))
print(red("\t[*]By Mostafa Elguerdawi"))

print(" ")

threads = []
for url in urls:
    t = threading.Thread(target=crawl_url, args=(url,))
    threads.append(t)

    if len(threads) == args.threads:
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        threads = []

if len(threads) > 0:
    for t in threads:
        t.start()
    for t in threads:
        t.join()
