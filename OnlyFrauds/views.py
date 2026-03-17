from django.shortcuts import render
import mysql.connector as mq
con=mq.connect(host="localhost",user="root",password="12345678",database="projectkavach")
cur=con.cursor()
def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        con=mq.connect(host="localhost",user="root",password="12345678",database="projectkavach")
        cur=con.cursor()
        cur.execute("select * from user where email = %s and password=%s",(email,password))
        fetchall = cur.fetchall()
        if fetchall:
            return render(request, "dashboard.html")

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cur.execute("insert into user (name,email,password) values (%s,%s,%s)",(name, email, password))
        con.commit()
        return render(request, "login.html")
    return render(request, "login.html")

def dashboard(request):
    return render(request, "dashboard.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def documentation(request):
    return render(request, "documentation.html")
def privacy(request):
    return render(request, "privacy.html")
def terms(request):
    return render(request, "terms.html")
def settings(request):
    return render(request, "settings.html")
def support(request):
    return render(request, "support.html")
def community(request):
    return render(request, "community.html")
def api(request):
    return render(request, "api.html")