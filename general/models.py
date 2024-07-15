from django.db import models
from solo.models import SingletonModel # type: ignore
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.


class Presentation(SingletonModel):
    title=models.CharField('Titulo',max_length=30)
    small_description=models.TextField('Descripcion')

    class Meta:
        verbose_name='Presentacion'
        verbose_name_plural=verbose_name
    
    def __str__(self) -> str:
        return self.title

class Social(SingletonModel):
    facebook = models.URLField(('facebook'))
    instagram = models.URLField('instagram')
    twitter = models.URLField('twitter')

    class Meta:
        verbose_name = "Redes sociales"
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Redes sociales'


class Gallery(models.Model):
    name = models.CharField('Nombre',max_length=100)
    image = models.ImageField('Imagen',upload_to='gallery')
    

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class BlogComment(models.Model):
    email = models.EmailField('email')
    comment = models.TextField('comentario' ,max_length=250)
    active = models.BooleanField('activo',default=False)
    likes = models.IntegerField('likes',default=0, validators=[MinValueValidator(0)])
    date_time_create= models.DateTimeField("Fecha de creacion",auto_now_add=True)
    users= models.ManyToManyField(User,blank=True,related_name='users')

    class Meta:
        verbose_name = 'Comentario sobre el Blog'
        verbose_name_plural = 'Comentarios sobre el Blog'

    def __str__(self):
        return self.email

    def user_has_comment(self,user):
        if self.users.filter(id=user).exists():
            return True
        return False
    
class Event(models.Model):
    name = models.CharField('Nombre',max_length=100)
    image = models.ImageField('Imagen',upload_to='events')
    active = models.BooleanField('activo',default=False)
    

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.name