from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля  
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    image = models.CharField(max_length=1200, null=False)
    release_date = models.CharField(max_length=30, null=False)
    lte_exests = models.BooleanField(null=False)
    slug = models.SlugField(max_length=100)
    pass
    
    #def __str__(self):
        #return f'{self.id}. {self.name}'
        