
from PIL import Image
import fitz
from io import BytesIO
import pytesseract


def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pdf = fitz.open(r"pdfs\Ementa_Cantina_Jantar.pdf")
    page = pdf.load_page(0)
    pix = page.get_pixmap()

    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img.save("output.jpeg", "JPEG")
    img = Image.open("output.jpeg")

    print(pytesseract.image_to_string(img))
    
    
if __name__ == '__main__':
    main()