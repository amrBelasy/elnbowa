from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from .models import HomeImage, Depart1, Depart2, Depart3, Depart4, Opinion, Youtube



def index(request):
    model = HomeImage.objects.all() 
    opi = Opinion.objects.all()
    return render(request, template_name='index.html', context={'image': model, 'opinion': opi})

def grass(request):
    model = Depart2.objects.all() 
    return render(request, template_name='grass.html', context={'image': model})


def lawful(request):
     video = Youtube.objects.all() 
     return render(request, template_name='lawful.html', context={'video': video})


def depart(request):

    return render(request, template_name='depart.html')

def depart1(request):
    model = Depart1.objects.all() 
    return render(request, template_name='dep1.html', context={'image': model})


def depart2(request):
    model = Depart2.objects.all() 
    return render(request, template_name='dep2.html', context={'image': model})


def depart3(request):
    model = Depart3.objects.all() 
    return render(request, template_name='dep3.html', context={'model': model})


def depart4(request):
    model = Depart4.objects.all() 
    return render(request, template_name='dep4.html', context={'image': model})

  


# other stuff

def view_404(request, exception):
    return redirect('/')


def contact(request):

    #     form = ContactForm(request.POST or None)
    #     if form.is_valid():
    #         # for key, value in form.cleaned_data.iteritems():
    #         # 	print key, value
    #         # 	#print form.cleaned_data.get(key)
    #         form_email = form.cleaned_data.get("email")
    #         form_message = form.cleaned_data.get("message")
    #         form_full_name = form.cleaned_data.get("full_name")
    #         # print email, message, full_name
    #         subject = 'Site contact form'
    #         from_email = settings.EMAIL_HOST_USER
    #         to_email = [from_email, 'amrbelasy2@gmail.com']
    #         contact_message = "%s: %s via %s" % (
    #             form_full_name,
    #             form_message,
    #             form_email)
    #         some_html_message = """
    # 		<h1>hello</h1>
    # 		"""
    #         send_mail(subject,
    #                   contact_message,
    #                   from_email,
    #                   to_email,
    #                   html_message=some_html_message,
    #                   fail_silently=True)

    # #         email = EmailMessage(
    # #          subject = 'That’s your subject',
    # #           body = 'That’s your message body',
    # #            from_email = 'from@yourdjangoapp.com',
    # #            to = ['amrbelasy2@gmail.com'],
    # #           bcc = ['bcc@anotherbestuser.com'],
    # #           reply_to = ['whoever@itmaybe.com'],
    # # )
    title = "تواصل معنا"
    form = ContactForm(request.POST or None)
    context = {
        "form": form,
        "title": title,
    }

    if form.is_valid():
        # form.save()
        # print request.POST['email'] #not recommended
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("الاسم")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        # if not instance.full_name:
        # 	instance.full_name = "Justin"
        instance.save()
        context = {
            "title": "تم ارسال الرسالة بنجاح "
        }
    return render(request, "forms.html", context)
