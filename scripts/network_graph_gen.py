#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/network_graph_gen.py
Medeniyet Atlası - Oligark, Hanedan ve Siyaset Güç Ağı Görselleştirici
Ülkenin 04_shadow_power_osint/oligarch_network.csv dosyasını okuyarak Mermaid formatında güç ilişkileri şeması üretir.

Kullanım:
  python scripts/network_graph_gen.py <ulke_adi_veya_kodu>
  python scripts/network_graph_gen.py <csv_dosya_yolu>
  python scripts/network_graph_gen.py turkiye --save ag.mmd
"""

import sys
import json
import csv
from pathlib import Path

# Windows console encoding fix
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
REGISTRY_PATH = BASE_DIR / "global_datasets" / "countries_registry.json"

def find_country_csv(query: str):
    p = Path(query)
    if p.exists() and p.is_file():
        return p, p.stem

    if not REGISTRY_PATH.exists():
        return None, None

    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry = json.load(f)

    q = query.lower().strip()
    match = None
    for c in registry:
        if c["slug"] == q or c["name"].lower() == q or c["code"].lower() == q:
            match = c
            break
    if not match:
        for c in registry:
            if q in c["slug"] or q in c["name"].lower():
                match = c
                break

    if match:
        c_dir = BASE_DIR / match.get("economy_path", match.get("path", f"countries/{match['slug']}"))
        if not c_dir.exists():
            c_dir = BASE_DIR / match.get("path", f"countries/{match['slug']}")
        csv_path = c_dir / "04_shadow_power_osint" / "oligarch_network.csv"
        if csv_path.exists():
            return csv_path, match["name"]
    return None, None

def generate_mermaid_network(csv_path: Path, country_name: str = "Devlet / Siyasi İktidar") -> str:
    if not csv_path.exists():
        return f"Hata: {csv_path} bulunamadı."
        
    lines = ["```mermaid", "graph TD"]
    lines.append(f'  State["🏛️ {country_name} Siyasi Otoritesi / Güç Bloğu"]')
    lines.append('  classDef stateClass fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#fff;')
    lines.append('  classDef oligarchClass fill:#334155,stroke:#ef4444,stroke-width:2px,color:#fff;')
    lines.append('  classDef sectorClass fill:#0f172a,stroke:#10b981,stroke-width:1px,color:#94a3b8;')
    lines.append('  class State stateClass;')
    
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        count = 0
        for i, row in enumerate(reader):
            count += 1
            entity = row.get("person_or_entity", f"Entity_{i}").replace('"', "").replace("'", "")
            role = row.get("role_or_title", "").replace('"', "").replace("'", "")
            sector = row.get("connected_sector", "").replace('"', "").replace("'", "")
            conn = row.get("political_connection", "İlişkili").replace('"', "").replace("'", "")
            wealth = row.get("estimated_wealth_usd_m", "")
            
            node_id = f"node_{i}"
            wealth_label = f" (${wealth}M)" if wealth and wealth != "0" else ""
            label = f'"{entity}<br/><i>{role}</i>{wealth_label}"'
            
            lines.append(f'  {node_id}[{label}]')
            lines.append(f'  class {node_id} oligarchClass;')
            lines.append(f'  State == "{conn}" ==> {node_id}')
            if sector:
                sector_id = f"sec_{i}"
                lines.append(f'  {sector_id}(["🏭 {sector}"])')
                lines.append(f'  class {sector_id} sectorClass;')
                lines.append(f'  {node_id} --- {sector_id}')

    if count == 0:
        lines.append('  NoData["(Kayıtlı oligark veya paravan sermaye verisi yok)"]')
                
    lines.append("```")
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ["--help", "-h", "yardim"]:
        print(__doc__)
        sys.exit(0)
        
    target = sys.argv[1]
    csv_p, c_name = find_country_csv(target)
    
    if not csv_p:
        print(f"[-] Ülke veya ağ dosyası bulunamadı: '{target}'")
        sys.exit(1)

    diagram = generate_mermaid_network(csv_p, c_name or "Devlet")
    
    if len(sys.argv) > 3 and sys.argv[2] in ["--save", "-s", "--out", "-o"]:
        out_f = Path(sys.argv[3])
        out_f.write_text(diagram, encoding="utf-8")
        print(f"[+] Mermaid şeması başarıyla kaydedildi: {out_f.resolve()}")
    else:
        print(f"\n📊 {c_name} - Oligark & Siyaset Güç Ağı (Mermaid Grafiği):\n")
        print(diagram)
        print("\n")

if __name__ == "__main__":
    main()
