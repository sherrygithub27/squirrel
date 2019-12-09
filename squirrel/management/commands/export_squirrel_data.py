import csv
from django.core.management.base import BaseCommand
from squirrel.models import squirrel

class Command(BaseCommand): 
    def add_arguments(self, parser): 
        parser.add_argument('args', nargs='*') 
    
    def handle(self, *args,**options): 
        meta = { 
            'file': args[0], 
            'class': squirrel, 
            'fields': ( 
                'Unique_Squirrel_ID',
		'Latitude',
		'Longitude',
		'Shift',
		'Date',
		'Age',
		'Primary_Fur_Color',
		'Location',
		'Specific_Location',
		'Running',
		'Chasing',
		'Climbing',
		'Eating',
		'Foraging',
		'Other_Activities',
		'Kuks',
		'Quaas',
		'Moans',
		'Tail_flags',
		'Tail_twitches',
		'Approaches',
		'Indifferent',
		'Runs_from',
                ) 
            }
            
        f = open(meta['file'], 'w+') 
        writer = csv.writer(f) 
        writer.writerow(meta['fields']) 
        for instance in meta['class'].objects.all(): 
            row = [getattr(instance, field) for field in meta['fields']] 
            writer.writerow(row) 
        f.close()
