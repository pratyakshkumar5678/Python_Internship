import requests
from datetime import datetime, timezone

API = "https://api.coingecko.com/api/v3/simple/price"

def fetch_prices(ids, vs_currency="usd"):
    params = {"ids": ",".join(ids), "vs_currencies": vs_currency, "include_24hr_change": "true"}
    r = requests.get(API, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def pretty_print(data, vs_currency="usd"):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"Prices at {now}\n")
    for coin, info in data.items():
        price = info.get(vs_currency)
        change = info.get(f"{vs_currency}_24h_change")
        print(f"{coin:12} : {price} {vs_currency.upper()}  (24h change: {change:.2f}%)")

def main():
    print("--- Crypto Price Checker ---")
    print("Enter coin IDs separated by spaces (e.g., bitcoin ethereum dogecoin)")
    
    while True:
        user_input = input("\nEnter coin IDs or 'q' to quit: ").strip()

        if user_input.lower() in ['q', 'quit', 'exit']:
            print("Exiting program. Goodbye!")
            break
            
        if not user_input:
            continue
        ids = [id.strip().lower() for id in user_input.split()]
        price_data = fetch_prices(ids)
        if price_data is not None:
            pretty_print(price_data)
        
        print("\n" + "-"*50)

if __name__ == "__main__":
    main()
