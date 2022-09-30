from django.shortcuts import render
from .forms import InfoForm


def home(request):
    submitted = False
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
            # return HttpResponseRedirect('/?submitted=True')
    else:
        form = InfoForm()
        if 'submitted' in request.GET:
            submitted = True

    form = InfoForm

    context = {
        'form': form,
        'submitted': submitted,
    }
    return render(request, 'home.html', context)
