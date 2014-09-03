from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime, date
from bootstrap3_datetime.widgets import DateTimePicker

from .models import (Medications, MedDoseUnitLkup, 
                     MedDoseFreqLkup, MedClassLkup, 
		     Patient, UploadFile)
#from .validators import today_val


class UploadFileForm(ModelForm):
    class Meta:
	model = UploadFile


class Medications_Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Medications_Form, self).__init__(*args, **kwargs)
	self.fields['med_class'].label='Standard Medication Name*'
        self.fields['med_class'].choices=[(x.med_class_id, x.med_class_name) 
                                           for x in 
                                           MedClassLkup.objects.filter(
                                           med_class_id__gte=92)]
	self.fields['med_class'].required = True
        self.fields['med_dose'].label='Dose*'
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
        self.fields['start_date'].label='Start Date*'
	self.fields['start_date'].required = True
        self.fields['start_date_est_flag'].label='Est.'
        self.fields['end_date'].label='End Date'
        self.fields['end_date_est_flag'].label='Est.'
	self.fields['data_source'].label='Data Source'
	self.fields['med_prescriber'].label='Prescriber'
	self.fields['med_route'].label='Route'
#	self.fields['prn_flag'].initial = 0
#	self.fields['start_date'].validators.append(today_val)

    class Meta:
        model = Medications
        fields = (
            'patient', 'med_class', 'med_dose', 'med_dose_est_flag',
            'dose_unit', 'dose_freq', 'prn_flag', 'med_route',
            'start_date', 'start_date_est_flag', 'end_date',
            'end_date_est_flag', 'data_source', 'med_prescriber', 'notes'
            )     
        widgets = {
#            'start_date': DateTimePicker(
#		options={"format": "YYYY-MM-DD","pickTime": False}),	    
            'start_date': SelectDateWidget(
                years=range(date.today().year-6,date.today().year)),
	    'end_date': SelectDateWidget(
                years=range(date.today().year,date.today().year+6)),
            }
