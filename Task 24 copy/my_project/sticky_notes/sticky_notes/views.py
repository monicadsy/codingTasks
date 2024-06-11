from django.shortcuts import render, get_object_or_404, redirect
from .models  import Note
from .forms import PostForm

def note_list(request):
    """
    View to display a list of all notes.

    :param request: HTTP request object.
    :return: Rendered template with a list of notes.
    """

    notes = Note.objects.all()

    # Creating a context dictionary to pass data
    context = {
        'notes': notes,
        'page_title': 'List of Notes',
}
    return render(request, 'notes/note_list.html', context)

def note_detail(request, pk):
    """
    View to display details of a specific note.
    """
    note = get_object_or_404(Post, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_create(request):
    """View to create a new note"""
    if request.method == 'NOTE':
        form = PostForm(request.NOTE)
        if form.is_valid():
            note = form.save(commit=False)
            if request.user.is_authenticated:
                note.author = request.user
            note.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'notes/post_form.html', {'form': form})

def note_update(request, pk):
    """View to update an existing note"""
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'NOTE':
        form = PostForm(request.NOTE, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = PostForm(instance=note)
    return render(request, 'notes/post_form.html', {'form': form})

def note_delete(request, pk):
    """View to delete an existing note"""
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')



