from django.db import models

# Create your models here.

class ZipCode(models.Model):
    zip = models.CharField(max_length=20)

class City(models.Model):
    name = models.CharField(max_length=100)

class NewBusiness(models.Model):
ENTITY_TYPE = (
    'Assumed biz name',    'Assumed business name',
    'Co-op',               'Cooperative',
    'Dmtc biz corp',       'Dmtcestic business corporation',
    'Dmtc llco',           'Dmtcestic limited liability company',
    'Dmtc llp',            'Dmtcestic limited partnership',
    'Dmtc nonprofit corp', 'Dmtcestic nonprofit corporation',
    'Dmtc pro corp',       'Dmtcestic professional corporation',
    'Dmtc reg llp',        'Dmtcestic registered limited liability partnership',
    'Fgn biz corp',        'Foreign business corporation',
    'Fgn biz trust',       'Foreign business trust',
    'Fgn llco',            'Foreign limited liability company',
    'Fgn llp',             'Foreign limited partnership',
    'Fgn nonprofit corp',  'Foreign nonprofit corporation',
    'Fgn pro corp',        'Foreign professional corporation',
    'Fgn reg llp',         'Foreign registered limited liability partnership',
)

ASSOCIATED_NAME_TYPE = (
    'auth_rep',  'Authorized representative',
    'mail_add',  'Mailing address',
    'reg_agent', 'Registered agent',
)

    registry = models.IntegerField()
    name = models.CharField(max_length=200)
    entity_type = models.CharField(max_length=35, choices=ENTITY_TYPE)
    registry_date = models.DateField()
    assoc_name_type = models.CharField(max_length=20, choices=ASSOCIATED_NAME_TYPE)
    first_name = models.CharField(max_length=110)
    middle_name = models.CharField(max_length=115)
    last_name = models.CharField(max_length=120)
    suffix = models.CharField(max_length=50)
    not_of_record_entity = models.CharField(max_length=85)
    entity_of_record_reg_no = models.IntegerField()
    entity_of_record_name = models.CharField(max_length=125)
    address = models.CharField(max_length=260)
    address_continued = models.CharField(max_length=255)
    city = models.ForeignKey(City)
    state = models.CharField(max_length=105)
    zip_code = models.ForeignKey(ZipCode)
