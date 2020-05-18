from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libra.models import *
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
import json, mammoth, os
from djusers.settings import BASE_DIR


"""------------------------------------------------------------"""


def get_text_from_book(request):
    if request.user.is_authenticated:
        
        book_file = book.objects.filter(id = request.POST["id"])[0]

        file_name = os.path.split(book_file.book_file.url)[1]
        media_dir = os.path.join(BASE_DIR, 'media')
        file_path = os.path.join(media_dir, file_name)

        with open(file_path, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            text = result.value # The raw text
            messages = result.messages # Any messages

        converted_docx = text
        
        converted_docx_list = list(converted_docx.split('</p><p>'))
        chunk_length = 22

        converted_docx_list = [converted_docx_list[i:i + chunk_length] for i in range(0, len(converted_docx_list), chunk_length)]

        for i in converted_docx_list:
            try:
                i[0] = i[0].replace('<p>','')
            except:
                pass
            try:
                i[-1] = i[-1].replace('</p>','')
            except:
                pass
            converted_docx_list[converted_docx_list.index(i)] = '<p>' + str('</p><p>'.join(i)) + '</p>'


        error = 'Все норм'

    else:
        error = 'Вы не зарегистрировались'

    responseData = {
        'error': error,
        'converted_docx': converted_docx,
        'converted_docx_list': converted_docx_list
    }

    return JsonResponse(responseData)

def get_book_description(request):
    if request.user.is_authenticated:
        book_file = book.objects.filter(id = request.POST["id"])[0]
    else:
        error = 'Вы не зарегистрировались'

    responseData = {
        'error': error,
        'description': book_file.description,
        'author': book_file.author,
        'name': book_file.name,
        'release_date': book_file.release_date,
        'category': book_file.category,
        'cover': book_file.cover,
    }

    return JsonResponse(responseData)