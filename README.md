# Projeto.API.Bitcoin
<h4>Um script simples em Python que busca e registra o preço atual do Bitcoin da API da Coinbase a cada 15 segundos.</h4>
<ul>
  <li>Recursos: Busca o preço atual do Bitcoin em USD na API da Coinbase.
Registra o preço e quaisquer erros encontrados durante o processo de busca.
Intervalo configurável para buscar os dados.</li>
</ul>
<ol>
  
  <li><h3>Bibliotecas usadas:</h3></li>
  <ul>
    <li>Requests</li>
    <li>time</li>
    <li>logging</li>
  </ul>
  <li><h3>Instalando as bibliotecas necessárias</h3></li>
  <b>pip install requests </b>
  
  ![image](https://github.com/user-attachments/assets/585045bc-741c-40f6-9823-b404f59e1d73)



  
<li><h3>Bibliotecas</h3></li>
<ul>
  <li><b>Requests: </b>Biblioteca usada para fazer requisições HTTP. Aqui, ela é usada para chamar a API da Coinbase. </li>
  <li><b>time: </b> Biblioteca que permite manipulação de tempo, motivo de ter usado essa biblioteca foi porque eu queria que o código rodasse a cada 15 segundos.</li>
  <li><b>logging:</b>Biblioteca para registrar mensagens de log, que ajuda a monitorar e depurar o programa. Que no caso desse código, foi usado para mostrar a data e as horas de quando o código foi rodado. </li>
  
  ![image](https://github.com/user-attachments/assets/91a68993-cffe-43d5-ac5c-50ea7f3a81ec)

</ul>

<li><h3>Configurando o logging</h3></li>

![image](https://github.com/user-attachments/assets/d444be25-b3ed-4e1f-b444-6b4ecb992fa4)

<li><h3>Enfim criando a função</h3></li>


![image](https://github.com/user-attachments/assets/dfd7f76e-1941-4774-874d-c83eb4b9f8cf)



<ul>
  <li>try block: Tenta executar o código dentro dele, capturando exceções que possam ocorrer.</li>
  <li>url: URL da API Coinbase para obter o preço atual do Bitcoin.</li>
  <li>requests.get(url): Faz uma requisição HTTP GET para a URL fornecida.</li>
  <li>response.raise_for_status(): Verifica o status HTTP da resposta. Se houver um erro (status >= 400), lança uma exceção.</li>
  <li>dados = response.json(): Converte a resposta JSON da API para um dicionário Python.</li>
  <li>price: Extrai o valor do preço do Bitcoin da estrutura do JSON, usando .get() para evitar erros se a chave não existir.</li>
  <li>except requests.RequestException as e: Captura qualquer exceção que ocorra durante a requisição, registrando-a como erro.</li>
  <li> e por fim,o return None, que retorna None se houver um erro na requisição.</li>
</ul>

<li><h3>Função main()</h3></li>

![image](https://github.com/user-attachments/assets/4e215e2b-e8d1-40c6-a82c-9ff1c5f2ad80)


<ul>
  <li>interval: Define o intervalo de tempo (15 segundos) entre cada chamada à API.</li>
  <li>while True: Inicia um loop infinito que executará continuamente.</li>
  <li>extract_dados_bitcoin(): Chama a função para obter o preço do Bitcoin.</li>
  <li>if price: Verifica se price não é None (o que significa que a requisição foi bem-sucedida).</li>
  <li>logging.info(): Registra o preço do Bitcoin com nível de log INFO</li>
  <li>time.sleep(interval): Pausa a execução do loop por 15 segundos antes de começar novamente.</li>
</ul>

  
</ol>
