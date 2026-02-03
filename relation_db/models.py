from django.db import models


# Модель отношения many:many
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class NumberCar(models.Model):
    nameCar = models.CharField(max_length=100, default='Lexus GX 570')
    nummer_car = models.CharField(max_length=15, default="..KG....")
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return f'{self.nameCar}------{', '.join(i.name for i in self.tags.all() )}'



# Модель отношение 1:1  
class DocumentCar(models.Model):
    choice_car = models.OneToOneField(NumberCar, on_delete=models.CASCADE, related_name='car')
    document = models.CharField(max_length=100)

    def __str__(self):
        return self.document
    
# Модель 1:many
class Review(models.Model):
    MARKS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    choice_car = models.ForeignKey(NumberCar, on_delete=models.CASCADE, related_name='review')
    marks = models.CharField(max_length=100, choices=MARKS, default='5')
    text = models.CharField(max_length=100, default='отличная машина')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Марка:{self.choice_car}-Оценка:{self.marks}-Коммент:{self.text}'
    







    





