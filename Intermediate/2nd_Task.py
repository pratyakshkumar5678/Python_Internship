import sys
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape(url, selector, max_items=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    items = soup.select(selector)
    results = []
    for i, el in enumerate(items):
        if max_items and i >= max_items:
            break
        text = el.get_text(strip=True)
        href = el.get("href") if el.has_attr("href") else ""
        href = urljoin(url, href)
        results.append({"text": text, "url": href})
    return results

def save_csv(rows, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "url"])
        writer.writeheader()
        writer.writerows(rows)

def main():
    if len(sys.argv) < 4:
        print("Usage: python 2nd_Task .py <url> <css-selector> <output.csv> [max_items]")
        sys.exit(1)
    url = sys.argv[1]
    selector = sys.argv[2]
    out = sys.argv[3]
    max_items = int(sys.argv[4]) if len(sys.argv) > 4 else None
    rows = scrape(url, selector, max_items)
    save_csv(rows, out)
    print(f"Saved {len(rows)} items to {out}")

if __name__ == "__main__":
    main()
