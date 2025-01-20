import requests
import time
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def extract_dados_bitcoin():
    try:
        url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para status de erro
        dados = response.json()
        price = dados.get('data', {}).get('amount', 'N/A')
        return price
    except requests.RequestException as e:
        logging.error(f"Erro ao acessar a API: {e}")
        return None

def main():
    interval = 15  # Intervalo de 15 segundos
    while True:
        price = extract_dados_bitcoin()
        if price:
            logging.info(f"Preço atual do Bitcoin: ${price}")
        time.sleep(interval)

if __name__ == "__main__":
    main()
