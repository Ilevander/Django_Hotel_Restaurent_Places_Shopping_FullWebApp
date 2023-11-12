from .models import Property
from .serializers import PropertySerializer
from rest_framework.generics import ListAPIView , RetrieveAPIView,ListCreateAPIView , RetrieveUpdateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

'''
ListAPIView : a simple view of data that returns json data
*********** : Provides a get method handler.
class PropertyAPIList(ListAPIView):
      #A queryset to get all properties
      queryset = Property.objects.all()
      serializer_class = PropertySerializer
'''


'''ListCreateAPIView : This returns json data and also a graphical form as a control pannel : 
  ******************* : Provides GET and POST method handlers.
'''
class PropertyAPIList(ListCreateAPIView):
      #A queryset to get all properties
      queryset = Property.objects.all()
      serializer_class = PropertySerializer  
      permission_classes = [IsAuthenticated]
'''
RetrieveAPIView : This provides the details of data
**************** : Used for read-only endpoints to represent a single model instance.
                 : Provides a get method handler.
class PropertyAPIDetail(RetrieveAPIView):
      #A queryset to get all properties
      queryset = Property.objects.all()
      serializer_class = PropertySerializer 
'''


'''RetrieveUpdateAPIView : Used for read or update endpoints to represent a single model instance.
   ********************* : Provides get, put and patch method handlers.
   class PropertyAPIDetail(RetrieveUpdateAPIView):
      #A queryset to get all properties
      queryset = Property.objects.all()
      serializer_class = PropertySerializer 
'''


'''But what we realy need is to apply the crud method.
So gonne use this : 
'''
class PropertyAPIDetail(RetrieveUpdateDestroyAPIView):
      #A queryset to get all properties
      queryset = Property.objects.all()
      serializer_class = PropertySerializer 
      permission_classes = [IsAuthenticated]