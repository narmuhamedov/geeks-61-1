from django import forms
from prog_lang.models import ProgLang

class ProgLangForm(forms.ModelForm):
    class Meta:
        model = ProgLang
        fields = "__all__"

        #если вдруг только определенные
        #fields = "title description".split()

        