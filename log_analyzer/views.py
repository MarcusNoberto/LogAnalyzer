from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Log
from .utils import process_logs

# View para chamar o metodo para processar os logs e passar os dados para o template
def import_logs(request):
    process_logs()
    log_list = Log.objects.all()

    # Configurar o número de registros por página
    items_per_page = 10
    paginator = Paginator(log_list, items_per_page)

    # Obter o número da página da solicitação GET
    page = request.GET.get('page')

    try:
        logs = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um número inteiro, entregue a primeira página
        logs = paginator.page(1)
    except EmptyPage:
        # Se a página está fora do intervalo (por exemplo, 9999), entregue a última página de resultados
        logs = paginator.page(paginator.num_pages)

    return render(request, 'log_list.html', {'logs': logs})
