# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Applicant


@api_view(['GET'])
def get_all_applicants(request):
    entrys = list(Applicant.objects.all())
    return_list = []
    for e in entrys:
        entry = {
            'name': e.name,
            'education': e.education,
            'contact': e.contact,
            'status': e.status,
            'rate': e.rate,
            'rate_number': e.rate_number
        }
        return_list.append(entry)
    return Response(return_list)


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


@api_view(['POST'])
def add_rate(request):
    res = request.data
    contact = res['contact']
    new_rate = int(res['newRate']['rate'])
    print(new_rate)
    entry = Applicant.objects.filter(contact=contact)[0]
    s = entry.rate * entry.rate_number + new_rate
    entry.rate_number += 1
    entry.rate = s / entry.rate_number
    entry.save()
    return Response(entry.rate)
