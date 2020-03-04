from quotes.models import Quote
from quotes.serializers import QuoteSerializer
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#For yasg
from drf_yasg.utils import swagger_auto_schema



class QuoteList(APIView):
    '''
    List all quotes or create a new quote
    '''
    @swagger_auto_schema(
        responses={200: QuoteSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No quotes found'},
        tags=['Get Quotes'],
        operation_description="Method to fetch all the quotes",
    )
    def get(self,request,format=None):
        print("Get quotes list called")
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        description="Method to post a new building",
        request_body=QuoteSerializer,
        responses={200: QuoteSerializer(many=False),
                   401: 'Unauthorized',
                   201: 'Quote Added'},
        tags=['Create, Update and Delete Quote'],
        operation_description="Method to post a new Quote",
    )
    def post(self, request, format=None):
        print("Create quote called")
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuoteDetail(APIView):
    """
    Retrieve, update or delete a quote instance.
    """
    @swagger_auto_schema(
        auto_schema=None,
    )
    def get_object(self, pk):
        try:
            return Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: QuoteSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No quote found for the given id'},
        tags=['Get Quotes'],
        operation_description="Method to fetch a quote",
    )
    def get(self, request, pk, format=None):
        quote = self.get_object(pk)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

    @swagger_auto_schema(
        description="Method to update a quote",
        request_body=QuoteSerializer,
        responses={200: QuoteSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Quote updated'},
        tags=['Create, Update and Delete Quote'],
        operation_description="Method to update a quote",
    )
    def put(self, request, pk, format=None):
        quote = self.get_object(pk)
        serializer = QuoteSerializer(quote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        description="Method to delete a quote",
        request_body=QuoteSerializer,
        responses={200: QuoteSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Quote deleted'},
        tags=['Create, Update and Delete Quote'],
        operation_description="Method to update a quote",
    )    
    def delete(self, request, pk, format=None):
        quote = self.get_object(pk)
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
