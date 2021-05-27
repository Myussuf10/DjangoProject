from rest_framework import serializers
from .models import PostMessage
from .models import Interaction

class PostMessageSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = PostMessage
		fields = '__all__'

class InteractionSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = Interaction
		fields = '__all__'
