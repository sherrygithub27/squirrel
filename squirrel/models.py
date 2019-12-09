from django.db import models

class squirrel(models.Model):
    Unique_Squirrel_ID = models.CharField(max_length=14,default=None,blank=True,primary_key=True)
    Longitude = models.DecimalField(max_digits=1000,decimal_places=13,default=None,null=True,blank=True)
    Latitude = models.DecimalField(max_digits=1000,decimal_places=13,default=None,null=True,blank=True)
	
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )
    Shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
        blank=True,
	null=True,
    )
	
    Date = models.CharField(max_length=20,default=0,blank=True)
	
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )
    Age = models.CharField(
        max_length=20,
        choices=AGE_CHOICES,
        blank=True,
	null=True,
    )
	
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
    )
    Primary_Fur_Color = models.CharField(
		max_length=8,
		choices=COLOR_CHOICES,
		default=None,
		blank=True,
		null=True,
	)
	
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
    )
    Location = models.CharField(
		max_length=100,
		choices=LOCATION_CHOICES,
		default=None,
		blank=True,
		null=True,
	)
	
    Specific_Location = models.CharField(max_length=100,default=None,blank=True,null=True)
    Running = models.BooleanField(default=None,blank=True,null=True)
    Chasing = models.BooleanField(default=None,blank=True,null=True)
    Climbing = models.BooleanField(default=None,blank=True,null=True)
    Eating = models.BooleanField(default=None,blank=True,null=True)
    Foraging = models.BooleanField(default=None,blank=True,null=True)
    Other_Activities = models.CharField(max_length=100,default=None,blank=True,null=True)
    Kuks = models.BooleanField(default=None,blank=True,null=True)
    Quaas = models.BooleanField(default=None,blank=True,null=True)
    Moans = models.BooleanField(default=None,blank=True,null=True)
    Tail_flags = models.BooleanField(default=None,blank=True,null=True)
    Tail_twitches = models.BooleanField(default=None,blank=True,null=True)
    Approaches = models.BooleanField(default=None,blank=True,null=True)
    Indifferent = models.BooleanField(default=None,blank=True,null=True)
    Runs_from = models.BooleanField(default=None,blank=True,null=True)
