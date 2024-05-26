from pypdf import PdfWriter
from docx2pdf import convert

from os import remove as removeItem, path as osPath, listdir

TEMP_FILES = osPath.join(osPath.dirname(__file__), 'static','_temp_files')
TEMP_PDFS = osPath.join(osPath.dirname(__file__), 'static','_temp_pdfs')

def delete_old_files():
    for file in listdir(TEMP_FILES):
        file = osPath.join(TEMP_FILES, file)
        try:
            if osPath.isfile(file):
                removeItem(file)
        except Exception as e:
            print("delete_old_files() 1: ", e)
    for file in listdir(TEMP_PDFS):
        file = osPath.join(TEMP_PDFS, file)
        try:
            if osPath.isfile(file):
                removeItem(file)
        except Exception as e:
            print("delete_old_files() 2: ", e)

def d2p_cov(input_file:str, output_file:str):
    try:
        convert(input_file, output_file)
    except Exception as e:
        print("d2p_cov() : ",e)

def merge_pdfs(pdfs:list[str], output:str):
    try:
        merger = PdfWriter()
        for pdf in pdfs:
            if pdf.endswith('.pdf'):
                merger.append(pdf)
            elif pdf.endswith('.docx'):
                out = osPath.join(TEMP_PDFS, pdf.replace('.docx', '.pdf'))
                d2p_cov(pdf, out)
                pdf = out
                merger.append(pdf)
                removeItem(pdf)
        merger.write(output)
        merger.close()
    except Exception as e:
        print("merge_pdfs() : ",e)
        return False
    return True