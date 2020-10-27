# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Applicant



@api_view(['GET'])
def get_all_applicants(request):
    res = request.data
    return Response(res)
