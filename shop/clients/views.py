from django.shortcuts import render


def clients_main(request):
    return render(request,'clients/main.html')
