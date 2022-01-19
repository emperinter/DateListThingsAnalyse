#froms.py通过模型创建表单

from .models import ModelFileField
from django.forms import ModelForm

class ModelFormFile(ModelForm):
    class Meta:
        model = ModelFileField
        fields = "__all__"