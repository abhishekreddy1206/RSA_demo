from models import *
from rest_framework import serializers
import pdb

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student

# class ParentSerializer(serializers.ModelSerializer):
# 	#student = serializers.PrimaryKeyRelatedField()	
# 	class Meta:
# 		model = Parent
# 		depth = 1

class RegisterSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Parent

    def create(self, validated_data):
    	studentList = validated_data.pop('students')
    	parent = Parent.objects.create(**validated_data)
    	for student_data in studentList:
    		Student.objects.create(parent=parent, **student_data)
    	return parent

# class RegistrationSerializer(serializers.ModelSerializer):
# 	#student = StudentSerializer( source='student_set')
# 	student_set = StudentSerializer(many = True)
# 	class Meta:
# 		model = Parent
