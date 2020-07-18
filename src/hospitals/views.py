from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from .forms import AvailabilityModelForm
from .models import (
    Hospital,
    Availability,
    SearchState,
    SearchDistrict,
    SearchTaluka,
    SearchPincode,
)


class HomePageView(ListView):
    model = Hospital
    paginate_by = 50
    template_name = "hospitals/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["states"] = SearchState.objects.all().order_by("state")
        context["districts"] = SearchDistrict.objects.all().order_by("district")
        context["talukas"] = SearchTaluka.objects.all().order_by("taluka")
        return context


class HospitalList(ListView):
    model = Hospital
    paginate_by = 60

    def get_queryset(self, **kwargs):
        qs = super(HospitalList, self).get_queryset(**kwargs)

        if self.request.GET.get("state_id"):
            state_id = self.request.GET.get("state_id")
            state = SearchState.objects.get(id=state_id)
            qs = qs.filter(state=state)

        if self.request.GET.get("district_id"):
            district_id = self.request.GET.get("district_id")
            district = SearchDistrict.objects.get(id=district_id)
            qs = qs.filter(district=district)

        if self.request.GET.get("taluka_id"):
            taluka_id = self.request.GET.get("taluka_id")
            taluka = SearchTaluka.objects.get(id=taluka_id)
            qs = qs.filter(taluka=taluka)

        return qs


class FilterDistrict(TemplateView):
    template_name = "hospitals/filter_district.html"

    def get_context_data(self, **kwargs):
        context = super(FilterDistrict, self).get_context_data(**kwargs)
        if self.request.GET.get("state_id"):
            state_id = self.request.GET.get("state_id")
            state = SearchState.objects.get(id=state_id)
            districts = SearchDistrict.objects.filter(state=state).order_by("district")
        else:
            districts = SearchDistrict.objects.all().order_by("district")
        context["districts"] = districts
        return context


class FilterTaluka(TemplateView):
    template_name = "hospitals/filter_taluka.html"

    def get_context_data(self, **kwargs):
        context = super(FilterTaluka, self).get_context_data(**kwargs)
        if self.request.GET.get("district_id"):
            district_id = self.request.GET.get("district_id")
            district = SearchDistrict.objects.get(id=district_id)
            talukas = SearchTaluka.objects.filter(district=district).order_by("taluka")
        else:
            talukas = SearchTaluka.objects.all().order_by("taluka")
        context["talukas"] = talukas
        return context


class HospitalDetail(DetailView):
    model = Hospital


class HospitalUpdateView(UpdateView):
    model = Availability
    template_name = "hospitals/hospital_update.html"
    form_class = AvailabilityModelForm
    success_url = reverse_lazy("hospital:home_page")

    def get_context_data(self, **kwargs):
        context = super(HospitalUpdateView, self).get_context_data(**kwargs)
        hospital_id = self.kwargs.get("pk")
        context["hospital_id"] = hospital_id
        return context

    def get_object(self):
        id_ = self.kwargs.get("pk")
        hospital = Hospital.objects.get(id=id_)
        try:
            avail_obj = hospital.availability
        except Availability.DoesNotExist:
            avail_obj = Availability.objects.create(hospital=hospital)
        return avail_obj
