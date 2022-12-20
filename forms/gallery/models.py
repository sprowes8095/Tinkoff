from django.db import models

# Create your models here.

class Gallery(models.Model): # картинки принято хранить в uploads
    image = models.FileField(upload_to='my_gallery')  #ссылка на файл в стороннем хранилище, сам файл в БД не сохраняет
