from django.forms import ModelForm, BooleanField
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Подтвердить!')

    class Meta:
        model = Post
        fields = ['author', 'postTitle', 'postCategory', 'postText', 'categoryType', 'check_box']
