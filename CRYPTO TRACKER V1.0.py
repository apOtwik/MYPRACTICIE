import requests
from datetime import datetime

print("""
 ********  **      **   **   **  **
    **     **      **   **   ** ** 
    **     **  **  **   **   ****  
    **      ** ** **    **   ** ** 
    **       **  **     **   **  **
""")
alpha = [
    "   ***     **      ******   **  **     ***  ",
    " **   **   **      **   **  **  **   **   ** ",
    " *******   **      ******   ******   *******",
    " **   **   **      **       **  **   **   ** ",
    " **   **   ******  **       **  **   **   ** "
]
for line in alpha:
    print(line)
print()
print('PRODUCED BY TWIK')

#WORK PLACE DONE!
def get_crypto_price(coin="bitcoin"):
    # Используем публичное API Coingecko
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, что запрос прошел успешно

        data = response.json()
        price = data[coin]['usd']

        return price
    except Exception as e:
        return f"Ошибка доступа: {e}"


def main():
    print("--- 🪙 CRYPTO TRACKER V1.0 ---")
    asset = "bitcoin"

    current_price = get_crypto_price(asset)
    time_now = datetime.now().strftime("%H:%M:%S")

    # Вайбовый вывод с форматированием
    print(f"[{time_now}] Текущий курс {asset.upper()}:")
    print(f"💰 ${current_price:,}")

    print("-" * 30)
    print("Статус: Мониторинг завершен успешно.")


if __name__ == "__main__":
    main()