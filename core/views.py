from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .data import NOTES # the . stands for the current dir
from django.db.models import Q
from django.views.generic import ListView
from .models import Note
from .forms import NoteForm

# Create your views here.
# @login_required
def list_notes(request):
    notes = Note.objects.all() #this will become Note.objects.filter(user=request.user) to show only those notes for the user whose loggedin
    return render(request, "base.html", {"notes": notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "core/note_detail.html", {"note": note})

def add_note(request):
    if request.method == 'GET':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="notes_list")

    return render(request, 'core/add_note.html', {'form': form})

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'GET':
        form = NoteForm(instance=note)
    else:
        form = NoteForm(data=request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(to='notes_list')
        
    return render(request, "core/edit_note.html", {"form": form, "note": note})

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect(to='notes_list')
    
    return render(request, "core/delete_note.html", {"note": note})

class SearchResultsView(ListView):
    model = Note
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Note.objects.filter(title__icontains=query)
        return object_list


