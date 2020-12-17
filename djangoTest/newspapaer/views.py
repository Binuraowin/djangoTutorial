from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Destination


# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.desc="binura woin destination"
    dest1.name="binura"
    dest1.img="destination_1.jpg"
    dest1.price=700
    dest1.offer=True

    dest2 = Destination()
    dest2.desc = "binura woin destination"
    dest2.name = "binura"
    dest2.img = "destination_1.jpg"
    dest2.price = 700
    dest2.offer = False

    dest3 = Destination()
    dest3.desc = "binura woin destination"
    dest3.name = "binura"
    dest3.img = "destination_2.jpg"
    dest3.price = 700
    dest3.offer = False

    dest4 = Destination()
    dest4.desc = "binura woin destination"
    dest4.name = "binura"
    dest4.img = "destination_3.jpg"
    dest4.price = 700
    dest4.offer = True

    destList = [dest1,dest2,dest3,dest4]

    return render(request,"index.html",{"destList":destList})