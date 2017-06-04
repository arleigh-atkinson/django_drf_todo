from django.db import models

class Item(models.Model):
	"""Item model."""
	name = models.CharField(max_length=255, blank=False)
	completed = models.BooleanField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""Format model name and completed"""
		return "{}".format(self.name, self.completed)
