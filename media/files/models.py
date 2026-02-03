from django.db import models

class Todo(models.Model):
    name_todo = models.CharField(max_length=100, verbose_name='enter your todo')
    plans = models.TextField(verbose_name='enter your_plan', blank=True)
    STATUS = (
        ('✅', '✅'),
        ('❌', '❌')
    )
    status = models.CharField(max_length=100, verbose_name='enter your status', 
                              choices=STATUS, default='❌')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name_todo}-{self.status}'
    
    class Meta:
        verbose_name = 'tasks'
        verbose_name_plural = 'task'

