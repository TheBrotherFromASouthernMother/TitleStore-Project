from django.db import models

# Create your models here.
class people(models.Model):
    id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=200)
    age = models.IntegerField()
    def __str__(self):
        return self.person_name

class Customer(models.Model):
    ID_TYPES = (
        ('DRIVERS_LICENSE', 'U.S. Driver\'s License/ID Card'),
        ('MILITARY_ID', 'U.S. Military ID'),
        ('DOJ_ID', 'U.S. Citizenship & Immigration Services/DOJ ID'),
        ('NATO_ID', 'NATO ID'),
        ('DOS_ID', 'U.S. Department of State ID'),
    )
    id = models.AutoField(primary_key=True)
    cu_date_added = models.DateField(auto_now_add=True)
    cu_date_last_changed = models.DateField(auto_now=True)
    cu_first_name = models.CharField('First Name', max_length=200)
    cu_last_name = models.CharField('Last Name', max_length=200)
    cu_middle_name = models.CharField('Middle Name', max_length=200, blank=True, null = True)
    cu_suffix = models.CharField('Suffix', max_length=200, blank=True, null = True)
    cu_email = models.EmailField('Email', blank=True, null = True)
    cu_address_line_1 = models.CharField('Address Line 1', max_length=200, blank=True, null = True)
    cu_address_line_2 = models.CharField('Address Line 2', max_length=200, blank=True, null = True)
    cu_city = models.CharField('City', max_length=200, blank=True, null = True)
    cu_state = models.CharField('State', max_length=2, blank=True, null = True, default='TX')
    cu_zip = models.CharField('Zip', max_length=10, blank=True, null = True)
    cu_country = models.CharField('Country', max_length=200, blank=True, null = True, default='USA')
    cu_county = models.CharField('County', max_length=200, blank=True, null = True)
    cu_phone_primary = models.CharField('Phone', max_length=200, blank=True, null = True)
    cu_photo_id_number = models.CharField('Driver\'s License/ID Number', blank=True, null = True, max_length=8)
    cu_photo_id_type = models.CharField('ID Type', max_length=200, choices=ID_TYPES, default='DRIVERS_LICENSE', blank=True, null = True)
    cu_photo_id_state = models.CharField('ID State', max_length=2, blank=True, null = True)
    cu_flag_military = models.NullBooleanField('Are you military personel stationed in Texas?', blank=True, null = True)

    def __str__(self):
        return self.cu_first_name + ' ' + self.cu_last_name

class Vehicle(models.Model):
    NO_PLATES_FLAGS = (
        ('HAS_PLATES', 'License plates and registration issued for this vehicle are being surrendered. The registration for this vehicle is not currently suspended or revoked.'),
        ('NO_PLATES', 'Vehicle has no license plates and/or registration.'),
        ('MIL_PLATES', 'Vehicle has been issued a license plate under the applicable status of forces agreement.'),
    )
    id = models.AutoField(primary_key=True)
    v_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    v_date_added = models.DateField(auto_now_add=True)
    v_date_last_changed = models.DateField(auto_now=True)
    v_vin = models.CharField('Vehicle Identification Number', max_length=17, null = True)
    v_year = models.DecimalField('Year', max_digits=4, decimal_places=0, blank=True, null = True)
    v_make = models.CharField('Make', max_length=200, blank=True, null = True)
    v_body_style = models.CharField('Body Style', max_length=200, blank=True, null = True)
    v_model = models.CharField('Model', max_length=200, blank=True, null = True)
    v_purchased_from_name = models.CharField('Seller Name', max_length=200, blank=True, null = True)
    v_purchased_from_city = models.CharField('City Purchased From', max_length=200, blank=True, null = True)
    v_purchased_from_state = models.CharField('State Purchased From', max_length=200, blank=True, null = True)
    v_odometer_reading = models.IntegerField('Odometer Reading', blank=True, null = True)
    v_purchase_date = models.DateField('Purchase Date', blank=True, null = True)
    v_purchase_price_usd = models.DecimalField('Purchase Price (USD)', max_digits=20, decimal_places=2, blank=True, null = True)
    v_plate_number = models.CharField('License Plate Number', max_length=8, blank=True, null = True)
    v_empty_weight = models.IntegerField('Empty Weight', blank=True, null = True)
    v_lienholder_name_first = models.CharField('Lienholder Name (First)', max_length=200, default='N/A', blank=True, null = True)
    v_seller_signature = models.CharField('Seller Signature', max_length=200, default='UNAVAILABLE', blank=True, null = True)
    v_bond_request_explanation = models.TextField('Provide an explanation for requesting a bonded title or tax assessor-collector hearing.', blank=True, null = True)
    v_flag_last_titled_in_tx = models.NullBooleanField('Was the vehicle last titled in Texas?', blank=True, null = True)
    v_flag_abandoned = models.NullBooleanField('Is the vehicle an abandoned vehicle?', blank=True, null = True)
    v_flag_subject_to_charges = models.NullBooleanField('Is the vehicle subject to storage or mechanic\'s charges?', blank=True, null = True)
    v_flag_subject_to_lien = models.NullBooleanField('Is the vehicle subject to any type of foreclosure lien?', blank=True, null = True)
    v_flag_nonrepairable = models.NullBooleanField('Is the vehicle a nonrepairable vehicle?', blank=True, null = True)
    v_flag_salvage = models.NullBooleanField('Is the vehicle a salvage vehicle?', blank=True, null = True)
    v_flag_pending_lawsuits = models.NullBooleanField('Is the vehicle involved in any pending lawsuits or disputes of ownership?', blank=True, null = True)
    v_flag_legal_posession = models.NullBooleanField('Are you in legal possession of the vehicle?', blank=True, null = True)
    v_flag_legal_control = models.NullBooleanField('Are you in legal control of the vehicle?', blank=True, null = True)
    v_flag_manufactured_us = models.NullBooleanField('Was the vehicle manufactured for sale or distribution in the United States by a motor vehicle manufacturer?', blank=True, null = True)
    v_flag_assembled = models.NullBooleanField('Is the vehicle an assembled vehicle from new or used part(s) or a kit that has not been previously titled?', blank=True, null = True)
    v_flag_complete = models.NullBooleanField('Is the vehicle complete?', blank=True, null = True)
    v_flag_25_or_older = models.NullBooleanField('Is the vehicle 25 or more years old?', blank=True, null = True)
    v_flag_no_plates = models.CharField('Please select one:', max_length=200, choices=NO_PLATES_FLAGS, blank=True, null = True)

    def __str__(self):
        return self.v_vin