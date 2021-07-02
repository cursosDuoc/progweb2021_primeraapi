# sirve para relacionar nuestra API con los modelos que ya existen
# En este caso, vamos a partir con User
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer) :
    # voy a decir cuales son los campos que quiero que sean visibles del usuario
    # normalmente, voy a omitir la password.
    class Meta :
        model = User
        fields = ['url' , 'username', 'email']