from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField (max_length = 30, blank=True)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, category, update):
        updated = cls.objects.filter(id=id).update(category=update)
        return updated

    def __str__(self):
        return self.name