# log_analyzer/utils.py

import os
import csv
from .models import Log
from datetime import datetime, timezone

# Função que faz o processamento dos dados
def process_logs():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    logs_directory = os.path.join(current_directory, 'Logs')
    for filename in os.listdir(logs_directory):
        
        file_path = os.path.join(logs_directory, filename)
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                ip, timestamp_str, service_name, version, user_id, message, level, descricao = row[:8]
                timestamp = datetime.strptime(timestamp_str, '%d-%b-%Y')
                timestamp = timestamp.replace(tzinfo=timezone.utc)
                if Log.objects.filter(ip_address=ip).count() == 0:
                    Log.objects.create(
                        ip_address=ip,
                        timestamp=timestamp,
                        service_name=service_name,
                        version=version,
                        user_id=user_id,
                        message=message,
                        level=level,
                        description=descricao,
                    )
                # O break serve para deixar o programa mais rápido, já que todos os logs já estão no sistema
                # Se for adicionado mais arquivos, tirar o break e deixar o programa ler e fazer o reconhecimento dos dados denovo
                break
                