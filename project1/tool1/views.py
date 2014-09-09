from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (CreateView, ListView, 
                                  UpdateView, DeleteView)
from django.core.urlresolvers import reverse_lazy

from .models import Medications, Patient, UploadFile, content_file_name
from .forms import MedicationsForm, UploadFileForm


### for tests ####
#class viewform(FormView):
#    form_class = ExampleModelForm
#    template_name = 'test.html'


##### file uploader #####
def handle_uploaded_file(f):
    with open('/home/splus/Johsin/Django/upload/content_file_name', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
#####


##### search #####
def search_form(request):
    return render(request, 'search_form.html')
 
def search(request):
    if 'q' in request.GET and request.GET['q']:
        query = request.GET['q']
        patients = Medications.objects.filter(patient= query)
        return render(request, 'search_results.html',
            {'patients': patients, 'query': query})
    else:
        return HttpResponse('Please enter a patient ID.')
#####


class Patient_List(ListView):
    template_name = 'search_form.html'
    model = Patient


class Medications_Create(CreateView):
    form_class = MedicationsForm
    template_name = 'med_form.html'
    success_url = reverse_lazy('med_list')    

    def get_form(self, form_class):
        form = super(Medications_Create, self).get_form(form_class)
	form.fields['patient'].initial = self.kwargs.get('pk')   
        return form


class Medications_List(ListView):
    template_name = 'med_list.html'
    model = Medications
    paginate_by = 20	


class Medications_Update(UpdateView):
    model = Medications
    form_class = MedicationsForm
    template_name='med_form.html'
    success_url = reverse_lazy('med_list')


class Medications_Delete(DeleteView):
    model = Medications
    template_name='confirm_delete.html'
    success_url = reverse_lazy('med_list')
