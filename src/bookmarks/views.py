from django.contrib.auth.decorators import login_required
from django.shortcuts import render

app_name = 'bookmarks'

@login_required
def dashboard_view(request):
    return render(request, 'bookmarks/dashboard.html')
