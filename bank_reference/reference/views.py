from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class AddBank(View):
    template_name = ('reference/add_bank.html')
    form = AddBankForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = self.form(request.POST)
            if form.is_valid():
                saved_form = form.save()
                return HttpResponseRedirect('/list_of_banks/')
        else:
            form = self.form()

        return render(request, self.template_name, context={'form': form})


def list_of_banks(request):
    search_query = request.GET.get('search', '')
    if search_query:
        banks = Bank.objects.filter(Q(BIC__icontains=search_query) | Q(name__icontains=search_query))
    else:
        banks = Bank.objects.all()
    return render(request, 'reference/list_of_banks.html', context={'banks': banks})
