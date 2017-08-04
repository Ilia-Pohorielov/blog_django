from django import template
from comments.forms import CommentForm

register = template.Library()

@register.inclusion_tag('blogs/inner_blog.html')
def tree_comments_by_object(object):
    from django.contrib.contenttypes.models import ContentType
    comments = object.comments.select_related().all()
    content_type = ContentType.objects.get_for_model(object)
    form = CommentForm(initial={'content_id': object.id, 'content_type': content_type.id})
    return {'comments': comments, 'comment_form': form}