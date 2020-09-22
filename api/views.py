from rest_framework import viewsets, permissions
from api.models import BankDetail
from api.serializers import UserSerializer, BankInfoSerializer


class BankViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = BankDetail.objects.all()
    serializer_class = BankInfoSerializer
    lookup_field = 'ifsc_code'
    # http_method_names = ['get', 'post', 'update','list','create','put']



    


 