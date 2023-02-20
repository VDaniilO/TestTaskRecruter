from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib import messages

from .forms import *


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("allVacancy")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="regUser.html", context={"form":form})


def vacancy_output(request):
    vacancy = Vacancy.objects.all()
    return render(request, 'vacancy.html', {'vacancy': vacancy})


class AddVacancy(CreateView):
    form_class = VacancyForm
    template_name = 'register.html'
    success_url = reverse_lazy('allVacancy')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create new vacancy'
        return context
