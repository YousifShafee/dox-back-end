from django.db.models import Max
import random
from django.core.mail import send_mail
from django.conf import settings
from .models import Advertisement

def get_confirm_code(email):
    active_code = random.randint(100000, 999999)
    send_mail(
        'Verify Email',
        str(active_code),
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=True,
    )
    return active_code


def get_data_by_field(request, search_dict):
    q = {}
    for item in request:
        if request[item] != '' and request[item] != 'NaN':
            if item in search_dict and search_dict[item]:
                q[search_dict[item]] = u'%s' % request[item]
    if 'price' in search_dict:
        if 'fprice' not in request or request['fprice'] == 'NaN':
            fprice = 0
        else:
            fprice = request['fprice']
        if 'lprice' not in request or request['lprice'] == 'NaN':
            lprice = Advertisement.objects.all().aggregate(Max('price'))['price__max']
        else:
            lprice = request['lprice']
        q[search_dict['price']] = [fprice, lprice]
    return q