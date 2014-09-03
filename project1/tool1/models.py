# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])


data_source_choices = (
    ('Patient', 'Patient'),
    ('Provider', 'Provider'),
    ('Significant Other', 'Significant Other'),
    ('Pharmacy', 'Pharmacy'),
    ('Claims', 'Claims'),
    ('Others', 'Others')
)


class UploadFile(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to=content_file_name)	


class Facility(models.Model):
    facility_id = models.BigIntegerField(primary_key=True)
    facility_name = models.CharField(max_length=100)
    deleted = models.IntegerField(blank=True, null=True)
    deletedby = models.CharField(max_length=30, blank=True)
    deleteddate = models.DateTimeField(blank=True, null=True)
    lastupdatedby = models.CharField(max_length=30, blank=True)
    lastupdateddate = models.DateTimeField(blank=True, null=True)
    common_address_id = models.BigIntegerField()
    facility_type_id = models.BigIntegerField(blank=True, null=True)
    npi_id = models.CharField(max_length=50, blank=True)
    tax_id = models.CharField(max_length=50, blank=True)
    is_virtual = models.IntegerField()
    salesforce_link_id = models.CharField(max_length=18, blank=True)
    class Meta:
        managed = False
        db_table = 'facility'


class MedClassLkup(models.Model):
    med_class_id = models.BigIntegerField(primary_key=True)
    med_class_name = models.CharField(max_length=64, blank=True)
    med_type_flag = models.CharField(max_length=1, blank=True)
    med_temp_flag = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'med_class_lkup'


class MedDoseFreqLkup(models.Model):
    dose_freq_id = models.BigIntegerField(primary_key=True)
    dose_freq_name = models.CharField(max_length=64, blank=True)
    freq_type_flag = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'med_dose_freq_lkup'


class MedDoseUnitLkup(models.Model):
    dose_unit_id = models.BigIntegerField(primary_key=True)
    dose_unit_name = models.CharField(max_length=64, blank=True)
    unit_type_flag = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'med_dose_unit_lkup'


class Medications(models.Model):
    med_id = models.BigIntegerField(primary_key=True)
    patient = models.ForeignKey('Patient')
    ndc_code = models.CharField(max_length=30, blank=True)
    med_class = models.ForeignKey('MedClassLkup', blank=True, null=True)
    med_dose = models.CharField(max_length=20, blank=True)
    dose_unit = models.ForeignKey('MedDoseUnitLkup', blank=True, null=True)
    med_dose_est_flag = models.BooleanField(blank=True)
#    med_dose_est_flag = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    dose_freq = models.ForeignKey('MedDoseFreqLkup',blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    start_date_est_flag = models.BooleanField(blank=True)
#    start_date_est_flag = models.IntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    end_date_est_flag = models.BooleanField(blank=True)
#    end_date_est_flag = models.IntegerField(blank=True, null=True)
    prn_flag=models.BooleanField(blank=True)
#    prn_flag = models.IntegerField(blank=True, null=True)
    data_source = models.CharField(max_length=30,
        choices=data_source_choices, blank=True)
    med_route = models.CharField(max_length=25, blank=True)
    med_prescriber = models.CharField(max_length=25, blank=True)
    assessed_by = models.CharField(max_length=30, blank=True)
    asmt_date = models.DateTimeField(blank=True, null=True)
    med_class_flag = models.CharField(max_length=1, blank=True)
    others = models.CharField(max_length=250, blank=True)
    deleted = models.IntegerField(blank=True, null=True)
    deleteby = models.CharField(max_length=30, blank=True)
    deleteddate = models.DateTimeField(blank=True, null=True)
    lastupdatedby = models.CharField(max_length=30, blank=True)
    lastupdateddate = models.DateTimeField(blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    facility = models.ForeignKey(Facility, blank=True, null=True)
    physician_id = models.BigIntegerField(blank=True, null=True)
    other_prescriber = models.CharField(max_length=20, blank=True)
    class Meta:
#        managed = False
        db_table = 'medications'

    def __unicode__(self):
        return str(self.med_id)
#	return str(self.pk)
#	return self.pk

    def get_absolute_url(self):
        return reverse('med_list', kwargs={'pk': self.pk})


class Patient(models.Model):
    patient_id = models.BigIntegerField(primary_key=True)
    member_id = models.CharField(max_length=20)
    time_zone = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=10, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    middle_name = models.CharField(max_length=30, blank=True)
    maiden_name = models.CharField(max_length=30, blank=True)
    pref_first_name = models.CharField(max_length=30, blank=True)
    suffix = models.CharField(max_length=10, blank=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    ssn = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    health_plan_id = models.BigIntegerField(blank=True, null=True)
    health_policy_id = models.BigIntegerField(blank=True, null=True)
    ptp_infusion_id = models.BigIntegerField(blank=True, null=True)
    ptp_infusion_elgiblity_flag = models.CharField(max_length=1, blank=True)
    ptp_infusion_elgiblity_flag_updt = models.DateTimeField(
        blank=True, null=True)
    home_phone = models.CharField(max_length=15, blank=True)
    work_phone = models.CharField(max_length=15, blank=True)
    mobile_phone = models.CharField(max_length=15, blank=True)
    school_phone = models.CharField(max_length=15, blank=True)
    primary_phone = models.CharField(max_length=15, blank=True)
    phone_email_type = models.CharField(max_length=25, blank=True)
    email_address = models.CharField(max_length=50, blank=True)
    email_alt_address = models.CharField(max_length=50, blank=True)
    contact_prefer_method = models.CharField(max_length=15, blank=True)
    contact_prefer_time = models.CharField(max_length=20, blank=True)
    low_utilizer_flag = models.IntegerField()
    total_opt_out = models.IntegerField()
    total_opt_out_reason = models.CharField(max_length=200, blank=True)
    do_not_contact_home_phone_flag = models.IntegerField()
    do_not_contact_work_phone_flag = models.IntegerField()
    do_not_contact_mobile_phone_flag = models.IntegerField()
    do_not_contact_school_phone_flag = models.IntegerField()
    do_not_contact_email_address_flag = models.IntegerField()
    do_not_contact_email_alt_address_flag = models.IntegerField()
    not_used_referred_by_date = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    deletedby = models.CharField(max_length=30, blank=True)
    deleteddate = models.DateTimeField(blank=True, null=True)
    deleted_reason = models.TextField(blank=True)
    lastupdatedby = models.CharField(
        db_column='lastUpdatedby', max_length=30, blank=True) 
        # Field name made lowercase.
    lastupdateddate = models.DateTimeField(blank=True, null=True)
    reconciliation_flag = models.IntegerField(db_column='Reconciliation_Flag') 
        # Field name made lowercase.
    salesforce_link_id = models.CharField(max_length=18, blank=True)
    service_center_id = models.BigIntegerField(blank=True, null=True)
    enrolled_by_exception_tobedeleted = models.IntegerField(
        db_column='Enrolled_By_Exception_tobedeleted', blank=True, null=True) 
        # Field name made lowercase.
    admission_risk_status = models.CharField(max_length=1, blank=True)
    admission_risk_contact = models.CharField(max_length=50, blank=True)
    admission_risk_date = models.DateTimeField(blank=True, null=True)
    paid_by_id = models.IntegerField(blank=True, null=True)
    load_method = models.CharField(max_length=1, blank=True)
    assistance_level_id = models.IntegerField()
    referred_by_id = models.IntegerField(blank=True, null=True)
    referred_by_updated_date = models.DateTimeField(blank=True, null=True)
    sf_referred_by_id = models.IntegerField(blank=True, null=True)
    sf_referred_by_date = models.DateTimeField(blank=True, null=True)
    sf_referred_by_updated_date = models.DateTimeField(blank=True, null=True)
    sf_master_status = models.IntegerField(blank=True, null=True)
    calculated_referred_by_id = models.IntegerField(blank=True, null=True)
    calculated_referred_by_date = models.DateTimeField(blank=True, null=True)
    calculated_referred_by_updated_date = models.DateTimeField(
        blank=True, null=True)
    calculated_referred_by_comment = models.CharField(
        max_length=100, blank=True)
    wh_anxiety_flag = models.IntegerField()
    wh_depression_flag = models.IntegerField()
    wh_stress_flag = models.IntegerField()
    wh_weight_flag = models.IntegerField()
    wh_smoking_flag = models.IntegerField()
    wh_sleep_flag = models.IntegerField()
    wh_pain_flag = models.IntegerField()
    wh_multi_condition_flag = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'patient'

    def __unicode__(self):
        return str(self.patient_id)

    def get_absolute_url(self):
        return reverse('patient_list', kwargs={'pk': self.pk})
