import appsettings
from django import forms

register = appsettings.register('myprojects')

@register(nogroup=True)
class Main:
    setting = "Mutable"
    ease = 1000
    usefulness = forms.ChoiceField(label='Usefulness', choices = (('very','Very'),('extremely', 'Extremely'),('surprisingly','Amazingly')))

# vim: et sw=4 sts=4
