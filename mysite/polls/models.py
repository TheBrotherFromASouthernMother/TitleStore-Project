from django.db import models

# Create your models here.
class people(models.Model):
    id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=200)
    age = models.IntegerField()
    def __str__(self):
        return self.person_name

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    cu_date_added = models.DateField(auto_now_add=True)
    cu_date_last_changed = models.DateField(auto_now=True)
    cu_first_name = models.CharField(max_length=200)
    cu_last_name = models.CharField(max_length=200)
    cu_middle_name = models.CharField(max_length=200, null = True)
    cu_suffix = models.CharField(max_length=200, null = True)
    cu_email = models.EmailField(null = True)
    cu_address_line_1 = models.CharField(max_length=200, null = True)
    cu_address_line_2 = models.CharField(max_length=200, null = True)
    cu_city = models.CharField(max_length=200, null = True)
    cu_state = models.CharField(max_length=2, null = True)
    cu_zip = models.CharField(max_length=10, null = True)
    cu_country = models.CharField(max_length=200, null = True)
    cu_county = models.CharField(max_length=200, null = True)
    cu_phone_primary = models.CharField(max_length=200, null = True)
    cu_photo_id_number = models.IntegerField(null = True)
    cu_photo_id_state = models.CharField(max_length=2, null = True)
    cu_flag_military = models.NullBooleanField(null = True)

    def __str__(self):
        return self.cu_first_name + self.cu_last_name

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    v_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    v_date_added = models.DateField(auto_now_add=True)
    v_date_last_changed = models.DateField(auto_now=True)
    v_vin = models.CharField(max_length=200, null = True)
    v_year = models.IntegerField(max_length=4, null = True)
    v_make = models.CharField(max_length=200, null = True)
    v_body_style = models.CharField(max_length=200, null = True)
    v_model = models.CharField(max_length=200, null = True)
    v_purchased_from_name = models.CharField(max_length=200, null = True)
    v_purchased_from_city = models.CharField(max_length=200, null = True)
    v_purchased_from_state = models.CharField(max_length=200, null = True)
    v_odometer_reading = models.IntegerField(null = True)
    v_purchase_date = models.DateField(null = True)
    v_purchase_price_usd = models.DecimalField(max_digits=20, decimal_places=2, null = True)
    v_plate_number = models.CharField(max_length=200, null = True)
    v_empty_weight = models.IntegerField(null = True)
    v_lienholder_name_first = models.CharField(max_length=200, default='N/A', null = True)
    v_seller_signature = models.CharField(max_length=200, default='UNAVAILABLE', null = True)
    v_bond_request_explanation = models.TextField(null = True)
    v_flag_last_titled_in_tx = models.NullBooleanField(null = True)
    v_flag_abandoned = models.NullBooleanField(null = True)
    v_flag_subject_to_charges = models.NullBooleanField(null = True)
    v_flag_subject_to_lien = models.NullBooleanField(null = True)
    v_flag_nonrepairable = models.NullBooleanField(null = True)
    v_flag_salvage = models.NullBooleanField(null = True)
    v_flag_pending_lawsuits = models.NullBooleanField(null = True)
    v_flag_legal_posession = models.NullBooleanField(null = True)
    v_flag_legal_control = models.NullBooleanField(null = True)
    v_flag_manufactured_us = models.NullBooleanField(null = True)
    v_flag_assembled = models.NullBooleanField(null = True)
    v_flag_complete = models.NullBooleanField(null = True)
    v_flag_25_or_older = models.NullBooleanField(null = True)
    v_flag_no_plates = models.NullBooleanField(null = True)

    def __str__(self):
        return self.v_vin