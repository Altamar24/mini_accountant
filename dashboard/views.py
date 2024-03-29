from django.shortcuts import render

def index (request):
    return render(request, 'dashboard/index.html')


def get_category (request):
    return render(request, 'dashboard/category.html')


def get_transaction (request):
    return render(request, 'dashboard/transaction.html')