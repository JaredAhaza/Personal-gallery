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

class Image(models.Model):
    image = models.ImageField(upload_to='gallery/', blank=True)
    image_name = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=100, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    locaton = models.ForeignKey('Location', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, target, update):
        updated = cls.objects.filter(id=id).update(target=update)
        return updated

    @classmethod
    def get_all(cls):
        images = cls.objects.order_by('-post_date')
        return images

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def searched(cls, query):
        result = cls.objects.filter(description_icontains=query).order_by('-post_date')

        return result

    @classmethod
    def today_pics(cls):
        today = dt.date.today()
        images = cls.objects.filter(post_date__date=today)
        return images

    @classmethod
    def kenya(cls):
        images = cls.objects.filter(
            location__location__startswith='kenya').order_by('-post_date')
        return images

    @classmethod
    def personal(cls):
        images = cls.objects.filter(
            location__location__startswith='personal').order_by('-post_date')
        return images


class Location(models.Model):
    location = models.CharField(max_length=20)
    
    def save_locations(self):
        self.save()

    def delete_locations(self):
        self.delete()

    
    @classmethod
    def update_location(cls, id, location, update):
        updated = cls.objects.filter(id=id).update(location=update)
        return update

    def __str__(self):
        return self.location