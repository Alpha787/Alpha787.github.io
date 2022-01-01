"""To render HTML web pages"""
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import Lead
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def lead_detail_view(request, id=None):
    lead_obj = None
    if id is not None:
        lead_obj = Lead.objects.get(id=id)
    context = {
        'objects': lead_obj,
    }
    return render(request, 'MainSite/index_test.html', context=context)

def index(request):
    context = {}
    return render(request, 'MainSite/index.html', context)

def about(request):
    context = {}
    return render(request, 'MainSite/about.html', context)

def blog(request):
    context = {}
    return render(request, 'MainSite/blog.html', context)

def contact(request):
    context = {}
    return render(request, 'MainSite/contact.html', context)

# def send_contact(request):
#     if request.method == "POST":
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
#         # send an email
#         send_mail(
#             subject, # subject
#             message, # message
#             email, # from email
#             ['olofmeister22668@gmail.com'], # to email
#             )
#         return render(request, 'MainSite/contact.html', {'subject':subject})
#     else:
#         return render(request, 'MainSite/contact.html', {})


def get_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Пробное сообщение'
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())
            try:
                send_mail(subject, message,
                          'vasya22668@gmail.com',
                          ['vasya22668@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect('homepage')

    form = ContactForm()
    return render(request, 'MainSite/contact.html', {'form': form})


def services(request):
    context = {}
    return render(request, 'MainSite/services.html', context)

def work(request):
    context = {}
    return render(request, 'MainSite/work.html', context)

def work_single(request):
    context = {}
    return render(request, 'MainSite/work-single.html', context)

