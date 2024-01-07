from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Log
from .serializers import LogSerializer
from rest_framework import filters
from django.utils.dateparse import parse_date
from rest_framework.generics import ListAPIView
from datetime import datetime
from rest_framework.pagination import PageNumberPagination

class LogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class LogListView(ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description', 'timestamp']
    pagination_class = LogPagination

    def get_queryset(self):
        start_date_str = self.request.query_params.get('start_date')
        end_date_str = self.request.query_params.get('end_date')

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

            queryset = Log.objects.filter(timestamp__range=(start_date, end_date))
            return queryset

        return Log.objects.all()

'''
class LogViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Log.objects.all()
    serializer_class = LogSerializer


    @action(detail=False, methods=['GET'])
    def filter_logs(self, request):
        """
        Endpoint para filtrar logs por período e/ou conteúdo da mensagem e/ou descrição.
        Parâmetros opcionais:
            - start_date: Data de início (formato: 'YYYY-MM-DD').
            - end_date: Data de término (formato: 'YYYY-MM-DD').
            - search: Termo de busca para o conteúdo da mensagem.
            - description_search: Termo de busca para a descrição.

        Exemplo de requisição:
        /filter_logs/?start_date=2022-01-01&end_date=2022-12-31&search=Erro&description_search=Detalhes
        """
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        search_term = request.query_params.get('search', '')
        filter_backends = [filters.SearchFilter, rest_framework_filters.OrderingFilter]
        search_fields = ['description', 'timestamp']
        ordering_fields = ['timestamp']
        description_search_term = request.query_params.get('description_search', '')

        # Validação dos parâmetros
        if start_date and end_date:
            try:
                start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d')
                end_date = timezone.datetime.strptime(end_date, '%Y-%m-%d')
            except ValueError:
                return Response({'error': 'Formato de data inválido. Use o formato: YYYY-MM-DD.'}, status=400)

            queryset = Log.objects.filter(timestamp__range=(start_date, end_date))
        elif search_term or description_search_term:
            queryset = Log.objects.filter(message__icontains=search_term, description__icontains=description_search_term)
        else:
            return Response({'error': 'Pelo menos um dos parâmetros start_date, end_date, search ou description_search deve ser fornecido.'}, status=400)

        serializer = LogSerializer(queryset, many=True)
        return Response(serializer.data)'''