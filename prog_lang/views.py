from django.shortcuts import render, get_object_or_404,redirect
from . import models, forms
from django.core.paginator import Paginator

#search

def search_view(request):
    query = request.GET.get("s", '')
    if query:
        prog_lang = models.ProgLang.objects.filter(title__icontains=query)
    else:
        prog_lang = models.ProgLang.objects.none
    
    return render(
        request,
        'prog_languages.html',
        {
            "prog_lang": prog_lang,
        }

    )







#UPDATE
def update_proglang_view(request,id):
    prog_lang_id = get_object_or_404(models.ProgLang, id=id)
    if request.method == "POST":
        form = forms.ProgLangForm(request.POST, instance=prog_lang_id)
        if form.is_valid():
            form.save()
            return redirect('/prog_lang/')
    else:
        form = forms.ProgLangForm(instance=prog_lang_id)
    return render(
        request,
        'update_prog_lang.html',
        {
            "form": form,
            "prog_lang_id": prog_lang_id
        }
    )







#DELETE PROG LANG
def delete_prog_lang_view(request, id):
    prog_lang_id = get_object_or_404(models.ProgLang, id=id)
    prog_lang_id.delete()
    return redirect('/prog_lang/')





#CREATE PROG LANG
def create_prog_lang_view(request):
    if request.method == 'POST':
        form = forms.ProgLangForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/prog_lang/')
    else:
        form = forms.ProgLangForm()
    
    return render(
        request,
        'create_prog_lang.html',
        {
            "form": form
        }
    )
    









#READ

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
        paginator = Paginator(prog_lang, 2)
        page = request.GET.get("page")
        page_obj = paginator.get_page(page)
        return render(
            request,
            'prog_languages.html',
            {
                "prog_lang": page_obj
            }
        )

    