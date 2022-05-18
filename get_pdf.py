from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os


def main():
    url = "http://www.sas.uminho.pt/Default.aspx?tabid=10&pageid=26&lang=pt-PT"

    folder_location = "{}\pdfs".format(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.exists(folder_location):os.mkdir(folder_location)

    response = requests.get(url)
    soup= BeautifulSoup(response.text, "html.parser")     
    for link in soup.select("a[href$='.pdf']"):
        #Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)
    
if __name__ == '__main__':
    main()