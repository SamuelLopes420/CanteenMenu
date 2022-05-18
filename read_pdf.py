
from PIL import Image
import fitz

monday = (127, 165, 250, 310)
tuesday = (265, 165, 390, 310)
wednesday = (407, 165, 530, 310)
thursday = (544, 165, 670, 310)
friday = (680, 165, 800, 310)


def main():
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

    # page = pdf.load_page(0)
    # pix = page.get_pixmap()

    # img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    # img.save("output.jpeg", "JPEG")
    # img = Image.open("output.jpeg")
    # img_croped = img.crop(monday)
    # img_croped.save("output2.jpeg")

    

    
if __name__ == '__main__':
    main()