import urllib.parse
from django import template

register = template.Library()

@register.filter
def youtube_embed(value):
    """
    Primește un URL YouTube (watch?v=ID sau youtu.be/ID)
    și returnează URL-ul de embed: https://www.youtube.com/embed/ID
    """
    if not value:
        return ''

    parsed = urllib.parse.urlparse(value)

    # Cazul "youtube.com/watch?v=ID"
    if 'youtube.com' in parsed.netloc:
        qs = urllib.parse.parse_qs(parsed.query)
        vid = qs.get('v')
        if vid:
            return f'https://www.youtube.com/embed/{vid[0]}'

    # Cazul "youtu.be/ID"
    if 'youtu.be' in parsed.netloc:
        vid = parsed.path.lstrip('/')
        return f'https://www.youtube.com/embed/{vid}'

    # În orice alt caz, întoarce URL-ul original
    return value