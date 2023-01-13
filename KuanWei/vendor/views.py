from django.shortcuts import render#rendor可以將我們要傳達的資料一併打包，再透過 HttpResponse 回傳到瀏覽器
from .models import Vendor

# Create your views here.
def vendor_index(request):#名稱對應urls.py urlpatterns中的path
    vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list} # 建立 Dict對應到Vendor的資料，
    return render(request, 'vendors/vendor_detail.html',context)
