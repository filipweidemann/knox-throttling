from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]


class ThrottledReferenceView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(data={"content": "request was valid."})
