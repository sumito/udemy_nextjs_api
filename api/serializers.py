from rest_framework import serializers
from .models import Task,Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fiedls = ('id','username','password')
        fields='__all__' # 追加
        extra_kwargs = {'password': {'write_only': True, 'required' : True }}
        

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)

    class Meta:
        model = Post
        fields = ('id','title','content','created_at')
        fields='__all__' # 追加

class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)

    class Meta:
        model = Task
        fields = ('id','title','created_at')
        fields='__all__' # 追加