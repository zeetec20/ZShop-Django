from django.shortcuts import render
from django.views import View
from django.shortcuts import render

class Index(View):
    template_name = "store/index.html"

    def get(self, request, *args, **kwargs):
        context = {
        
        }
        return render(request, self.template_name, context)

