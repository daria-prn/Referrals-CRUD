from django.db import models
class Referral(models.Model):
	referral_id = models.CharField (max_length=6, unique=True)
	last_name = models.CharField (max_length=40)
	first_name = models.CharField (max_length=40)
	note = models.TextField (blank=True)
	referrer = models.CharField (max_length=255)
	class Meta:
		db_table = "referral"