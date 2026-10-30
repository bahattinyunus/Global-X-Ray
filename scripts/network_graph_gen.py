#!/usr/bin/env python3
"""
scripts/network_graph_gen.py
Küresel Röntgen - Oligark-Siyaset Güç Ağı Görselleştirici
Ülkenin 04_shadow_power_osint/oligarch_network.csv dosyasını okuyarak Mermaid veya DOT formatında ilişkiler şeması üretir.
"""

import sys
import csv
from pathlib import Path

# Windows console encoding fix
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass


def generate_mermaid_network(csv_path: Path) -> str:
    if not csv_path.exists():
        return f"Hata: {csv_path} bulunamadı."
        
    lines = ["```mermaid", "graph TD"]
    lines.append('  State["🏛️ Devlet / Siyasi İktidar"]')
    
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            entity = row.get("person_or_entity", f"Entity_{i}").replace('"', "")
            role = row.get("role_or_title", "").replace('"', "")
            sector = row.get("connected_sector", "").replace('"', "")
            conn = row.get("political_connection", "İlişkili").replace('"', "")
            wealth = row.get("estimated_wealth_usd_m", "")
            
            node_id = f"node_{i}"
            wealth_label = f" (${wealth}M)" if wealth and wealth != "0" else ""
            label = f'"{entity}<br/><i>{role}</i>{wealth_label}"'
            
            lines.append(f'  {node_id}[{label}]')
            lines.append(f'  State == "{conn}" ==> {node_id}')
            if sector:
                sector_id = f"sec_{i}"
                lines.append(f'  {sector_id}(["🏭 {sector}"])')
                lines.append(f'  {node_id} --- {sector_id}')
                
    lines.append("```")
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python network_graph_gen.py <oligarch_network.csv yolu>")
        print("Örnek: python network_graph_gen.py regions/asia/turkmenistan/04_shadow_power_osint/oligarch_network.csv")
        sys.exit(1)
        
    csv_file = Path(sys.argv[1])
    diagram = generate_mermaid_network(csv_file)
    print("\n" + diagram + "\n")

if __name__ == "__main__":
    main()
