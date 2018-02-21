from django.shortcuts import render


# Главная страница
def index(request):
    # print("#######-->", request)
    return render(request, 'mainApp/homePage.html')


# Контактные данные
def contact(request):
    contact_info = {
        'value': [
            'Если у вас остались, то задайте их мне по телефону',
            '+7(961)-080-03-86',
            'rasulov3645@gmail.com'
            ]
    }
    return render(request, 'mainApp/basic.html', contact_info)
