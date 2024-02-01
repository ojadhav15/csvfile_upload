from django.shortcuts import render, HttpResponse
from .forms import FileUploadForm


# Create your views here.
def FileUploadView(r):
    form = FileUploadForm()

    if r.method == 'POST':
        form = FileUploadForm(r.POST, r.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('<h1>file upload successfully</h1>')
    return render(r, "myapp/fileupload.html", {"form": form})
