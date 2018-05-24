
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect,  HttpRequest

from django.template import loader

from django.shortcuts import get_object_or_404, render
from .models import Customer, Vehicle, AcctForm

from django.db import models
from django.views.generic.edit import CreateView, DeleteView, UpdateView

import json

from .acct_form_filler import makePdf as acct_pdf_maker

# dashboard view
def index(request):
    return render(request, 'EzForm/index.html')

# customer list view
def customers(request):
    all_customers = Customer.objects.order_by('cu_last_name')
    context = {'customer_list' : all_customers }
    return render(request, 'EzForm/customers.html', context)

# vehicle list view
def vehicles(request):
    all_vehicles = Vehicle.objects.order_by('Customer')
    context = {'vehicle_list' : all_vehicles }
    return render(request, 'EzForm/vehicles.html', context)



def customer_review(request):
    if request.method == 'GET':
        template = loader.get_template('EzForm/formReview.html')
        context = {
            'customers': []
        }
        customers_on_file = Customer.objects.filter()
        for customer in customers_on_file:
            context['customers'].append(customer.cu_last_name + ', ' + customer.cu_first_name)

        return HttpResponse(template.render(context, request))

def forms(request):
    return render(request, 'EzForm/forms.html')

def customer_info_to_review(request, cu_name):
    cumstomer_query = cu_name.split(', ')
    # print(cumstomer_query[0])
    cu_last_name = cumstomer_query[0]
    cu_first_name = cumstomer_query[1]
    customers_on_file = Customer.objects.get(cu_last_name=cu_last_name, cu_first_name=cu_first_name)
    # print(customers_on_file.__dict__)
    customer_file = customers_on_file.__dict__
    dataToSendToClient = {}
    for key in customer_file:
        if key != '_state':
            dataToSendToClient[key] = customer_file[key]
    # print(dataToSendToClient)
    response = JsonResponse(dataToSendToClient)
    return response



class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = '/customers/'

class CustomerDelete(DeleteView):
    model = Customer
    success_url = '/customers/'

class CustomerUpdate(UpdateView):
    model = Customer
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/customers/'

class VehicleCreate(CreateView):
    model = Vehicle
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = '/vehicles/'

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = '/vehicles/'

class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/vehicles/'

class AcctFormCreate(CreateView):
    model = AcctForm
    fields = '__all__'
    template_name_suffix = '_create_form'

class AcctFormDelete(DeleteView):
    model = AcctForm
    success_url = 'index' # check for correct url

class AcctFormUpdate(UpdateView):
    model = AcctForm
    fields = '__all__'
    template_name_suffix = '_update_form'

def makeAcctPdf(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        c_id = body['id']
        # print(type(c_id))
        # c_id = int(c_id)
        #TODO: redirect user to PDF page
        # acct_form_filler.makePdf(data=body)
        acct_pdf_maker(data=body) # sends POST data to make pdf
        
    # try:
        #TODO: save to DB, and
        acct_form = AcctForm(**body)
        acct_form.save()
        customer = Customer.objects.filter(id=c_id).update(**body)

        print(customer)


    # pdf should be already made when this is called
    def pdf_view(request):
        try:
            return FileResponse(open('result_form.pdf', 'rb'), content_type='application/pdf')
        except FileNotFoundError:
            raise Http404()

    return pdf_view(request)
    # except:
    #     print('no record found')
    # return JsonResponse({'greet': 'G\'day mate'})
