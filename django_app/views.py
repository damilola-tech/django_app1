from django.shortcuts import render

# Create your views here.


def hello_world(request):
    return render(request, 'hello_world.html')


def fiver(request):
    context = {
        'message': 'This is how we do.',
         'sugar': 'https://images.theconversation.com/files/307440/original/file-20191217-58292-nlmvmh.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=900.0&fit=crop'
    }
    return render(request, 'fiver.html', context)


