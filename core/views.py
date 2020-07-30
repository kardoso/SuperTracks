from django.shortcuts import render
from core.models import Track, Album, Artist

# Create your views here.


def list_tracks(request):
    tracks_info = []
    tracks = Track.objects.all()
    for track in tracks:
        track_album = Album.objects.get(AlbumId=track.AlbumId)
        track_artist = Artist.objects.get(ArtistId=track_album.ArtistId)
        tracks_info.append(
            {"Name": track.Name,
             "Album": track_album.Title,
             "Artist": track_artist.Name})
    response = {'tracks': tracks_info}
    return render(request, 'track_list.html', response)
