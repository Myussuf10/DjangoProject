from django.shortcuts import render
from rest_framework import viewsets
from .models import PostMessage
from .serializers import PostMessageSerializer
from .serializers import InteractionSerializer
from .models import Interaction
# Create your views here.

class PostMessageViewSet(viewsets.ModelViewSet):
	queryset = PostMessage.objects.all().order_by('created')
	serializer_class = PostMessageSerializer

class InteractionViewSet(viewsets.ModelViewSet):
	queryset = Interaction.objects.all().order_by('created')
	serializer_class = InteractionSerializer

def myapp_post(request):
	post_list = PostMessage.objects.all()
	interaction = Interaction.objects.all()
	return render(request, 'main.html', {'post': post_list, 'interaction':interaction})
