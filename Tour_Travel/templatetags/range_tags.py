from django import template

register = template.Library()

@register.filter(name='to')
def to(value, end):
    """
    Returns a Python range from value to end (exclusive).
    Example:
      {% for i in 0|to:5 %} → 0,1,2,3,4
    """
    try:
        start = int(value)
        stop = int(end)
        return range(start, stop)
    except (ValueError, TypeError):
        return []
