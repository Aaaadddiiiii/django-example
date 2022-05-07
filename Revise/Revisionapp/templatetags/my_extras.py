from django import template

register = template.Library()

def remove(value,arg):
    """
    This cuts out all values of arg from the string
    """

    return value.replace(arg,'')

register.filter('remover',remove)
