from django import template

register = template.Library()

@register.filter(name='cutvalue')
def cutvalue(value,arg):
    """
    This cuts out values of arg from string
    """
    return value.replace(arg,'')

# register.filter('cutvalue',cutvalue)
