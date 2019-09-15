from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api view"""

    def get(self, request, format=None):
        """Returns a list of APIView reatures"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your appication logic',
            'Is mapped manually to URLs',]

        return Response({'message':'Hello', 'an_apiview': an_apiview})
