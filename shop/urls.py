from django.conf.urls import url
from shop.forms import CustomUserCreationForm, CreateVehicleForm
from shop.views import CategoryView , HomePageView, FirmView, RegistrationView, BrandView, CreateVehicleView, CreateBrandView

urlpatterns = [
        url(r'^$', HomePageView.as_view(), name="home"),
        url(r'^category$', CategoryView.as_view(), name="categorylist"),
        url(r'^firm$',FirmView.as_view(), name="firmlist"),
        url(r"^signup/$", RegistrationView.as_view(form_class=CustomUserCreationForm), name="register"),
        url(r"^brand$",BrandView.as_view(), name="brandlist"),
        url(r"^create_vehicle/$", CreateVehicleView.as_view(), name="createvehicle" ),
        url(r'^create_brand/$', CreateBrandView.as_view(), name="createbrand" ),
      ]

