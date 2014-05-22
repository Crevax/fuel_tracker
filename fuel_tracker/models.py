from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    owner           = models.ForeignKey(User)
    nickname        = models.CharField(max_length=50)
    make            = models.CharField(max_length=50)
    model           = models.CharField(max_length=50)
    year            = models.CharField(max_length=4)
    base_miles      = models.DecimalField(decimal_places=1, max_digits=7)
    #fueling_history = models.OneToManyField(FuelUp)

    def __unicode__(self):
        return "%s's %s" % (self.owner, self.nickname)

class GasCompany(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    #locations   = models.OneToManyField(GasStation)

    def __unicode__(self):
        return self.name

class GasStation(models.Model):
    company         = models.ForeignKey(GasCompany)
    street_address  = models.CharField(max_length=100)
    city            = models.CharField(max_length=100)
    state           = models.CharField(max_length=50)
    zipcode         = models.CharField(max_length=5)
    #fueling_history = models.OneToManyField(FuelUp)

    def __unicode__(self):
        return "%s on %s in %s, %s %s" % (self.company, self.street_address, self.city, self.state, self.zipcode)

class FuelUp(models.Model):
    station             = models.ForeignKey(GasStation)
    vehicle             = models.ForeignKey(Vehicle)
    gas_type            = models.CharField(max_length=50, default='Regular Unleaded')
    price_per_gallon    = models.DecimalField(decimal_places=3, max_digits=4)
    amount              = models.DecimalField(decimal_places=3, max_digits=5)
    miles_traveled      = models.DecimalField(decimal_places=1, max_digits=4)
    complete_fill       = models.BooleanField(default=True)
    date                = models.DateField()

    @property
    def cost(self):
        return self.price_per_gallon * self.amount

    @property
    def mpg(self):
        if( (self.miles_traveled / self.amount) == 0 or self.complete_fill == False ):
            return 'N/A'
        else:
            return self.miles_traveled / self.amount

    def __unicode__(self):
        return "%s at %s on %s" % (self.vehicle, self.station, self.date)

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def __unicode__(self):
        return self.user.username