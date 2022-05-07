from django import template

register = template.Library()

@register.filter(name='cooler')
def make_it_cool(arg):
    return arg[::2]

# register.filter('cooler',make_it_cool)
