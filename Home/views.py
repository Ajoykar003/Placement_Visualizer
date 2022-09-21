from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from Home.models import Contact


def home(request):
    return render(request, 'Home/index.html')


#
def contact(request):
    if request.method == "POST":
        print("Post section is working")
        mail = request.POST['email']
        name = request.POST['name']
        Passout_year = request.POST['Passout_year']
        company_name = request.POST['company_name']
        job_role = request.POST['job_role']
        linkedin_id = request.POST['linkedin_id']
        print(mail, name, job_role, linkedin_id, company_name)
        ins = Contact(email=mail, name=name, linkedin_id=linkedin_id, Passout_year=Passout_year,
                      company_name=company_name, job_role=job_role)
        ins.save()

    # return redirect('/')

    return render(request, 'Home/contact.html')


#  return render(request, 'Home/record.html', context)

def record(request):
    allpost = Contact.objects.all()
    context = {'allpost': allpost}
    return render(request, 'Home/record.html', context)
