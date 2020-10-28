from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username', 'email', 'password')
    
    def update(self,instance, validated_data):
        self.instance.username = self.validated_data['username']
        self.instance.email = self.validated_data['email']
        self.instance.set_password(self.validated_data['password'])
        self.instance.save()
        return self.instance
    def create(self,validated_data):
        user = User()
        print(validated_data)
        user.username = self.validated_data['username']
        user.email = self.validated_data['email']
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
    