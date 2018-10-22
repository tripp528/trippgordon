from django.shortcuts import render

# Create your views here.
def music(request):
    return render(request, 'music/maniac.html')

def accordian(request):
    return render(request, 'music/accordian.html')
