from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Submit

from .models import (Medications, MedDoseUnitLkup, 
                     MedDoseFreqLkup, MedClassLkup, 
		     Patient, UploadFile)
#from .validators import today_val


### for tests ###
#class ExampleModelForm(forms.ModelForm):
#    def __init__(self, *args, **kwargs):
#        super(ExampleModelForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
#        self.helper = FormHelper(self)
        # You can dynamically adjust your layout
#        self.helper.layout.append(Submit('save', 'save'))
#    class Meta:
#        model = Patient


class UploadFileForm(ModelForm):
    class Meta:
	model = UploadFile
	fields = ('title', 'file')


class MedicationsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicationsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            'patient', 'med_class', 
            Div(
                Div('med_dose', css_class='col-md-2'), 
                Div('med_dose_est_flag', css_class='col-md-1'),
                css_class='row',
                ),
            'dose_unit', 
            'dose_freq', 
            'prn_flag', 
            'med_route',
            Div(
                Div('start_date', css_class='col-md-2'), 
                Div('start_date_est_flag', css_class='col-md-1'),
                css_class='row',
                ),
            Div(
                Div('end_date', css_class='col-md-2'), 
                Div('end_date_est_flag', css_class='col-md-1'),
                css_class='row',
                ),
            'data_source', 
            'med_prescriber', 
            'notes',
            )
        self.helper.layout.append(Submit('save','Save'))
	self.fields['med_class'].label='Standard Medication Name'
        self.fields['med_class'].choices=[(x.med_class_id, x.med_class_name) 
                                           for x in 
                                           MedClassLkup.objects.filter(
                                           med_class_id__gte=92)]
	self.fields['med_class'].required = True
        self.fields['med_dose'].label='Dose'
        self.fields['med_dose'].required = True
        self.fields['med_dose_est_flag'].label='Est.'
	self.fields['dose_unit'].label='Dose Unit'
        self.fields['dose_unit'].choices=[(x.dose_unit_id, x.dose_unit_name) 
                                          for x in 
                                          MedDoseUnitLkup.objects.all()]
        self.fields['dose_freq'].label='Dose Frequency'
        self.fields['dose_freq'].choices=[(x.dose_freq_id, x.dose_freq_name) 
                                          for x in 
                                          MedDoseFreqLkup.objects.all()]
        self.fields['prn_flag'].label='PRN'
        self.fields['start_date'].label='Start Date'
	self.fields['start_date'].required = True
        self.fields['start_date_est_flag'].label='Est.'
        self.fields['end_date'].label='End Date'
        self.fields['end_date_est_flag'].label='Est.'
	self.fields['data_source'].label='Data Source'
	self.fields['med_prescriber'].label='Prescriber'
	self.fields['med_route'].label='Route'

    class Meta:
        model = Medications
        fields = (
            'patient', 'med_class', 'med_dose', 'med_dose_est_flag',
            'dose_unit', 'dose_freq', 'prn_flag', 'med_route',
            'start_date', 'start_date_est_flag', 'end_date',
            'end_date_est_flag', 'data_source', 'med_prescriber', 'notes'
            )
