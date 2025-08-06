from django.http import HttpResponse
from django.template import loader

def sum_view(request):  
    if request.method == 'POST':
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        result = num1 + num2
        return HttpResponse(f"Views: {result}")
    template = loader.get_template('sum.html')
    return HttpResponse(template.render({}, request))