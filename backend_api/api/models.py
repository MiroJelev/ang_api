# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Borders(models.Model):
    pk = models.CompositePrimaryKey('country1', 'country2')
    country1 = models.CharField(db_column='Country1', max_length=4)  # Field name made lowercase.
    country2 = models.CharField(db_column='Country2', max_length=4)  # Field name made lowercase.
    length = models.FloatField(db_column='Length', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'borders'
        unique_together = (('country1', 'country2'),)


class City(models.Model):
    pk = models.CompositePrimaryKey('name', 'country', 'province')
    name = models.CharField(db_column='Name', max_length=35)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'
        unique_together = (('name', 'country', 'province'),)


class Continent(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=20)  # Field name made lowercase.
    area = models.FloatField(db_column='Area', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'continent'


class Country(models.Model):
    name = models.CharField(db_column='Name', unique=True, max_length=35)  # Field name made lowercase.
    code = models.CharField(db_column='Code', primary_key=True, max_length=4)  # Field name made lowercase.
    capital = models.CharField(db_column='Capital', max_length=35, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35, blank=True, null=True)  # Field name made lowercase.
    area = models.FloatField(db_column='Area', blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
    politics = models.ForeignKey(to='Politics', db_column='code', to_field="country", related_name='+', on_delete=models.DO_NOTHING)
    continents = models.ForeignKey(to='Encompasses', db_column='code', to_field="country", related_name='+', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'country'


class Desert(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=35)  # Field name made lowercase.
    area = models.FloatField(db_column='Area', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'desert'


class Economy(models.Model):
    country = models.CharField(db_column='Country', primary_key=True, max_length=4)  # Field name made lowercase.
    gdp = models.FloatField(db_column='GDP', blank=True, null=True)  # Field name made lowercase.
    agriculture = models.FloatField(db_column='Agriculture', blank=True, null=True)  # Field name made lowercase.
    service = models.FloatField(db_column='Service', blank=True, null=True)  # Field name made lowercase.
    industry = models.FloatField(db_column='Industry', blank=True, null=True)  # Field name made lowercase.
    inflation = models.FloatField(db_column='Inflation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'economy'


class Encompasses(models.Model):
    pk = models.CompositePrimaryKey('country', 'continent')
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    continent = models.CharField(db_column='Continent', max_length=20)  # Field name made lowercase.
    percentage = models.FloatField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'encompasses'
        unique_together = (('country', 'continent'),)


class Ethnicgroup(models.Model):
    pk = models.CompositePrimaryKey('name', 'country')
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    percentage = models.FloatField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ethnicGroup'
        unique_together = (('name', 'country'),)


class GeoDesert(models.Model):
    pk = models.CompositePrimaryKey('province', 'country', 'desert')
    desert = models.CharField(db_column='Desert', max_length=35)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geo_desert'
        unique_together = (('province', 'country', 'desert'),)


class GeoEstuary(models.Model):
    pk = models.CompositePrimaryKey('province', 'country', 'river')
    river = models.CharField(db_column='River', max_length=35)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geo_estuary'
        unique_together = (('province', 'country', 'river'),)


class GeoIsland(models.Model):
    pk = models.CompositePrimaryKey('province', 'country', 'island')
    island = models.CharField(db_column='Island', max_length=35)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geo_island'
        unique_together = (('province', 'country', 'island'),)


class GeoLake(models.Model):
    pk = models.CompositePrimaryKey('province', 'country', 'lake')
    lake = models.CharField(db_column='Lake', max_length=35)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geo_lake'
        unique_together = (('province', 'country', 'lake'),)


class GeoMountain(models.Model):
    pk = models.CompositePrimaryKey('province', 'country', 'mountain')
    mountain = models.CharField(db_column='Mountain', max_length=35)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geo_mountain'
        unique_together = (('province', 'country', 'mountain'),)


class GeoRiver(models.Model):
    pk = models.CompositePrimaryKey('province', 'country', 'river')
    river = models.CharField(db_column='River', max_length=35)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geo_river'
        unique_together = (('province', 'country', 'river'),)


class GeoSea(models.Model):
    pk = models.CompositePrimaryKey('province', 'country', 'sea')
    sea = models.CharField(db_column='Sea', max_length=35)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geo_sea'
        unique_together = (('province', 'country', 'sea'),)


class GeoSource(models.Model):
    pk = models.CompositePrimaryKey('province', 'country', 'river')
    river = models.CharField(db_column='River', max_length=35)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geo_source'
        unique_together = (('province', 'country', 'river'),)


class Ismember(models.Model):
    pk = models.CompositePrimaryKey('country', 'organization')
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    organization = models.CharField(db_column='Organization', max_length=12)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=35, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'isMember'
        unique_together = (('country', 'organization'),)


class Island(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=35)  # Field name made lowercase.
    islands = models.CharField(db_column='Islands', max_length=35, blank=True, null=True)  # Field name made lowercase.
    area = models.FloatField(db_column='Area', blank=True, null=True)  # Field name made lowercase.
    height = models.FloatField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'island'


class Islandin(models.Model):
    island = models.CharField(db_column='Island', max_length=35, blank=True, null=True)  # Field name made lowercase.
    sea = models.CharField(db_column='Sea', max_length=35, blank=True, null=True)  # Field name made lowercase.
    lake = models.CharField(db_column='Lake', max_length=35, blank=True, null=True)  # Field name made lowercase.
    river = models.CharField(db_column='River', max_length=35, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'islandIn'


class Lake(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=35)  # Field name made lowercase.
    area = models.FloatField(db_column='Area', blank=True, null=True)  # Field name made lowercase.
    depth = models.FloatField(db_column='Depth', blank=True, null=True)  # Field name made lowercase.
    altitude = models.FloatField(db_column='Altitude', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    river = models.CharField(db_column='River', max_length=35, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lake'


class Language(models.Model):
    pk = models.CompositePrimaryKey('name', 'country')
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    percentage = models.FloatField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'language'
        unique_together = (('name', 'country'),)


class Located(models.Model):
    city = models.CharField(db_column='City', max_length=35, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4, blank=True, null=True)  # Field name made lowercase.
    river = models.CharField(db_column='River', max_length=35, blank=True, null=True)  # Field name made lowercase.
    lake = models.CharField(db_column='Lake', max_length=35, blank=True, null=True)  # Field name made lowercase.
    sea = models.CharField(db_column='Sea', max_length=35, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'located'


class Locatedon(models.Model):
    pk = models.CompositePrimaryKey('city', 'province', 'country', 'island')
    city = models.CharField(db_column='City', max_length=35)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    island = models.CharField(db_column='Island', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'locatedOn'
        unique_together = (('city', 'province', 'country', 'island'),)


class Mergeswith(models.Model):
    pk = models.CompositePrimaryKey('sea1', 'sea2')
    sea1 = models.CharField(db_column='Sea1', max_length=35)  # Field name made lowercase.
    sea2 = models.CharField(db_column='Sea2', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mergesWith'
        unique_together = (('sea1', 'sea2'),)


class Mountain(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=35)  # Field name made lowercase.
    mountains = models.CharField(db_column='Mountains', max_length=35, blank=True, null=True)  # Field name made lowercase.
    height = models.FloatField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mountain'


class Mountainonisland(models.Model):
    pk = models.CompositePrimaryKey('mountain', 'island')
    mountain = models.CharField(db_column='Mountain', max_length=35)  # Field name made lowercase.
    island = models.CharField(db_column='Island', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mountainOnIsland'
        unique_together = (('mountain', 'island'),)


class Organization(models.Model):
    abbreviation = models.CharField(db_column='Abbreviation', primary_key=True, max_length=12)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=80)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=35, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=35, blank=True, null=True)  # Field name made lowercase.
    established = models.DateField(db_column='Established', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organization'


class Politics(models.Model):
    country = models.CharField(db_column='Country', primary_key=True, max_length=4)  # Field name made lowercase.
    independence = models.DateField(db_column='Independence', blank=True, null=True)  # Field name made lowercase.
    dependent = models.CharField(db_column='Dependent', max_length=4, blank=True, null=True)  # Field name made lowercase.
    government = models.CharField(db_column='Government', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'politics'


class Population(models.Model):
    country = models.CharField(db_column='Country', primary_key=True, max_length=4)  # Field name made lowercase.
    population_growth = models.FloatField(db_column='Population_Growth', blank=True, null=True)  # Field name made lowercase.
    infant_mortality = models.FloatField(db_column='Infant_Mortality', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'population'


class Province(models.Model):
    pk = models.CompositePrimaryKey('name', 'country')
    name = models.CharField(db_column='Name', max_length=35)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
    area = models.FloatField(db_column='Area', blank=True, null=True)  # Field name made lowercase.
    capital = models.CharField(db_column='Capital', max_length=35, blank=True, null=True)  # Field name made lowercase.
    capprov = models.CharField(db_column='CapProv', max_length=35, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'province'
        unique_together = (('name', 'country'),)


class Religion(models.Model):
    pk = models.CompositePrimaryKey('name', 'country')
    country = models.CharField(db_column='Country', max_length=4)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    percentage = models.FloatField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'religion'
        unique_together = (('name', 'country'),)


class River(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=35)  # Field name made lowercase.
    river = models.CharField(db_column='River', max_length=35, blank=True, null=True)  # Field name made lowercase.
    lake = models.CharField(db_column='Lake', max_length=35, blank=True, null=True)  # Field name made lowercase.
    sea = models.CharField(db_column='Sea', max_length=35, blank=True, null=True)  # Field name made lowercase.
    length = models.FloatField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    sourcelongitude = models.FloatField(db_column='SourceLongitude', blank=True, null=True)  # Field name made lowercase.
    sourcelatitude = models.FloatField(db_column='SourceLatitude', blank=True, null=True)  # Field name made lowercase.
    mountains = models.CharField(db_column='Mountains', max_length=35, blank=True, null=True)  # Field name made lowercase.
    sourcealtitude = models.FloatField(db_column='SourceAltitude', blank=True, null=True)  # Field name made lowercase.
    estuarylongitude = models.FloatField(db_column='EstuaryLongitude', blank=True, null=True)  # Field name made lowercase.
    estuarylatitude = models.FloatField(db_column='EstuaryLatitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'river'


class Sea(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=35)  # Field name made lowercase.
    depth = models.FloatField(db_column='Depth', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sea'
