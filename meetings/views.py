from django.shortcuts import render, redirect , get_object_or_404, redirect
import meetings  # Added redirect
from meetings.models import Meeting, Room
from .forms import MeetingForm  


def meetings_list_view(request):
    meetings = Meeting.objects.all()  # Get all meetings
    return render(request, 'meetings/meetings.html', {'meetings': meetings})

def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/details.html", {"meeting": meeting})

def rooms_list_view(request):
    rooms = Room.objects.all()  # Get all rooms
    return render(request, 'meetings/rooms.html', {'rooms': rooms})

def detail_room(request, id):
    room = Room.objects.get(pk=id)
    return render(request, "meetings/room_details.html", {"room": room})

def add_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the meeting if the form is valid
            return redirect('meetings_list_view')  # Redirect to the meetings list
    else:
        form = MeetingForm()

    return render(request, 'meetings/new.html', {'form': form})

#******************************************
# def delete_meeting(request, id):
#     meeting = get_object_or_404(Meeting, id=id)
#     if request.method == "POST":
#         meeting.delete()  # Delete the meeting
#         return redirect('meetings_list_view')  # Redirect to the meetings list after deletion

#     return render(request, 'meetings/confirm_delete.html', {'meeting': meeting})  # Render a confirmation template



def delete_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id)
    
    if request.method == "POST":
        meeting.delete() # Redirige vers la vue des réunions après suppression
        return redirect('meetings_list_view')
    
    return render(request, 'meetings/confirm_delete.html', {'meeting': meeting})
 

def update_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id)  # Récupérer la réunion par ID
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)  # Passer l'instance à mettre à jour
        if form.is_valid():
            form.save()  # Sauvegarder les modifications
            return redirect('meetings_list_view')  # Rediriger vers la liste des réunions
    else:
        form = MeetingForm(instance=meeting)  # Remplir le formulaire avec les données existantes

    return render(request, 'meetings/update_meeting.html', {'form': form})  # Rendre le template