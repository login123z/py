from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название статьи", help_text="Например: сеггодня 212ww22434")
    slug = models.CharField(max_length=255, verbose_name="URL", unique=True)
# Create your models here.
    class Meta:
        verbose_name ="категоря "
        verbose_name_plural ="Категория"
    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey("Category", on_delete =models.CASCADE, verbose_name ="Категория")
    title = models.CharField(max_length=250, verbose_name="Название статьи", help_text="Например: сеггодня 21222434")
    slug = models.CharField(max_length=255, verbose_name="URL", unique=True)
    is_active =models.BooleanField(default=True, verbose_name="jnjfjfj")
    content = models.TextField(verbose_name="Контент", blank=False)
    image = models.ImageField(upload_to="blog/", verbose_name="izo", blank=False, null=False)

    class Meta:
        verbose_name ="Посты "
        verbose_name_plural ="Посты"
    def __str__(self):
        return self.title
