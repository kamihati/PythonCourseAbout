import os
from django.conf import settings
from django import forms

file_save_path = os.path.join(settings.BASE_DIR, "upload/portaint/")


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
