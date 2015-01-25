from models import *
from serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pdb

class StudentDetails(APIView):
	def get(self, request, pk, format = None):
		student_detail = Student.objects.filter(id = pk)
		serialized_student_detail = StudentSerializer(student_detail, many = True)
		return Response(serialized_student_detail.data)

class RegistrationDetails(APIView):
	def get(self, request, pk, format = None):
		parent_detail = Parent.objects.filter(id = pk)
		serialized_parent_detail = RegistrationSerializer(parent_detail, many = True)
		return Response(serialized_parent_detail.data)

class RegistrationList(APIView):
	def get(self, request, format = None):
		pass

	def post(self, request, format = None):
		register = RegisterSerializer(data = request.data)
		if register.is_valid():
			register.save()
			return Response(True, status = status.HTTP_201_CREATED)
		return Response(register.errors, status = status.HTTP_400_BAD_REQUEST)
