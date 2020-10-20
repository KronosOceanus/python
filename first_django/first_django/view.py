from django.http import HttpResponse

'''python .../django-admin.py startproject first_django
    当前（dos）目录创建 Web 应用'''

def hello(request):
    return HttpResponse('项目！')

def greeting(request):
    return HttpResponse('hello！')
