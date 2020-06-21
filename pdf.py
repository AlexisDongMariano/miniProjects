'''
Date: Jun-12-2020

Platform: Windows

Description: Non-commented code (see SECTION D) allows to apply watermark from a pdf file to the pdf files in a specified
folder/directory using PyPDF2 <https://pythonhosted.org/PyPDF2/index.html>
**features merging multiple pdf files into 1 pdf file (see SECTION B)

Usage: python pdf.py [watermark_file.pdf] [dir_of_pdfFiles/]
**the watermark_file.pdf should be the same level of the pdf.py in the dir, else, specify the absolute path
**the dir_of_pdfFiles should be the same level of the pdf.py in the dir, else, specify the absolute path

Section: A-D
**Actual working code found in SECTION D
'''

# SECTION A:
# import PyPDF2 #module for pdf manipulation, stackoverflow prefers tika module
# with open('../dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file) #opening actual pdf file
#     reader.numPages #pages of document
#     reader.documentInfo
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     # print(page.extractText()) # getting the text content of the pdf

#     writer = PyPDF2.PdfFileWriter() #class for writing/saving pdf files
#     writer.addPage(page) #adds a page to the writer
#     with open('../tilt.pdf', 'wb') as new_file:
#         writer.write(new_file) #saving the new file
#########################################
# SECTION B: MERGING PDF FILES INTO 1 PDF FILE
# merges pdf files that are specified as arguments in the command line into a single pdf
# pdf_input = sys.argv[1:]
# merger =  PyPDF2.PdfFileMerger()
#
# for item in pdf_input:
#     merger.append(item)
#
# merger.write('super.pdf')
# #########################################
# SECTION C:
# APPLYING WATERMARK into the specied pdf files in command line as arguments
# Usage: python pdf.py [watermark_file] [watermark_files ...]
# python pdf.py watermark.pdf pdf1.pdf pdf2.pdf ...
# import PyPDF2
# import sys
#
# watermark_file = sys.argv[1]
# pdf_files = sys.argv[2:]
#
# print(watermark_file)
# print(pdf_files)
#
# for pdf_file in pdf_files:
#     with open(pdf_file, 'rb') as input_file:
#         pdf = PyPDF2.PdfFileReader(input_file)
#         with open(watermark_file, 'rb') as input_file_wtr:
#             watermark = PyPDF2.PdfFileReader(input_file_wtr)
#             watermark_page = watermark.getPage(0)
#             # pdf_pages = pdf.getPage()
#
#             pdf_writer = PyPDF2.PdfFileWriter()
#             for pdf_page_num in range(pdf.numPages):
#                 pdf_page = pdf.getPage(pdf_page_num)
#                 pdf_page.mergePage(watermark_page)
#                 pdf_writer.addPage(pdf_page)
#
#             new_file = pdf_file[3:]
#             with open(new_file, "wb") as output_file:
#                 pdf_writer.write(output_file)
#####################################
# SECTION D:
import PyPDF2
import sys
import os


def check_dir(pdf_dir):
    if not os.path.exists(pdf_dir):
        print(f"{pdf_dir} directory does not exists!")


def set_dir(pdf_dir):
    cwd = os.getcwd()
    if not pdf_dir.endswith('\\'):
        pdf_dir += '\\'
    dir_output = cwd + "\\" + pdf_dir
    check_dir(pdf_dir)
    return dir_output


def apply_watermark(watermark_file, pdf_dir):
    for pdf_entry in os.scandir(pdf_dir):  # or os.listdir(path)
        # img_entry.name #name of file
        # img_entry.path #path of file
        if pdf_entry.name.endswith('pdf') and pdf_entry.is_file():
            pdf_filename = pdf_entry.name
            try:
                with open(pdf_dir + pdf_filename, 'rb') as input_file:
                    pdf = PyPDF2.PdfFileReader(input_file)
                    print(f'{pdf} retrieved...')
                    with open(watermark_file, 'rb') as input_file_wtr:
                        watermark = PyPDF2.PdfFileReader(input_file_wtr)
                        watermark_page = watermark.getPage(0)
                        pdf_writer = PyPDF2.PdfFileWriter()

                        for pdf_page_num in range(pdf.numPages):
                            pdf_page = pdf.getPage(pdf_page_num)
                            pdf_page.mergePage(watermark_page)
                            pdf_writer.addPage(pdf_page)

                            with open(f'watermarked_{pdf_filename}', "wb") as output_file:
                                pdf_writer.write(output_file)
            except:
                print(f'Unable to open {pdf_filename}')


watermark_file = sys.argv[1]
pdf_dir = set_dir(sys.argv[2])
apply_watermark(watermark_file, pdf_dir)
