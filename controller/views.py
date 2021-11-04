from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from controller.models import Device
from serial import Serial


# change below parameters as per need
com_port = "COM9"
baud_rate = 9600
timeout = 0.0
encoding = 'utf-8'
arduino = Serial(com_port, baud_rate, timeout=timeout)


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')

    devices = Device.objects.all()
    return render(request, 'index.html', context={'devices':devices})


def update_values(request):
    if request.method == "POST":
        devices = Device.objects.all()
        for device in devices:
            # if device is present in the post method then turn them on else turn off
            if device.name in request.POST:
                device.state = True
            else:
                device.state = False
            device.save()
            arduino_message = f'{1 if device.pin_type else 0}:{device.pin}:{1 if device.state else 0},'
            arduino.write(arduino_message.encode(encoding))
            print(device.name,arduino_message)

    return redirect("/")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect("/login")