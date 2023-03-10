import os
from django.conf import settings
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def my_view(request):
    return render(request, 'index.html')

def load_excel(request):
    return render(request, 'upload_excel.html')

def upload_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        # 获取上传的文件对象
        uploaded_file = request.FILES['excel_file']
        # 生成文件名并拼接文件路径
        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
        # 保存文件到服务器上的指定目录
        # with open(file_path, 'wb+') as f:
        #     for chunk in uploaded_file.chunks():
        #         f.write(chunk)
        # 返回文件路径到模板
        context = {'file_path': file_path}
        return render(request, 'upload_success.html', context)
    return render(request, 'upload_excel.html')