from django.db import models
from userroles.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class StudyActivityStorage(models.Model):   
    #лаборатория 
    container_name = models.CharField(max_length = 100, verbose_name = 'Название лаборатории')
    container_director = models.OneToOneField(UserProfile, on_delete= models.CASCADE)
    container_capacity = models.IntegerField(
        default = 0,
        validators=[MaxValueValidator(200), MinValueValidator(0)]
    )
    '''
    3 - LAB
    4 - COURSE
    5 - PRACTICE
    '''
    container_type = models.IntegerField(
        default = 3,
        validators=[MaxValueValidator(5), MinValueValidator(3)]
    )
    
    
    def __str__(self):
        return "Название лаборатории: {0}".format(self.lab_name)


class StudyRequest(models.Model):
    #Запрос в "контейнер"
    student = models.ForeignKey(UserProfile, on_delete= models.CASCADE)
    container = models.ForeignKey(Container, on_delete= models.CASCADE)
    
    '''
    0 = SENDED
    1 = ACCEPTED
    2 = DECLINED 
    '''
    status = models.IntegerField(
        default = 0,
        validators=[MaxValueValidator(2), MinValueValidator(0)]
    )
    
    send_date = models.DateField(auto_now=True)