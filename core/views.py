from django.shortcuts import render, redirect
from django import forms
from core.models import Track, Album, Artist
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def list_tracks(request):
    tracks_info = []
    tracks = Track.objects.all()
    for track in tracks:
        track_album = Album.objects.get(AlbumId=track.AlbumId)
        track_artist = Artist.objects.get(ArtistId=track_album.ArtistId)
        tracks_info.append(
            {"Id": track.TrackId,
             "Name": track.Name,
             "Album": track_album.Title,
             "Artist": track_artist.Name})
    response = {'tracks': tracks_info}
    return render(request, 'track_list.html', response)


class EditNameForm(forms.Form):
    track_name = forms.CharField(
        label='Track Name', max_length=200)


@csrf_exempt
def edit_track(request, track_id):
    if request.method == "POST":
        form = EditNameForm(request.POST)
        if form.is_valid():
            track = Track.objects.get(TrackId=track_id)
            track.Name = form.cleaned_data['track_name']
            track.save()
            return redirect('/')
    else:
        track = Track.objects.get(TrackId=track_id)
        form = EditNameForm(initial={'track_name': track.Name})
        return render(request, 'track_edit.html', {'form': form, 'track_name': track.Name, 'track_id': track_id})
