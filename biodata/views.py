from rest_framework.views import APIView
from rest_framework.response import Response
from biodata.models import Profile
from django.http import JsonResponse
from rest_framework.response import Response
# Create your views here.
class ProfileList(APIView):
    def get(self, request, *args, **kwargs):
        data = {
        "slackUsername": "ambroseotundo",
        "backend": "true",
        "age": 24,
        "bio": "I am an avid backend engineer who is on a mission to develop scalable software."
    }
        return Response(data)
