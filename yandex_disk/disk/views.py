import requests

from io import BytesIO

from zipfile import ZipFile

from urllib.parse import quote

from django.shortcuts import render
from django.http import HttpResponse


API_BASE_URL = 'https://cloud-api.yandex.net/v1/disk/public/resources'

def index(request):
    public_key = request.GET.get('public_key')
    file_type = request.GET.get('file_type', '')
    file_list = []

    if public_key:
        response = requests.get(API_BASE_URL, params={'public_key': public_key})
        if response.status_code == 200:
            items = response.json().get('_embedded', {}).get('items', [])
            for item in items:
                if file_type == 'image' and item.get('media_type') != 'image':
                    continue
                elif file_type == 'document' and item.get('media_type') != 'document':
                    continue
                file_list.append(item)

    return render(request, 'disk.html', {'files': file_list, 'public_key': public_key, 'selected_type': file_type})

def download(request):
    public_key = request.POST.get('public_key')
    file_paths = request.POST.getlist('file_paths')

    if public_key and file_paths:
        zip_buffer = BytesIO()

        with ZipFile(zip_buffer, 'w') as zip_file:
            for file_path in file_paths:
                download_url = f'{API_BASE_URL}/download'
                encoded_file_path = quote(file_path)
                response = requests.get(download_url, params={'public_key': public_key, 'path': encoded_file_path})

                if response.status_code == 200:
                    href = response.json().get('href', '')
                    file_response = requests.get(href)
                    if file_response.status_code == 200:
                        zip_file.writestr(file_path.split('/')[-1], file_response.content)

        zip_buffer.seek(0)

        response = HttpResponse(zip_buffer, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="files.zip"'
        return response

    return HttpResponse('Error when downloading files!', status=400)
