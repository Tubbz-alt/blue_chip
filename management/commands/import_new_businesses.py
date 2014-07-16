import pprint
import csv
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from blue_chip.models import NewBusiness, City, ZipCode

class Command(BaseCommand):
    help = 'Import new business info from Oregon Secretary of State data dump file. Expects a .csv file.'
    
    def handle(self, *args, **options):
        if len(args) == 1:
            print args
            reader = csv.DictReader(open(args[0]))
            
            '''
            col  col name
            ===  ========
            0    Registry Number
            1    Business Name
            2    Entity Type
            3    Registry Date
            4    Associated Name Type
            5    First Name
            6    Middle Name
            7    Last Name
            8    Suffix
            9    Not of Record Entity
            10   Entity of Record Req Number
            11   Entity of Record Name
            12   Address
            13   Address Continued
            14   City
            15   State
            16   Zip Code
            '''
            for row in reader:
                pprint.pprint(row)
                city_obj, city_created = City.objects.get_or_create(name=row['City'])
                
                zip_obj, zip_created = ZipCode.objects.get_or_create(zip=row['Zip Code'])
                
                try:
                    biz_obj, biz_created = NewBusiness.objects.get_or_create(registry=row['Registry Number'],
                         defaults={
                             'name': row['Business Name'],
                             'entity_type': row['Entity Type'],
                             'registry_date': datetime.strptime(row['Registry Date'], '%m/%d/%Y'), # convert into date from string
                             'assoc_name_type': row['Associated Name Type'],
                             'first_name': row['First Name'],
                             'middle_name': row['Middle Name'],
                             'last_name': row['Last Name'],
                             'suffix': row['Suffix'],
                             'not_of_record_entity': row['Not of Record Entity'],
                             'entity_of_record_reg_no': row['Entity of Record Reg Number'],
                             'entity_of_record_name': row['Entity of Record Name'],
                             'address': row['Address '], # Yes, it has a space at the end ... 
                             'address_continued': row['Address Continued'],
                             'city': city_obj,
                             'state': row['State'],
                             'zip_code': zip_obj,
                         }
                    )
                except ValueError, err:
                    print '\nThe Python error:', err
                    print "Here's the problem:"
                    pprint.pprint(row)
                    print 'zip_obj:', zip_obj
                    print 'city_obj:'   , city_obj
                    return
        else:
            print 'You need to supply the path to a .csv file.'
