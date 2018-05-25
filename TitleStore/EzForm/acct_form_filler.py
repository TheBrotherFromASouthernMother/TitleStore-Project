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
    pdf.add_page() # sets page added to FPDF object to same parameters
    pdf.set_font('Arial', '', 12) # font, style ('' means normal), 12pt

    # test dictionary for overlay data
    ## this converts the HTTP body request data to variable names for the PDF maker function
    vehicle_vin =  data['v_vin'] # customer name ### COORDS BELONG TO VIN
    vehicle_year = data['v_year'] # vehicle year
    vehicle_make = data['v_make'] # vehicle make
    vehicle_style = data['v_body_style'] # vehicle body style
    vehicle_model = data['v_model'] # vehicle model

    # vehicle_title_no = data['v_title'] # vehicle title/document number
    # vehicle_plate_number = data['v_plate_number'] # TX license plate number
    #
    # applicant_name = data['applicant_name'] # applicant name
    # second_applicant_name = data['second_applicant_name'] # additional applicant name
    # date = '' # date above, date below

    recipient_first_name = data['cu_first_name'] # receipient first name
    recipient_middle_name = data['cu_middle_name'] # recipient middle name
    recipient_last_name = data['cu_last_name'] # receipient last name
    recipient_suffix = data['cu_suffix'] # receipient name suffix

    address = data['cu_address_line_1'] # mailing address
    city = data['cu_city'] # city
    state = data['cu_state'] # state
    zip_code = data['cu_zip'] # zip

    email = data['cu_email'] # email
    phone = data['cu_phone_primary'] # phone number

    # dictionary for ACCT form
    form_dictionary = {
        'form': 'ACCT', # form_type
        'data': [
            { 'x': 13, 'y': 147, 'w': 94, 'h': 5, 'value': vehicle_vin }, # customer name ### COORDS BELONG TO VIN
            { 'x': 109, 'y': 147, 'w': 23, 'h': 5, 'value': vehicle_year }, # vehicle year
            { 'x': 134, 'y': 147, 'w': 22, 'h': 5, 'value': vehicle_make }, # vehicle make
            { 'x': 157, 'y': 147, 'w': 22, 'h': 5, 'value': vehicle_style }, # vehicle body style
            { 'x': 180, 'y': 147, 'w': 22, 'h': 5, 'value': vehicle_model }, # vehicle model

            # { 'x': 13, 'y': 156, 'w': 22, 'h': 5, 'value': vehicle_title_no }, # vehicle title/document number
            # { 'x': 109, 'y': 156, 'w': 22, 'h': 5, 'value': vehicle_license }, # TX license plate number
            #
            #
            # { 'x': 95, 'y': 182, 'w': 22, 'h': 5, 'value': applicant_name }, # applicant name
            # { 'x': 95, 'y': 196, 'w': 22, 'h': 5, 'value': second_applicant_name }, # additional applicant name
            #
            #
            # { 'x': 177, 'y': 182, 'w': 22, 'h': 5, 'value': date }, # date above
            # { 'x': 177, 'y': 196, 'w': 22, 'h': 5, 'value': date }, # date below

            { 'x': 13, 'y': 216, 'w': 73, 'h': 5, 'value': recipient_first_name }, # receipient first name
            { 'x': 87, 'y': 216, 'w': 46, 'h': 5, 'value': recipient_middle_name }, # recipient middle name
            { 'x': 134, 'y': 216, 'w': 46, 'h': 5, 'value': recipient_last_name }, # receipient last name
            { 'x': 181, 'y': 216, 'w': 21, 'h': 5, 'value': recipient_suffix }, # receipient name suffix

            { 'x': 13, 'y': 225, 'w': 73, 'h': 5, 'value': address }, # mailing address
            { 'x': 87, 'y': 225, 'w': 80, 'h': 5, 'value': city }, # city
            { 'x': 134, 'y': 225, 'w': 46, 'h': 5, 'value': state }, # state
            { 'x': 181, 'y': 225, 'w': 22, 'h': 5, 'value': zip_code }, # zip

            { 'x': 13, 'y': 234, 'w': 22, 'h': 5, 'value': email }, # email
            { 'x': 110, 'y': 234, 'w': 22, 'h': 5, 'value': phone }, # phone number
        ]
    }


    # adds form data to overlay pdf
    for field in range(0, len(form_dictionary['data'])):
        pdf.set_xy(form_dictionary['data'][field]['x'], form_dictionary['data'][field]['y'])
        pdf.cell(form_dictionary['data'][field]['w'], form_dictionary['data'][field]['h'], form_dictionary['data'][field]['value'])

    # ready to overlay to watermark template
    pdf.output('overlay_PDF.pdf')
    pdf.close()


    ### this takes the overlay data and merges it with the watermark template
    ### WORKS
    with open('./EzForm/static/acct_background.pdf', 'rb') as pdf_template_file, open(overlay_pdf_file_name, 'rb') as overlay_PDF_file:
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
