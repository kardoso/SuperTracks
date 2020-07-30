from django.db import models

# Create your models here.


class MediaType(models.Model):
    MediaTypeId = models.IntegerField(null=False, primary_key=True)
    Name = models.CharField(max_length=120, null=True)

    class Meta:
        db_table = "MediaType"


class Genre(models.Model):
    GenreId = models.IntegerField(null=False, primary_key=True)
    Name = models.CharField(max_length=120, null=True)

    class Meta:
        db_table = "Genre"


class Artist(models.Model):
    ArtistId = models.IntegerField(null=False, primary_key=True)
    Name = models.CharField(max_length=120, null=True)

    class Meta:
        db_table = 'Artist'


class Album(models.Model):
    AlbumId = models.IntegerField(null=False, primary_key=True)
    Title = models.CharField(max_length=160, null=False)
    ArtistId = models.IntegerField(null=False)

    class Meta:
        db_table = 'Album'


class Track(models.Model):
    TrackId = models.IntegerField(null=False, primary_key=True)
    Name = models.CharField(max_length=200, null=False)
    AlbumId = models.IntegerField(null=False)
    MediaTypeId = models.IntegerField(null=False)
    GenreId = models.IntegerField(null=False)
    Composer = models.CharField(max_length=200, null=True)
    Milliseconds = models.IntegerField(null=False)
    Bytes = models.IntegerField(null=True)
    UnitPrice = models.FloatField(null=False)

    class Meta:
        db_table = 'Track'
