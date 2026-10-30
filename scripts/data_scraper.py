#!/usr/bin/env python3
"""
scripts/data_scraper.py
Küresel Röntgen - Açık Kaynak Veri Toplayıcı (Data Scraper)
Dünya Bankası, REST Countries ve açık API'lerden veri çekerek ülke dosyalarını günceller.
"""

import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

# Windows console encoding fix
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass


BASE_DIR = Path(__file__).resolve().parent.parent

def fetch_rest_countries(country_code: str) -> dict:
    """REST Countries API üzerinden temel ülke verilerini çeker."""
    url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    headers = {"User-Agent": "GlobalXRay-OSINT-Bot/1.0"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                return data[0] if isinstance(data, list) else data
    except urllib.error.URLError as e:
        print(f"[-] Hata: {url} çekilemedi: {e}", file=sys.stderr)
        return {}

def fetch_world_bank_indicator(country_code: str, indicator: str) -> list:
    """Dünya Bankası API'sinden makroekonomik indikatör verilerini çeker."""
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?format=json&per_page=5"
    headers = {"User-Agent": "GlobalXRay-OSINT-Bot/1.0"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                if len(data) > 1:
                    return data[1]
    except urllib.error.URLError as e:
        print(f"[-] Dünya Bankası verisi alınamadı ({indicator}): {e}", file=sys.stderr)
    return []

def main():
    print("=" * 60)
    print("🌐 Küresel Röntgen - Otomatik Açık Veri Entegratörü")
    print("=" * 60)
    
    if len(sys.argv) < 2:
        print("Kullanım: python data_scraper.py <ISO-2 veya ISO-3 Ülke Kodu>")
        print("Örnek: python data_scraper.py TUR")
        sys.exit(1)
        
    code = sys.argv[1].upper()
    print(f"[*] {code} için veriler sorgulanıyor...")
    country_data = fetch_rest_countries(code)
    
    if country_data:
        name = country_data.get("name", {}).get("common", code)
        capital = country_data.get("capital", ["Bilinmiyor"])[0] if country_data.get("capital") else "Bilinmiyor"
        population = country_data.get("population", 0)
        subregion = country_data.get("subregion", "Belirtilmemiş")
        print(f"[+] Ülke: {name}")
        print(f"[+] Başkent: {capital}")
        print(f"[+] Nüfus: {population:,}")
        print(f"[+] Bölge/Alt Bölge: {subregion}")
    else:
        print(f"[-] {code} için veri çekilemedi.")

if __name__ == "__main__":
    main()
