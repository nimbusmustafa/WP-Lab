from django.shortcuts import render, redirect
from .models import BookVote
from .forms import VoteForm
from django.db.models import Count

# View to reset all votes
def reset_votes(request):
    BookVote.objects.all().delete()  # Deletes all the votes in the database
    return redirect('vote') 

# View for voting page
def vote_view(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('results')
    else:
        form = VoteForm()

    return render(request, 'voting/vote_page.html', {'form': form})

# View for results page
def result_view(request):
    total_votes = BookVote.objects.count()
    if total_votes == 0:
        results = {
            'good': 0,
            'satisfactory': 0,
            'bad': 0,
        }
    else:
        results = {
            'good': BookVote.objects.filter(vote='good').count() / total_votes * 100,
            'satisfactory': BookVote.objects.filter(vote='satisfactory').count() / total_votes * 100,
            'bad': BookVote.objects.filter(vote='bad').count() / total_votes * 100,
        }

    return render(request, 'voting/results_page.html', {'results': results})
