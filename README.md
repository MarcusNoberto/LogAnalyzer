LogAnalyzer

Este projeto utiliza o LogAnalyzer para processar logs e oferece uma interface web e uma API para visualização e consulta.

0) Pré-requisitos
- Docker
- Docker Compose

1) Instruções para Execução

    - Clone o repositório para sua máquina local:
        - git clone https://seu-repositorio.git
        - cd LogAnalyzer
    
    Execute o seguinte comando para iniciar o sistema usando Docker Compose:

        - docker-compose up -d

    Isso irá baixar as dependências, construir os contêineres e iniciar o serviço.

    Aguarde até que a construção seja concluída e os contêineres estejam em execução.

    Acesse a interface web em pelo link abaixo para interagir com o LogAnalyzer.
       
        - http://127.0.0.1:8000/teste/import_logs/ 
        

    Acesse a API pelo link abaixo para consultar os logs via API 

        - http://127.0.0.1:8000/logs/ 
    
2) Utilizando a API

    Ao acessar a API, caso queira buscar algo, clique no botão Filters que irá abrir uma seção para você buscar, você pode buscar tanto uma data especifica, como por exemplo, todos os logs de 2022, como uma descrição especifica. Como exemplo temos: 

        - http://127.0.0.1:8000/logs/?search=2022
        - http://127.0.0.1:8000/logs/?search=teste

3) Consultas avançadas:
    
    Você também pode fazer buscas por intervalo de datas, utilizando start date e end date, como o exemplo a seguir:

        - http://127.0.0.1:8000/logs/?start_date=2022-03-05&end_date=2022-08-25

    Sendo o padrão: Ano, Mês, Dia.

4) Para encerrar o sistema, basta dar o seguinte comando:
    
    -  docker-compose down


    
        
    







