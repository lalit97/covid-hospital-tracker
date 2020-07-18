from . import views
from django.urls import path
from django.views.generic import TemplateView


app_name = "hospital"
urlpatterns = [
    path("", views.HomePageView.as_view(), name="home_page"),
    path("hospital/<int:pk>/", views.HospitalDetail.as_view(), name="h_detail"),
    path("hospital/", views.HospitalList.as_view(), name="h_list"),
    path(
        "hospital_update/<int:pk>/", views.HospitalUpdateView.as_view(), name="h_edit"
    ),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("filter_district/", views.FilterDistrict.as_view(), name="filter_district"),
    path("filter_taluka/", views.FilterTaluka.as_view(), name="filter_taluka"),
]
