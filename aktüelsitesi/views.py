from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "index.html")

def listbycategoryname(request, category_name):
    if category_name == ("bim" or "Bim" or "BİM" or "bİM" or "BIM" or "bım" or "bIM"):
        return render(request, "bim.html")
    elif category_name == ("a101" or "A101") :
        return render(request, "a101.html")
    elif category_name ==("migros" or "Migros" or "MİGROS" or "mİGROS" or "mIGROS" or "mıgros" or "MIGROS"):
        return render(request, "migros.html")
    elif category_name == ("sok" or "SOK" or "Sok" or "şok" or "ŞOK" or "Şok") :
        return render(request, "sok.html")
    elif category_name == ("iletisim" or "İletisim" or "Iletısım" or "ıletısım"):
        return render(request, "iletisim.html")
    elif category_name == ("a101-2subat"):
        return render(request, "a101_2subat.html")
    elif category_name == ("a101-4subat"):
        return render(request, "a101_4subat.html")    
    elif category_name == ("a101-9subat"):
        return render(request, "a101_9subat.html")   
    elif category_name == ("a101-11subat"):
        return render(request, "a101_11subat.html") 
    elif category_name == ("a101-16subat"):
        return render(request, "a101_16subat.html")
    elif category_name == ("bim-3subat"):
        return render(request, "bim_3subat.html")
    elif category_name == ("bim-7subat"):
        return render(request, "bim_7subat.html")
    elif category_name == ("bim-10subat"):
        return render(request, "bim_10subat.html")
    elif category_name == ("bim-14subat"):
        return render(request, "bim_14subat.html")
    elif category_name == ("bim-31ocak"):
        return render(request, "bim_31ocak.html")
    elif category_name == ("sok-4subat"):
        return render(request, "sok_4subat.html")
    elif category_name == ("sok-8subat"):
        return render(request, "sok_8subat.html")
    elif category_name == ("migros-2subat"):
        return render(request, "migros_2subat.html")
    elif category_name == ("migros-19ocak"):
        return render(request, "migros_19ocak.html")
    elif category_name == ("a101-18subat"):
        return render(request, "a101-18subat.html")
    elif category_name == ("a101-23subat"):
        return render(request, "a101-23subat.html")
    elif category_name == ("bim-17subat"):
        return render(request, "bim_17subat.html")
    elif category_name == ("bim-21subat"):
        return render(request, "bim_21subat.html")
    elif category_name == ("bim-24subat"):
        return render(request, "bim_24subat.html")
    elif category_name == ("sok-18subat"):
        return render(request, "sok_18subat.html")
    elif category_name == ("sok-11subat"):
        return render(request, "sok_11subat.html")
    elif category_name == ("sok-15subat"):
        return render(request, "sok_15subat.html")
    elif category_name == ("migros-16subat"):
        return render(request, "migros_16subat.html")
    elif category_name == ("admin"):
        return render(request, "admin/")









    
    else:
        return render(request,  "404.html")

