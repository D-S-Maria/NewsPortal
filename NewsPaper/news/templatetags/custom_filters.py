from django import template

register = template.Library()

CENSOR = [
    'музыка',
    'спорт'
]


@register.filter()
def censor(value):
    """
    value: значение, к которому нужно применить фильтр
   """
    for c in CENSOR:
        value = value.replace(c[1:], '*' * len(c[1:]))
    return f'{value}'
