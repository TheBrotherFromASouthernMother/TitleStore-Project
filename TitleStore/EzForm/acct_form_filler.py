import os
import sys
from fpdf import FPDF
from PyPDF2 import PdfFileReader, PdfFileWriter
# import .views

def makePdf(data): # data passed in from form
    # declare location of PDFs to use
    overlay_pdf_file_name = 'overlay_PDF.pdf' # textOverSuccess.pdf
    pdf_template_file_name = 'acct_background.pdf' # base_PDF_template

    #TODO: Change data to bracket notation so Python will stop complaining
    result_pdf_file_name = 'result_form' + data['cu_last_name'] + '.pdf'
    # result_pdf_file_name = "./pdfs/" + data['person_name'] + ".pdf"


    pdf = FPDF('P', 'mm', 'letter') # paragraph oriented, millimeters measured, letter page sized
    pdf.set_margins(0, 0, 0)
    pdf.add_page(same=True) # sets page added to FPDF object to same parameters
    pdf.set_font('Arial', '', 12) # font, style ('' means normal), 12pt

    ### test dictionary for overlay data
    ### WORKS

    vehicle_vin =  data.vin  # customer name ### COORDS BELONG TO VIN
    year = data.year # vehicle year
    vehicle_make = data.make # vehicle make
    vehicle_style = data.style # vehicle body style
    vehicle_model = data.model # vehicle model

    vehicle_title_no = data.title # vehicle title/document number
    vehicle_license = data.license # TX license plate number

    customer_name = data.name # customer name
    second_customer_name = data.second_name # additional customer name

    date = '' # date above, date below

    recipient_first_name = data.recipient_first_name # receipient first name
    recipient_middle_name = data.recipient_middle_name # recipient middle name
    recipient_last_name = data.recipient_last_name # receipient last name
    recipient_suffix = data.recipient_suffix # receipient name suffix

    address = data.address # mailing address
    city = data.city # city
    state = data.state # state
    zip_code = data.zip_code # zip

    email = data.email # email
    phone = data.phone # phone number


    '''
        vehicle_vin =  '12345678901234567' # customer name ### COORDS BELONG TO VIN
        year = '2000' # vehicle year
        vehicle_make = 'Affordy' # vehicle make
        vehicle_style = 'Stylo' # vehicle body style
        vehicle_model = 'Edsel' # vehicle model

        vehicle_title_no = '1234567890' # vehicle title/document number
        vehicle_license = 'DLR-J3L2' # TX license plate number

        data['person_name'] = 'Bob' # customer name
        second_customer_name = 'Cat' # additional customer name

        date = 'May 1, 2018' # date above, date below

        recipient_first_name = 'Johnny' # receipient first name
        recipient_middle_name = 'Middle' # recipient middle name
        recipient_last_name = 'Recipient' # receipient last name
        recipient_suffix = '' # receipient name suffix

        address = '123 Fake St.' # mailing address
        city = 'Houston' # city
        state = 'TX' # state
        zip_code = '77777' # zip

        email = 'john@john.com' # email
        phone = '123-123-1234' # phone number
    '''






    # dictionary for ACCT form

    form_dictionary = {
        'form': 'ACCT', # form_type
        'data': [
            { 'x': 6, 'y': 140, 'w': 94, 'h': 5, 'value': vehicle_vin }, # customer name ### COORDS BELONG TO VIN
            { 'x': 102, 'y': 140, 'w': 23, 'h': 5, 'value': year }, # vehicle year
            { 'x': 127, 'y': 140, 'w': 22, 'h': 5, 'value': vehicle_make }, # vehicle make
            { 'x': 150, 'y': 140, 'w': 22, 'h': 5, 'value': vehicle_style }, # vehicle body style
            { 'x': 173, 'y': 140, 'w': 22, 'h': 5, 'value': vehicle_model }, # vehicle model

            { 'x': 6, 'y': 149, 'w': 22, 'h': 5, 'value': vehicle_title_no }, # vehicle title/document number
            { 'x': 102, 'y': 149, 'w': 22, 'h': 5, 'value': vehicle_license }, # TX license plate number

            { 'x': 88, 'y': 175, 'w': 22, 'h': 5, 'value': customer_name }, # customer name
            { 'x': 88, 'y': 189, 'w': 22, 'h': 5, 'value': second_customer_name }, # additional customer name

            { 'x': 170, 'y': 175, 'w': 22, 'h': 5, 'value': date }, # date above
            { 'x': 170, 'y': 189, 'w': 22, 'h': 5, 'value': date }, # date below

            { 'x': 6, 'y': 209, 'w': 73, 'h': 5, 'value': recipient_first_name }, # receipient first name
            { 'x': 80, 'y': 209, 'w': 46, 'h': 5, 'value': recipient_middle_name }, # recipient middle name
            { 'x': 127, 'y': 209, 'w': 46, 'h': 5, 'value': recipient_last_name }, # receipient last name
            { 'x': 174, 'y': 209, 'w': 21, 'h': 5, 'value': recipient_suffix }, # receipient name suffix

            { 'x': 6, 'y': 218, 'w': 73, 'h': 5, 'value': address }, # mailing address
            { 'x': 80, 'y': 218, 'w': 80, 'h': 5, 'value': city }, # city
            { 'x': 127, 'y': 218, 'w': 46, 'h': 5, 'value': state }, # state
            { 'x': 174, 'y': 218, 'w': 22, 'h': 5, 'value': zip_code }, # zip

            { 'x': 6, 'y': 227, 'w': 22, 'h': 5, 'value': email }, # email
            { 'x': 103, 'y': 227, 'w': 22, 'h': 5, 'value': phone }, # phone number
        ]
    }





    '''
    {
        'form': 'ACCT',
        'data': [
            { 'x': 6, 'y': 140, 'w': 94, 'h': 5, 'value': vehicle_vin }, # customer name ### COORDS BELONG TO VIN
            { 'x': 102, 'y': 140, 'w': 23, 'h': 5, 'value': year }, # vehicle year
            { 'x': 127, 'y': 140, 'w': 22, 'h': 5, 'value': vehicle_make }, # vehicle make
            { 'x': 150, 'y': 140, 'w': 22, 'h': 5, 'value': vehicle_style }, # vehicle body style
            { 'x': 173, 'y': 140, 'w': 22, 'h': 5, 'value': vehicle_model }, # vehicle model

            { 'x': 6, 'y': 149, 'w': 22, 'h': 5, 'value': vehicle_title_no }, # vehicle title/document number
            { 'x': 102, 'y': 149, 'w': 22, 'h': 5, 'value': vehicle_license }, # TX license plate number

            { 'x': 88, 'y': 175, 'w': 22, 'h': 5, 'value': customerData['person_name'] }, # customer name
            { 'x': 88, 'y': 189, 'w': 22, 'h': 5, 'value': second_customer_name }, # additional customer name

            { 'x': 170, 'y': 175, 'w': 22, 'h': 5, 'value': date }, # date above
            { 'x': 170, 'y': 189, 'w': 22, 'h': 5, 'value': date }, # date below

            { 'x': 6, 'y': 209, 'w': 73, 'h': 5, 'value': recipient_first_name }, # receipient first name
            { 'x': 80, 'y': 209, 'w': 46, 'h': 5, 'value': recipient_middle_name }, # recipient middle name
            { 'x': 127, 'y': 209, 'w': 46, 'h': 5, 'value': recipient_last_name }, # receipient last name
            { 'x': 174, 'y': 209, 'w': 21, 'h': 5, 'value': recipient_suffix }, # receipient name suffix

            { 'x': 6, 'y': 218, 'w': 73, 'h': 5, 'value': address }, # mailing address
            { 'x': 80, 'y': 218, 'w': 80, 'h': 5, 'value': city }, # city
            { 'x': 127, 'y': 218, 'w': 46, 'h': 5, 'value': state }, # state
            { 'x': 174, 'y': 218, 'w': 22, 'h': 5, 'value': zip_code }, # zip

            { 'x': 6, 'y': 227, 'w': 22, 'h': 5, 'value': email }, # email
            { 'x': 103, 'y': 227, 'w': 22, 'h': 5, 'value': phone }, # phone number
        ]
    }
    '''
    ''' previous test dictionary
    form_dictionary = {
        'Vehicle Identification Number': 'TEST VIN #',
        'Year': 'TEST 1999',
        'Make': 'TES Cake',
        'Body Style': 'TEST Being There',
        'Model': 'TEST Modal',
        'TitleDocument Number if unknown leave blank': 'TEST 111 111',
        'Texas License Plate Number if unknown leave blank': 'TEST 12AS3F',
        'Printed Name of Applicant Owner': 'TEST FIRSTNAME',
        'Date': 'TEST TODAY',
        'Additional Applicant Owner': 'TEST NONE',
        'Date_2': 'TEST TODAY',
        'First Name or Entity Name Middle Name Last Name Suffix if any': 'TEST ENTITY MIDDLE',
        'Mailing Address City State Zip': 'TEST 123 FAKE ST',

        'Email': 'TEST GABBA@HEY.COM',
        'Phone Number': 'TEST 123-123-1234'
    }
    '''



    # adds form data to overlay pdf
    for field in range(0, len(form_dictionary['data'])):
        pdf.set_xy(form_dictionary['data'][field]['x'], form_dictionary['data'][field]['y'])
        pdf.cell(form_dictionary['data'][field]['w'], form_dictionary['data'][field]['h'], form_dictionary['data'][field]['value'])

    # ready to overlay to watermark template
    pdf.output('overlay_PDF.pdf')
    pdf.close()


    ### this takes the overlay data and merges it with the watermark template
    ### WORKS
    with open("./utils/acct_background.pdf", 'rb') as pdf_template_file, open(overlay_pdf_file_name, 'rb') as overlay_PDF_file:
        # open watermark template pdf object
        pdf_template = PdfFileReader(pdf_template_file)
        # open overlay data pdf object
        overlay_PDF = PdfFileReader(overlay_PDF_file)

        template_total_pages = pdf_template.getNumPages()
        # iterate through each page to flatten overlay data and watermark template
        for page_number in range(0, template_total_pages):
            # get each page from watermark template
            template_page = pdf_template.getPage(page_number)
            # merge overlay data to watermark template
            template_page.mergePage(overlay_PDF.getPage(page_number))
            # write result to new PDF
            output_pdf = PdfFileWriter()
            output_pdf.addPage(template_page)
        with open(result_pdf_file_name, 'wb') as result_pdf_file:
            output_pdf.write(result_pdf_file)






























# import io
# from fpdf import FPDF
# from pdfrw import PdfReader, PdfWriter, PageMerge


# from PyPDF2.generic import BooleanObject, NameObject, IndirectObject


# blank_pdf_file_name = 'blank_PDF.pdf'






# # test data to fill in form
# acct_vin = 'hello imma test phrase'
# acct_year = str(2000)
# acct_make = str('makeorbreak')







# VIN
# ACCT0
# # pdf.set_xy(ACCT0x, ACCT0y)
# pdf.set_xy(13, 146)
# # pdf.cell(ACCT0w, ACCT0h, ACCT0)
# pdf.cell(94, 5.5, acct_vin)

# # year
# # pdf.set_xy(ACCT1x, ACCT1y)
# pdf.set_xy(108, 146)
# # pdf.cell(ACCT1w, ACCT1h, ACCT1)
# pdf.cell(23, 5.5, acct_year)

# # make
# pdf.set_xy(133, 146)
# pdf.cell(22, 5.5, acct_make)















# ### ITERATING TO CREATE OVERLAY PDF NOT WORKING YET
# incoming_form = {
#     'form': 'ACCT',
#     'ACCT0x': 13,
#     'ACCT0y': 146,
#     'ACCT0w': 94,
#     'ACCT0h': 5.5,
#     'ACCT0': 'testing for iterating',
#     'ACCT1x': 108,
#     'ACCT1y': 146,
#     'ACCT1w': 23,
#     'ACCT1h': 5.5,
#     'ACCT1': '1999',
#     'ACCT2x': 133,
#     'ACCT2y': 146,
#     'ACCT2w': 22,
#     'ACCT2h': 5.5,
#     'ACCT2': 'iterate make',
# }

# # order the form fields topmost to bottom, leftmost to right???
# # ACCT (Application for a Certified Copy of Title) ACCT(form_field)

# # the form data is incoming as a dictionary
# # for field, value in incoming_form: MAYBS NOT WORK
# for field in range(0, len(incoming_form)-1):
#     pdf.set_xy(incoming_form['form'] + str(field) + 'x', incoming_form['form'] + str(field) + 'y')
#     pdf.cell(incoming_form['form'] + str(field) + 'w', incoming_form['form'] + str(field) + 'h', incoming_form['form'] + str(field))

# # ready to overlay to watermark template
# pdf.output('overlay_PDF.pdf')
# pdf.close()












'''
# ### TRYING TO REFACTOR SO THAT ONLY ONE PYTHON LIB IS USED. THOUGH I ADD /NEEDAPPEARANCES FLAG, RESULTS COME UP BLANK, FIELDS NOT FILLED. FIELDS FILLED IN BY DICTIONARY KEY-VALUE PAIRS, MERGED WITH A BLANK PAGE TO FLATTEN
# # set NeedAppearances flag
# def set_need_appearances(PdfFileWriter):
#     catalog = PdfFileWriter._root_object
#     # get the AcroForm tree
#     if '/AcroForm' not in catalog:
#         PdfFileWriter._root_object.update({
#             NameObject('/AcroForm'): IndirectObject(len(PdfFileWriter._objects), 0, PdfFileWriter)
#         })

#     need_appearances = NameObject('/NeedAppearances')
#     PdfFileWriter._root_object['/AcroForm'][need_appearances] = BooleanObject(True)
#     return PdfFileWriter

# with open(pdf_template_file_name, 'rb') as pdf_template_file, open(blank_pdf_file_name, 'rb') as blank_PDF_file:
#     # open blank pdf object
#     blank_PDF = PdfFileReader(blank_PDF_file)

#     # open  watermark template pdf object
#     pdf_template = PdfFileReader(pdf_template_file)

#     if '/AcroForm' in pdf_template.trailer['/Root']:
#         pdf_template.trailer['/Root']['/AcroForm'].update(
#             {NameObject('/NeedAppearances'): BooleanObject(True)}
#         )

#     template_total_pages = pdf_template.getNumPages()
#     # iterate through each page to flatten overlay data and watermark template
#     for page_number in range(0, template_total_pages):
#         # get each page from watermark template
#         template_page = pdf_template.getPage(page_number)

#         # write result to new PDF
#         output_pdf = PdfFileWriter()
#         set_need_appearances(output_pdf)
#         if '/AcroForm' in output_pdf._root_object:
#             output_pdf._root_object['/AcroForm'].update(
#                 {NameObject('/NeedAppearances'): BooleanObject(True)}
#             )
#         output_pdf.updatePageFormFieldValues(template_page, form_dictionary)
#         template_page.mergePage(blank_PDF.getPage(0))

#         output_pdf.addPage(template_page)
#     with open(result_pdf_file_name, 'wb') as result_pdf_file:
#         output_pdf.write(result_pdf_file)
'''
































# # testing compound /with/ statements to allow opened files to close
# # with open(pdf_template_file_name, 'rb') as pdf_template, open(overlay_pdf_file_name, 'rb') as overlay_PDF: # template_file_opened:

# # open your watermark template PDF
# pdf_template = PdfFileReader(open(pdf_template_file_name, 'rb'))
# # open overlay data pdf
# overlay_PDF = PdfFileReader(open(overlay_pdf_file_name, 'rb'))

# template_total_pages = pdf_template.getNumPages()
# # iterate through each page to flatten overlay data and watermark template
# for page_number in range(0, template_total_pages):
#     # get each page from watermark template
#     template_page = pdf_template.getPage(page_number)
#     # merge overlay data to watermark template
#     template_page.mergePage(overlay_PDF.getPage(page_number))
#     # write result to new PDF
#     output_pdf = PdfFileWriter()
#     output_pdf.addPage(template_page)
# output_pdf.write(open(result_pdf_file_name, 'wb'))





















# # get each page from watermark template
# template_page = pdf_template.getPage(0)
# # merge overlay data to watermark template
# template_page.mergePage(overlay_PDF.getPage(0))
# # write result to new PDF
# output_pdf = PdfFileWriter()
# output_pdf.addPage(template_page)
# output_pdf.write(open(result_pdf_file_name, 'wb'))














# applies watermark original form
# argv = sys.argv[1:] # find a way to get watermark original form from method other than passing in CLI arguments
# as of 5-15-18 2:30p usage: python3 fill_form_watermark.py -u textOverSuccess.pdf decryptedVTR431flat.pdf
# as of 5-15-18 2:45p usage: set inpfn and wmarkfn are variable names/filenames to the input and watermark files

# check if watermark underneath flag is necessary
# underneath = '-u' # in argv
# if underneath:
#     del argv[argv.index('-u')]
# inpfn, wmarkfn = argv

# get first page of template
# inpfn = 'textOverSuccess.pdf'
# wmarkfn = 'decryptedVTR341flat.pdf'

# outfn = 'watermark.' + os.path.basename(inpfn) # -u flag puts watermark underneath

# wmark = PageMerge().add(PdfReader(wmarkfn).pages[0])[0]
# trailer = PdfReader(inpfn)
# for page in trailer.pages:
#     PageMerge(page).add(wmark, prepend=underneath).render()
# PdfWriter(outfn, trailer=trailer).write()
