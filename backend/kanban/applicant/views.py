# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Applicant


@api_view(['GET'])
def get_all_applicants(request):
    res = request.data
    return Response(res)


@api_view(['POST'])
def add_applicant(request):
    res = request.data
    entry = Applicant(
        name = res['name'],
        education = res['education'],
        contact = res['contact'],
        status = 'Applied',
        rate = 0,
        rate_number = 0
    )
    entry.save()
    return Response(res)
