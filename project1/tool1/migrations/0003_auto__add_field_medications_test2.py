# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Medications.test2'
        db.add_column(u'medications', 'test2',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Medications.test2'
        db.delete_column(u'medications', 'test2')


    models = {
        u'tool1.facility': {
            'Meta': {'object_name': 'Facility', 'db_table': "u'facility'", 'managed': 'False'},
            'common_address_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deletedby': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'deleteddate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facility_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'facility_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'facility_type_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_virtual': ('django.db.models.fields.IntegerField', [], {}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'npi_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'salesforce_link_id': ('django.db.models.fields.CharField', [], {'max_length': '18', 'blank': 'True'}),
            'tax_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'tool1.medclasslkup': {
            'Meta': {'object_name': 'MedClassLkup', 'db_table': "u'med_class_lkup'", 'managed': 'False'},
            'med_class_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'med_class_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'med_temp_flag': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'med_type_flag': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        u'tool1.meddosefreqlkup': {
            'Meta': {'object_name': 'MedDoseFreqLkup', 'db_table': "u'med_dose_freq_lkup'", 'managed': 'False'},
            'dose_freq_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'dose_freq_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'freq_type_flag': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        u'tool1.meddoseunitlkup': {
            'Meta': {'object_name': 'MedDoseUnitLkup', 'db_table': "u'med_dose_unit_lkup'", 'managed': 'False'},
            'dose_unit_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'dose_unit_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'unit_type_flag': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        u'tool1.medications': {
            'Meta': {'object_name': 'Medications', 'db_table': "u'medications'"},
            'asmt_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'assessed_by': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'data_source': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'deleteby': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deleteddate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dose_freq': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tool1.MedDoseFreqLkup']", 'null': 'True', 'blank': 'True'}),
            'dose_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tool1.MedDoseUnitLkup']", 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'end_date_est_flag': ('django.db.models.fields.BooleanField', [], {}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tool1.Facility']", 'null': 'True', 'blank': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'med_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tool1.MedClassLkup']", 'null': 'True', 'blank': 'True'}),
            'med_class_flag': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'med_dose': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'med_dose_est_flag': ('django.db.models.fields.BooleanField', [], {}),
            'med_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'med_prescriber': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'med_route': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'ndc_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'other_prescriber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'others': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tool1.Patient']"}),
            'physician_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prn_flag': ('django.db.models.fields.BooleanField', [], {}),
            'provider_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_date_est_flag': ('django.db.models.fields.BooleanField', [], {}),
            'test': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'test2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'tool1.patient': {
            'Meta': {'object_name': 'Patient', 'db_table': "u'patient'", 'managed': 'False'},
            'admission_risk_contact': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'admission_risk_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'admission_risk_status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'assistance_level_id': ('django.db.models.fields.IntegerField', [], {}),
            'calculated_referred_by_comment': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'calculated_referred_by_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'calculated_referred_by_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calculated_referred_by_updated_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'contact_prefer_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'contact_prefer_time': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deleted_reason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'deletedby': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'deleteddate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'do_not_contact_email_address_flag': ('django.db.models.fields.IntegerField', [], {}),
            'do_not_contact_email_alt_address_flag': ('django.db.models.fields.IntegerField', [], {}),
            'do_not_contact_home_phone_flag': ('django.db.models.fields.IntegerField', [], {}),
            'do_not_contact_mobile_phone_flag': ('django.db.models.fields.IntegerField', [], {}),
            'do_not_contact_school_phone_flag': ('django.db.models.fields.IntegerField', [], {}),
            'do_not_contact_work_phone_flag': ('django.db.models.fields.IntegerField', [], {}),
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'email_alt_address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'enrolled_by_exception_tobedeleted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Enrolled_By_Exception_tobedeleted'", 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'health_plan_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'health_policy_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "u'lastUpdatedby'", 'blank': 'True'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'load_method': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'low_utilizer_flag': ('django.db.models.fields.IntegerField', [], {}),
            'maiden_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'member_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'not_used_referred_by_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'paid_by_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'patient_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'phone_email_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'pref_first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'primary_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'ptp_infusion_elgiblity_flag': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'ptp_infusion_elgiblity_flag_updt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ptp_infusion_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reconciliation_flag': ('django.db.models.fields.IntegerField', [], {'db_column': "u'Reconciliation_Flag'"}),
            'referred_by_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'referred_by_updated_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'salesforce_link_id': ('django.db.models.fields.CharField', [], {'max_length': '18', 'blank': 'True'}),
            'school_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'service_center_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sf_master_status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sf_referred_by_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sf_referred_by_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sf_referred_by_updated_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'total_opt_out': ('django.db.models.fields.IntegerField', [], {}),
            'total_opt_out_reason': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'wh_anxiety_flag': ('django.db.models.fields.IntegerField', [], {}),
            'wh_depression_flag': ('django.db.models.fields.IntegerField', [], {}),
            'wh_multi_condition_flag': ('django.db.models.fields.IntegerField', [], {}),
            'wh_pain_flag': ('django.db.models.fields.IntegerField', [], {}),
            'wh_sleep_flag': ('django.db.models.fields.IntegerField', [], {}),
            'wh_smoking_flag': ('django.db.models.fields.IntegerField', [], {}),
            'wh_stress_flag': ('django.db.models.fields.IntegerField', [], {}),
            'wh_weight_flag': ('django.db.models.fields.IntegerField', [], {}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        }
    }

    complete_apps = ['tool1']