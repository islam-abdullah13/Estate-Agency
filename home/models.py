from django.db import models
from django.utils.text import slugify

# Create your models here.

Governorates=[
    ('New Valley', 'New Valley'),
    ('Matruh', 'Matruh'),
    ('Red Sea', 'Red Sea'),
    ('Giza', 'Giza'),
    ('South Sinai', 'South Sinai'),
    ('North Sinai', 'North Sinai'),
    ('Suez', 'Suez'),
    ('Beheira', 'Beheira'),
    ('Helwan', 'Helwan'),
    ('Sharqia', 'Sharqia'),
    ('Dakahlia', 'Dakahlia'),
    ('Kafr el-Sheikh', 'Kafr el-Sheikh'),
    ('Alexandria', 'Alexandria'),
    ('Monufia', 'Monufia'),
    ('Minya', 'Minya'),
    ('Gharbia', 'Gharbia'),
    ('Faiyum', 'Faiyum'),
    ('Qena', 'Qena'),
    ('Asyut', 'Asyut'),
    ('Sohag', 'Sohag'),
    ('Ismailia', 'Ismailia'),
    ('Beni Suef', 'Beni Suef'),
    ('Qalyubia', 'Qalyubia'),
    ('Aswan', 'Aswan'),
    ('Damietta', 'Damietta'),
    ('Cairo', 'Cairo'),
    ('Port Said', 'Port Said'),
    ('Luxor', 'Luxor'),
    ('6th of October', '6th of October'),
    
]
State_Of_Estate=[
    ('Sale', 'Sale'),
    ('Rent', 'Rent'), 
]
Type_Of_Estate=[
    ('House', 'House'),
    ('Land', 'Land'),
    ('Apartment', 'Apartment'), 
    ('Villa', 'Villa'),  
]
class Estate(models.Model):
    tittle = models.CharField(max_length=100)
    estate_type = models.CharField(max_length=100,choices=Type_Of_Estate)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=100,choices=Governorates)
    published_at=models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=100,choices=State_Of_Estate)
    area =models.IntegerField(default="100")
    bed =models.IntegerField(default="2")
    room =models.IntegerField(default="2")
    bath =models.IntegerField(default="1")
    garag=models.IntegerField(default="0")
    image =models.ImageField(upload_to='estates/')
    price = models.IntegerField(default="10000")
    slug = models.SlugField(blank=True,null=True)

    def save (self,*args, **kwargs):
        self.slug=slugify(self.tittle)
        super(Estate,self).save(*args, **kwargs)


    def __str__(self):
        return self.tittle

class Amenities(models.Model):
    pass