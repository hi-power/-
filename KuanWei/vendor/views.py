from django.shortcuts import render#rendor可以將我們要傳達的資料一併打包，再透過 HttpResponse 回傳到瀏覽器
#from django.views.decorators.csrf import csrf_protect
from .models import Vendor
from .forms import VendorForm # Day18要記得 import 相對應的 Model Form 唷!

# Create your views here.
def vendor_index(request):#名稱對應urls.py urlpatterns中的path
    vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list} # 建立 Dict對應到Vendor的資料，
    return render(request, 'vendors/vendor_detail.html',context)

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