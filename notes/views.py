from django.shortcuts import render
from django.http import HttpResponse


def hi(requsert):
    return HttpResponse('Hello from Notes app.')
