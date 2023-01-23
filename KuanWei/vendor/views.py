from django.shortcuts import render#rendor可以將我們要傳達的資料一併打包，再透過 HttpResponse 回傳到瀏覽器
#from django.views.decorators.csrf import csrf_protect
from .models import Vendor
from .forms import VendorForm # Day18要記得 import 相對應的 Model Form 唷!
from django.http import Http404
from django.urls import reverse # 新增

# Create your views here.
def vendor_index(request):#名稱對應urls.py urlpatterns中的path
    vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list} # 建立 Dict對應到Vendor的資料，
    return render(request, 'vendors/vendor__detail_all.html',context)

# 針對 vendor_create.html
def vendor_create_view(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VendorForm() # 清空 form

    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)

def singleVendor(request, id):
    vendor_list = Vendor.objects.get(id=id)

    context = {
        'vendor_list': vendor_list
    }
    return render(request, 'vendors/vendor_detail.html', context)



def showtemplate(request):
    vendor_list = Vendor.objects.all()
    context = {'vendor_list': vendor_list}
    # print(vendor_list)
    return render(request, 'vendors/vendors_detail_all.html', context)