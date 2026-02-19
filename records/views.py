from django.shortcuts import render
from django.http import HttpResponse
from .models import TextRecord

def add_record(request):
    new_entry = TextRecord.objects.create(content="This is a new record!")
    return HttpResponse(f"<h1>Success!</h1><p>Record saved.</p>")

def show_records(request):
    all_records = TextRecord.objects.all()
    output = "<br>".join([f"{r.id}: {r.content}" for r in all_records])
    return HttpResponse(f"<h1>Stored Records:</h1><p>{output}</p>")
