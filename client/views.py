from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View


class Placeholder(View):
    def get(self, request):
        return redirect("/api/")
