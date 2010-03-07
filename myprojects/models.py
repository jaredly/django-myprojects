from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
import tagging
from tagging.fields import TagField

class Type(models.Model):
    """Type model"""
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        verbose_name = _('type')
        verbose_name_plural = _('types')
        ordering = ('title',)

    def __unicode__(self):
        return u'%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('myprojects_view_type', None, {'slug': self.slug})

STATUSES = (
        ('alpha', _('Alpha')),
        ('beta', _('Beta')),
        ('released', _('Released')),
        ('idk', _('Ummm...'))
    )

class Project(models.Model):
    """Project Model"""
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, blank=True, null=True)
    short_desc = models.CharField(max_length=255)
    description = models.TextField()
    source = models.FileField(upload_to = 'projects', blank=True)
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to='projects')
    time = models.DateTimeField(auto_now_add=True)
    tags = TagField()
    status = models.CharField(max_length=10, choices = STATUSES)
    types = models.ManyToManyField(Type, blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ('-time',)
        get_latest_by = 'time'

    @permalink
    def get_absolute_url(self):
        return ('myprojects_view', None, {
            'slug': self.slug
        })

