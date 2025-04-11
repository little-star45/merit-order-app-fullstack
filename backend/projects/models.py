from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser

class Project(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="project")

    #power plant capacity per technology
    cap_solar = models.FloatField(default=0)
    cap_coal = models.FloatField(default=0)
    cap_solar = models.FloatField(default=0)
    cap_nuclear = models.FloatField(default=0)
    cap_wind = models.FloatField(default=0)
    cap_brown_coal = models.FloatField(default=0)
    cap_n_gas = models.FloatField(default=0)
    cap_hydro = models.FloatField(default=0)
    cap_biofuel = models.FloatField(default=0)

    #price per WWh per technologycap_solar = models.FloatField(default=0)
    price_coal = models.FloatField(default=0)
    price_solar = models.FloatField(default=0)
    price_nuclear = models.FloatField(default=0)
    price_wind = models.FloatField(default=0)
    price_brown_coal = models.FloatField(default=0)
    price_n_gas = models.FloatField(default=0)
    price_hydro = models.FloatField(default=0)
    price_biofuel = models.FloatField(default=0)

    #co2 emmision per technology
    em_solar = models.FloatField(default=0)
    em_coal = models.FloatField(default=0)
    em_solar = models.FloatField(default=0)
    em_nuclear = models.FloatField(default=0)
    em_wind = models.FloatField(default=0)
    em_brown_coal = models.FloatField(default=0)
    em_n_gas = models.FloatField(default=0)
    em_hydro = models.FloatField(default=0)
    em_biofuel = models.FloatField(default=0)

    #power plant efficency per technology
    eff_solar = models.FloatField(default=100)
    eff_wind = models.FloatField(default=100)
    eff_hydro = models.FloatField(default=100)
    eff_coal = models.FloatField(default=46)
    eff_gas = models.FloatField(default=58)
    eff_bcoal = models.FloatField(default=44)
    eff_nuclear = models.FloatField(default=36)
    eff_biofuel = models.FloatField(default=85)

    #wo - wartosc opalowa
    wo_coal= models.FloatField(default=21.27)
    wo_brown_coal= models.FloatField(default=85)
    wo_n_gas= models.FloatField(default=48)
    wo_ch4_n_gas=models.FloatField(default=36.65)
    we_coal = models.FloatField(default=93.54)
    we_b_coal= models.FloatField(default=111.53)
    we_n_gas= models.FloatField(default=55.48)

    co2_price =  models.FloatField(default=80.24)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'], name='unique_project_per_user')
        ]

    def __str__(self):
        return f'{self.title} - {self.author}'