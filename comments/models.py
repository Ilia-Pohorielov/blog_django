# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class Comment(models.Model):
    path = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=u"Пользователь")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['path']
        db_table = 'comment'
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'

    def __init__(self, *args, **kwargs):
        self.parent_id = None
        super(Comment,self).__init__(*args, **kwargs)

    @property
    def level(self):
        return max(0,len(self.path)/8-1)

    @property
    def html_level(self):
        return self.level * 3

    def get_absolute_url(self):
        return '%s#comment%s' % (self.content_object.get_absolute_url() , self.id)

    def __unicode__(self):
        return self.text

    def save(self):
        super(Comment,self).save()
        if not self.path:
            if self.parent_id:
                try:
                    parent_path = Comment.objects.get(pk=self.parent_id).path
                except:
                    parent_path = ''
            else:
                parent_path = ''
            self.path =  '%s%08d' % (parent_path, self.id)
            super(Comment,self).save()