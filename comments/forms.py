from django import forms
from django.contrib.auth.models import User
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType


class CommentForm(forms.Form):
    parent_id = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
    message = forms.CharField(widget=forms.Textarea(), label = u'Комментарий')
    content_id = forms.IntegerField(widget=forms.HiddenInput())
    content_type = forms.IntegerField(widget=forms.HiddenInput())

    def save(self, auth_user):
        if self.is_valid() and auth_user.is_authenticated:
            content_id = self.cleaned_data.get('content_id')
            content_type = self.cleaned_data.get('content_type')
            parent_id = self.cleaned_data.get('parent_id')
            message = self.cleaned_data.get('message')
            object_c = ContentType.objects.get(pk=content_type).get_object_for_this_type(pk=content_id)
            c = Comment(
                text = message,
                user = User.objects.get(username = auth_user),
                content_object = object_c
            )
            c.parent_id = parent_id
            c.save()
            return c
        else:
            return False