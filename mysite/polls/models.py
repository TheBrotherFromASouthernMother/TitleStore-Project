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
    cu_middle_name = models.CharField(max_length=200)
    cu_suffix = models.CharField(max_length=200)
    cu_email = models.EmailField()
    cu_address_line_1 = models.CharField(max_length=200)
    cu_address_line_2 = models.CharField(max_length=200)
    cu_city = models.CharField(max_length=200)
    cu_state = models.CharField(max_length=2)
    cu_zip = models.CharField(max_length=10)
    cu_country = models.CharField(max_length=200)
    cu_county = models.CharField(max_length=200)
    cu_phone_primary = models.CharField(max_length=200)
    cu_photo_id_number = models.IntegerField()
    cu_photo_id_state = models.CharField(max_length=2)
    cu_flag_military = models.BooleanField()

    def __str__(self):
        return self.cu_first_name + self.cu_last_name

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    v_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    v_date_added = models.DateField(auto_now_add=True)
    v_date_last_changed = models.DateField(auto_now=True)
    v_vin = models.CharField(max_length=200)
    v_year = models.IntegerField(max_length=4)
    v_make = models.CharField(max_length=200)
    v_body_style = models.CharField(max_length=200)
    v_model = models.CharField(max_length=200)
    v_purchased_from_name = models.CharField(max_length=200)
    v_purchased_from_city = models.CharField(max_length=200)
    v_purchased_from_state = models.CharField(max_length=200)
    v_odometer_reading = models.IntegerField()
    v_purchase_date = models.DateField()
    v_purchase_price_usd = models.DecimalField(max_digits=20, decimal_places=2)
    v_plate_number = models.CharField(max_length=200)
    v_empty_weight = models.IntegerField()
    v_lienholder_name_first = models.CharField(max_length=200, default='N/A')
    v_seller_signature = models.CharField(max_length=200, default='UNAVAILABLE')
    v_bond_request_explanation = models.TextField()
    v_flag_last_titled_in_tx = models.BooleanField()
    v_flag_abandoned = models.BooleanField()
    v_flag_subject_to_charges = models.BooleanField()
    v_flag_subject_to_lien = models.BooleanField()
    v_flag_nonrepairable = models.BooleanField()
    v_flag_salvage = models.BooleanField()
    v_flag_pending_lawsuits = models.BooleanField()
    v_flag_legal_posession = models.BooleanField()
    v_flag_legal_control = models.BooleanField()
    v_flag_manufactured_us = models.BooleanField()
    v_flag_assembled = models.BooleanField()
    v_flag_complete = models.BooleanField()
    v_flag_25_or_older = models.BooleanField()
    v_flag_no_plates = models.BooleanField()

    def __str__(self):
        return self.v_vin