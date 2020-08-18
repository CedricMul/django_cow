from django.shortcuts import render
from cowsay_app.forms import CowsayForm
from cowsay_app.models import CowsayModel
import subprocess

def index(request):
    # If a cowsay is posted
    if request.method == 'POST':
        form = CowsayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            txt = data.get('text')
            #Creates the text model for history
            CowsayModel.objects.create(
                text=txt
            )
            # Runs cowsay and gets an instance back
            cow_process = subprocess.run(
                f'cowsay {txt}',
                shell=True,
                #text=True,
                capture_output=True
            )
            # Translates instance output into a string
            cow_state = cow_process.stdout.decode()
            # Keeps submision form on screen
            form = CowsayForm()
            # Returns sub form and the cow instance
            return render(request, 'index.html', {
                'form': form,
                'cow_state': cow_state
            })
    form = CowsayForm()
    return render(request, 'index.html', {'form': form})

def history_view(request):
    cows = CowsayModel.objects.all().order_by('-id')
    #cows = cows.reverse()
    history = cows[:10]
    return render(request, 'history.html', {'history': history})
