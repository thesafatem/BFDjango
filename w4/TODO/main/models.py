from django.db import models

# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Лист'
        verbose_name_plural = 'Листы'


class Task(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='Название')
    created = models.DateField(null=True, verbose_name='Создано')
    due_on = models.DateField(null=True, verbose_name='Выполнить до')
    owner = models.CharField(max_length=255, null=True, verbose_name='Создатель')
    mark = models.BooleanField(null=True, verbose_name='Статус')
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks', verbose_name='Лист')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

