from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def range_filter(value):
    if isinstance(value, Decimal):
        value = int(value)  # Convert Decimal to int
    return range(value)