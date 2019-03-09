from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
    now = datetime.now
    return render(
        request,
        "PaddeApp/index.html",
        {
            'content' : "Does this show up?"
        }
        )

# Create your views here.
