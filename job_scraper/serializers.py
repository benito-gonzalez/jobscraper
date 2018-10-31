from rest_framework.serializers import ModelSerializer
from .models import Job


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ('id','title', 'location', 'company')


class JobDetailSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
