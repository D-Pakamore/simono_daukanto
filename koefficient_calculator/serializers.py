from rest_framework import serializers
from .models import ProfessionToExperience, ProfessionToQualification, Experience, Qualification

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'        

class ProfessionToExperienceSerializer(serializers.ModelSerializer):
    experience = ExperienceSerializer()
    class Meta:
        model = ProfessionToExperience
        fields = '__all__'

class ProfessionToQualificationSerializer(serializers.ModelSerializer):
    qualification = QualificationSerializer()
    class Meta:
        model = ProfessionToQualification
        fields = '__all__'