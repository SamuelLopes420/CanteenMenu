from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os
from PIL import Image
import fitz

monday = (127, 165, 250, 310)
tuesday = (265, 165, 390, 310)
wednesday = (407, 165, 530, 310)
thursday = (544, 165, 670, 310)
friday = (680, 165, 800, 310)

def get_pdf():
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


def read_pdf():
    pdf_almoco = fitz.open(r"pdfs\Ementa_Cantina_Almoco.pdf")
    pdf_jantar = fitz.open(r"pdfs\Ementa_Cantina_Jantar.pdf")


    for i in range(pdf_almoco.page_count):
        page = pdf_almoco.load_page(i)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        monday_img = img.crop(monday)
        tuesday_img = img.crop(tuesday)
        wednesday_img = img.crop(wednesday)
        thursday_img = img.crop(thursday)
        friday_img = img.crop(friday)
        monday_img.save("almocos\week{}\monday.jpeg".format(i + 1), "JPEG")
        tuesday_img.save("almocos\week{}\\tuesday.jpeg".format(i + 1), "JPEG")
        wednesday_img.save("almocos\week{}\wednesday.jpeg".format(i + 1), "JPEG")
        thursday_img.save("almocos\week{}\\thursday.jpeg".format(i + 1), "JPEG")
        friday_img.save("almocos\week{}\\friday.jpeg".format(i + 1), "JPEG")

    for i in range(pdf_jantar.page_count):
        page = pdf_jantar.load_page(i)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        monday_img = img.crop(monday)
        tuesday_img = img.crop(tuesday)
        wednesday_img = img.crop(wednesday)
        thursday_img = img.crop(thursday)
        friday_img = img.crop(friday)
        monday_img.save("jantares\week{}\monday.jpeg".format(i + 1), "JPEG")
        tuesday_img.save("jantares\week{}\\tuesday.jpeg".format(i + 1), "JPEG")
        wednesday_img.save("jantares\week{}\wednesday.jpeg".format(i + 1), "JPEG")
        thursday_img.save("jantares\week{}\\thursday.jpeg".format(i + 1), "JPEG")
        friday_img.save("jantares\week{}\\friday.jpeg".format(i + 1), "JPEG")


def main():
    get_pdf()
    read_pdf()
    
if __name__ == '__main__':
    main()