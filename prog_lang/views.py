from django.shortcuts import render, get_object_or_404
from . import models



def prog_lang_detail_view(request, id):
    if request.method == 'GET':
        prog_lang_id = get_object_or_404(models.ProgLang, id=id)
        return render(
            request,
            'prog_lang_detail.html',
            {
                "prog_id": prog_lang_id
            }
        )





#list 
def prog_lang_list_view(request):
    if request.method == "GET":
        prog_lang = models.ProgLang.objects.all()
        return render(
            request,
            'prog_languages.html',
            {
                "prog_lang": prog_lang
            }
        )

    