from django.shortcuts import render, redirect
from.models import Client
from django.http import HttpResponse,JsonResponse
from.models import AIConversation
from.ai_servies import  ask_ai
    
def ai_chat (request):
    answer=""
    error=""
    question=""

    if request.method == "POST":
        question = request.POST.get("question","").strip()
        if question:
            try:
                answer= ask_ai(question)
                AIConversation.objects.create(question=question,answer=answer)
            except Exception:
                error = "Sorry, the AI service is unavailable"

    converations=AIConversation.objects.order_by("-created_at")
    context = {
        'titile':'Ai chat Program',
        'header':'Ai chat Asssitent',
        'answer':answer,
        'error':error,
        'question':question,
        'converstions':converations
    }
    return render(request,"Hotel/ai_chat.html",context)

def home(request):
    # return HttpResponse("Hotel")
    context={
        'header':'AVATARA RETURANT',
        'title':'Hotelsystem'
    }
    return render(request, "Hotel/home.html",context)

def list_client(request):
    clients=Client.objects.all()
    context={
        'header':'Client_list',
        'title':'Clients',
        "Client":clients
    }
    return render(request, "Hotel/list_client.html",context)

def Menu_list(request):
    context={
        'title':'Avatara Resturant - Dining Menu',
    }
    return render(request,"Hotel/Menu.html",context)


def book_table(request):
    if request.method == "POST":
        Name=request.POST.get("name")
        Phone_Number=request.POST.get("phone_number")
        Email=request.POST.get("email")
        Table_no=request.POST.get("Table_no")
        Reservation_Time=request.POST.get("reservation_time")
        document = request.FILES.get("document")

        Client.objects.create(name=Name, phone_number=Phone_Number, table=Table_no, email=Email, reservation_time=Reservation_Time, document=document)

        return redirect("home")

    else:
        context={
            'header':'Book a table',
            'title':'Book A table'
        }
    return render(request,"Hotel/Book.html", context)

def delete(request, Hotel_id):
    client=Client.objects.get(id=Hotel_id)
    client.delete()
    return redirect ('client')

def edit_client(request, Hotel_id):
    client = Client.objects.get(id=Hotel_id)

    if request.method == "POST":
        Name = request.POST.get("name")
        Phone_Number = request.POST.get("phone_number")
        Email = request.POST.get("email")
        Table_no = request.POST.get("Table_no")
        Reservation_Time = request.POST.get("reservation_time")
        document = request.FILES.get("document")

        Client.objects.filter(id=Hotel_id).update(
            name=Name,
            phone_number=Phone_Number,
            email=Email,
            table=Table_no,
            reservation_time=Reservation_Time,
        )

        if document:
            client.refresh_from_db()
            client.document = document
            client.save()

        return redirect("client")

    context = {
        'header': 'Edit Client',
        'title': 'Edit Client',
        'client': client,
    }
    return render(request, "Hotel/Book.html", context)