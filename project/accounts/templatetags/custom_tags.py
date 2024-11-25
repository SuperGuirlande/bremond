from django import template
from django.contrib import messages

register = template.Library()

@register.simple_tag(takes_context=True)
def clear_session_message(context, message_key):
    request = context['request']
    if message_key in request.session:
        del request.session[message_key]
    return ''