from django.shortcuts import render
from django.http import HttpResponse
from AVShopProject import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect,HttpResponseRedirect
from .forms import WriteUsForm
from django.http.response import HttpResponseNotAllowed

# Create your views here.
def message_view(request):
    if request.method == 'POST':
        form = WriteUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            prod_buyed = form.cleaned_data['prod_buyed']
            message = form.cleaned_data['message']
            all_data = f"Name: {name}\nCity/Village: {city}\nMobile: {mobile}\nProduct Buyed: {prod_buyed}\nMessage:{message}\n"
            subject = "Message Form WriteForUs Page."
            sender = 'beyondhorrizon7@gmail.com'
            recipients = ['akashmothe1@gmail.com']

            sent = send_mail(subject, all_data, sender, recipients,fail_silently=False,auth_user=settings.EMAIL_HOST_USER,auth_password=settings.EMAIL_HOST_PASSWORD)
            if sent == 1:
                return redirect('/suggestion-success')
            else:
                messages.warning(request,'Failed, Your message not sent. Try again!')
                return redirect('/')
            # return redirect('/thankyou')

            
    else:
        form = WriteUsForm()
    return render(request,'write_us_app/message.html',{'form':form})

def msg_thanks_view(request):
    # thanks_head = "Thanks For your Suggestion."
    # thanks_para = "Thank you very much, we will definitly think about your suggestion."
    return render(request,'write_us_app/msg_thanks.html')
