from django.conf.urls import url
from shop.forms import CustomUserCreationForm, CreateVehicleForm
from shop.views import CategoryView , HomePageView, FirmView, RegistrationView, BrandView, CreateVehicleView, CreateBrandView,CreateFirmView,VehicleView, DeleteVehicleView, UpdateVehicleView, CategoryDetailView, CategoryVehiclesView, VehiclesPDFView, BrandDetailView

urlpatterns = [
        url(r'^$', HomePageView.as_view(), name="home"),
        url(r'^category$', CategoryView.as_view(), name="categorylist"),
        url(r'^category/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name="categoryvehiclelist"),
        url(r'^firm$',FirmView.as_view(), name="firmlist"),
        url(r'^category/(?P<pk>\d+)/categoryvehicle.pdf$', CategoryVehiclesView.as_view(), name="catveh"),
        url(r"^signup/$", RegistrationView.as_view(form_class=CustomUserCreationForm), name="register"),
        url(r"^brand$",BrandView.as_view(), name="brandlist"),
        url(r'^brand/(?P<pk>\d+)/$', BrandDetailView.as_view(), name="brandvehiclelist"),
        url(r"^create_vehicle/$", CreateVehicleView.as_view(), name="createvehicle" ),
        url(r'^create_brand/$', CreateBrandView.as_view(), name="createbrand" ),
        url(r'^vehicle/(?P<pk>\d+)/$', VehicleView.as_view(), name="vehicledetail" ),
        url(r'^vehicle/(?P<pk>\d+)/delete/$',DeleteVehicleView.as_view() , name="vehicledelete" ),
        url(r'^vehicle/(?P<pk>\d+)/update/$',UpdateVehicleView.as_view() , name="updatevehicle" ),
        url(r'^vehicle/(?P<pk>\d+)/vehicle.pdf$', VehiclesPDFView.as_view(), name="vehiclepdf"),
        url(r'^create_firm/$', CreateFirmView.as_view(), name="createfirm"),
      ]

