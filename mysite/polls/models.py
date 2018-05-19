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


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='Nancy')

    def __str__(self):
        return self.name