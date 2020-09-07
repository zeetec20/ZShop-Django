from django.shortcuts import render
from django.views.generic import View

class Index(View):
    template_name = ''
    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)
