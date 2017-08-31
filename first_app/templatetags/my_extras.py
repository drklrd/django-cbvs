from django import template

register = template.Library()

def cut(value,arg):
    """
    This cuts out values of arg from string
    """
    return value.replace(arg,'')

register.filter('cut',cut)
