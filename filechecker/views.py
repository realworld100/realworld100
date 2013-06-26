from django.shortcuts import render
import os, re
def index(request):
    is_file_exist = False
    if request.POST.has_key('regex'):
        filenames = os.listdir('.')
        for filename in filenames:
            if re.match(request.POST['regex'], filename):
                is_file_exist = True
                break
    return render(request, 'index.html', {'is_file_exist':is_file_exist})
