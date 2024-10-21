import PyPDF2

def compare_pdfs(pdf1_path, pdf2_path):

    with open(pdf1_path, 'rb') as pdf1_file, open(pdf2_path, 'rb') as pdf2_file:

        pdf1reader = PyPDF2.PdfReader(pdf1_file)
        pdf2reader = PyPDF2.PdfReader(pdf2_file)

        if len(pdf1reader.pages) != len(pdf2reader.pages):
            return False


        for page_num in range(len(pdf1reader.pages)):
            pdf1_page = pdf1reader.pages[page_num].extract_text()
            pdf2_page = pdf2reader.pages[page_num].extract_text()

            if pdf1_page != pdf2_page:
                return False

    return True


pdf1 = 'p1.pdf'
pdf2 = 'p3.pdf'

result = compare_pdfs(pdf1, pdf2)

if result:
    print("yes,The PDFs are identical.")
else:
    print("no,The PDFs are not identical.")
