from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomepageView(TemplateView):
    '''Display homepage'''
    template_name = 'homepage/index.html'

    # def post(self, request):
    #     info = self.request.POST
    #     ContactMessage.objects.create(
    #     name = info['name'],
    #     email = info['email'],
    #     message = info['message']
    #     )
    #     context = {
    #     'temp_mes': 'Your message has been recored. Thank you!',
    #     }
    #     return render(request, self.template_name, context)