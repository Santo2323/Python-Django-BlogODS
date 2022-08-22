from django.db import models

class Ods(models.Model):
	nombre = models.CharField(max_length = 255)
	descripcion = models.TextField(null = True)
	imagen = models.ImageField(upload_to='imagenes_ods', null=True)

	def __str__(self):
		return self.nombre

class Posts(models.Model):
	nombre = models.CharField(max_length=255)
	body = models.TextField(null = True)
	fecha_post = models.DateTimeField(auto_now_add=True, null = True)
	Ods = models.ForeignKey(Ods, on_delete = models.CASCADE)
	imagen = models.ImageField(upload_to='imagenes_posts', null=True)
		
	class Meta:
		ordering = ['-fecha_post']

	def __str__(self):
		return self.nombre

class Comentarios(models.Model):
	Posts = models.ForeignKey(Posts, related_name="comments", on_delete = models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)

	class Meta: 
		ordering = ("date_added",)


	def __str__(self):
		return '%s - %s' % (self.Posts.nombre, self.name)
