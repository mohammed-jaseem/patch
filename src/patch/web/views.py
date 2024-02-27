from django.shortcuts import render,HttpResponse
from web.models import Service,Brand,Contact,Friend,FaqCategory

def index(request):
    services= Service.objects.all()
    brands= Brand.objects.all()
    contacts= Contact.objects.all()
    friends= Friend.objects.all()
    faqcategorys= FaqCategory.objects.all()
    context={
        "services": services,
        "brands" : brands,
        "contacts": contacts,
        "friends": friends,
        "faqcategorys": faqcategorys,
    }
    return render(request,"index.html",context=context)


