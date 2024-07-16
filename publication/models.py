from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class Category(models.Model):
    name = models.CharField('Nombre',max_length=100)
    active = models.BooleanField('Activar', default=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

    
class Publication(models.Model):
    title = models.CharField('Nombre',max_length=100)
    date_time_create= models.DateTimeField("Fecha de creacion",auto_now_add=True)
    image = models.ImageField('Imagen',upload_to='publication')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Autor')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Categoria')
    small_description = models.TextField('Pequeña descripcion',max_length=100)
    description = models.TextField('Cuerpo de la publicacion')
    active = models.BooleanField('Activar', default=False)

    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.title

class PublicationComment(models.Model):
    publication = models.ForeignKey(Publication,on_delete=models.CASCADE,verbose_name='Publicacion')
    email = models.EmailField('email')
    comment = models.TextField('comentario' ,max_length=255)
    active = models.BooleanField('activo',default=False)
    likes = models.IntegerField('likes',default=0, validators=[MinValueValidator(0)])
    date_time_create= models.DateTimeField("Fecha de creacion",auto_now_add=True)
    users= models.ManyToManyField(User,blank=True,related_name='users_publication')


    class Meta:
        verbose_name = 'Comentario sobre la publicacion'
        verbose_name_plural = 'Comentarios sobre Publicaciones'
        
    def __str__(self):
        return self.email
    
    def user_has_comment(self,user):
        if self.users.filter(id=user).exists():
            return True
        return False