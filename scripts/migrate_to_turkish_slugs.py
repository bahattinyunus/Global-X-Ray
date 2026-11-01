# -*- coding: utf-8 -*-
"""
scripts/migrate_to_turkish_slugs.py
Migrates all country folder names across the repository to proper Turkish names (slugified),
and updates countries_registry.json, global_power_matrix.json, and press_freedom_real_index.json.
"""

import os
import sys
import json
import re
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "global_datasets"

def turkish_slug(name):
    mapping = {
        'ı': 'i', 'İ': 'i', 'I': 'i',
        'ş': 's', 'Ş': 's',
        'ğ': 'g', 'Ğ': 'g',
        'ü': 'u', 'Ü': 'u',
        'ö': 'o', 'Ö': 'o',
        'ç': 'c', 'Ç': 'c',
        'â': 'a', 'Â': 'a',
        'î': 'i', 'Î': 'i',
        'û': 'u', 'Û': 'u',
    }
    s = ''
    for ch in name:
        ch_lower = mapping.get(ch, ch.lower())
        if ch_lower.isalnum():
            s += ch_lower
        elif ch in [' ', '-', '_', '.', ',', '(', ')', "'", '’', '/']:
            s += '_'
    s = re.sub(r'_+', '_', s).strip('_')
    return s

def main():
    with open(DATASETS_DIR / "countries_registry.json", encoding="utf-8") as f:
        countries = json.load(f)

    with open(DATASETS_DIR / "global_power_matrix.json", encoding="utf-8") as f:
        matrix_data = json.load(f)

    with open(DATASETS_DIR / "press_freedom_real_index.json", encoding="utf-8") as f:
        press_data = json.load(f)

    slug_map = {}
    for c in countries:
        old_slug = c["slug"]
        new_slug = turkish_slug(c["name"])
        slug_map[old_slug] = new_slug

    print(f"Total countries to process: {len(countries)}")
    renamed_countries = 0
    renamed_regions = 0
    renamed_eco = 0

    # 1. Rename directories in countries/
    countries_dir = BASE_DIR / "countries"
    for old_slug, new_slug in slug_map.items():
        if old_slug != new_slug:
            old_p = countries_dir / old_slug
            new_p = countries_dir / new_slug
            if old_p.exists() and not new_p.exists():
                old_p.rename(new_p)
                renamed_countries += 1

    # 2. Rename directories in regions/<region>/
    regions_dir = BASE_DIR / "regions"
    for c in countries:
        old_slug = c["slug"]
        new_slug = slug_map[old_slug]
        region = c.get("region", "")
        if old_slug != new_slug and region:
            old_p = regions_dir / region / old_slug
            new_p = regions_dir / region / new_slug
            if old_p.exists() and not new_p.exists():
                old_p.rename(new_p)
                renamed_regions += 1

    # 3. Rename directories in economic blocks
    for c in countries:
        old_slug = c["slug"]
        new_slug = slug_map[old_slug]
        eco_id = c.get("economy_group_id", "")
        if old_slug != new_slug and eco_id:
            old_p = BASE_DIR / eco_id / old_slug
            new_p = BASE_DIR / eco_id / new_slug
            if old_p.exists() and not new_p.exists():
                old_p.rename(new_p)
                renamed_eco += 1

    print(f"Renamed in countries/: {renamed_countries}")
    print(f"Renamed in regions/: {renamed_regions}")
    print(f"Renamed in economic blocks: {renamed_eco}")

    # 4. Update countries_registry.json
    for c in countries:
        old_slug = c["slug"]
        new_slug = slug_map[old_slug]
        c["slug"] = new_slug
        c["path"] = f"countries/{new_slug}"
        c["economy_path"] = f"{c['economy_group_id']}/{new_slug}"

    with open(DATASETS_DIR / "countries_registry.json", "w", encoding="utf-8") as f:
        json.dump(countries, f, indent=2, ensure_ascii=False)
    print("Updated global_datasets/countries_registry.json")

    # 5. Update global_power_matrix.json
    for c in matrix_data.get("countries", []):
        old_slug = c.get("slug")
        if old_slug in slug_map:
            c["slug"] = slug_map[old_slug]

    with open(DATASETS_DIR / "global_power_matrix.json", "w", encoding="utf-8") as f:
        json.dump(matrix_data, f, indent=2, ensure_ascii=False)
    print("Updated global_datasets/global_power_matrix.json")

    # 6. Update press_freedom_real_index.json
    new_press_data = {}
    for old_k, v in press_data.items():
        new_k = slug_map.get(old_k, old_k)
        new_press_data[new_k] = v

    with open(DATASETS_DIR / "press_freedom_real_index.json", "w", encoding="utf-8") as f:
        json.dump(new_press_data, f, indent=2, ensure_ascii=False)
    print("Updated global_datasets/press_freedom_real_index.json")

if __name__ == "__main__":
    main()
