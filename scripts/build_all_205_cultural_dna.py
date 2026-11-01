# -*- coding: utf-8 -*-
"""
scripts/build_all_205_cultural_dna.py
Combines the existing 60 cultural DNA entries with the 145 new entries
to form the complete 205-nation Cultural DNA and Civilizations Registry.
"""

import json
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "global_datasets"

# Import regional datasets
from data_europe_26 import EUROPE_26
from data_middle_east_11 import MIDDLE_EAST_11
from data_asia_21 import ASIA_21
from data_americas_26 import AMERICAS_26
from data_oceania_13 import OCEANIA_13
from data_africa_part1_24 import AFRICA_PART1_24
from data_africa_part2_24 import AFRICA_PART2_24

with open(DATA_DIR / "countries_registry.json", "r", encoding="utf-8") as f:
    countries_registry = json.load(f)

expected_codes = {c["code"]: c["name"] for c in countries_registry}
print(f"[INFO] Expected total countries from registry: {len(expected_codes)}")

with open(DATA_DIR / "cultural_codes_and_civilizations_registry.json", "r", encoding="utf-8") as f:
    culture_registry = json.load(f)

existing_entries = culture_registry.get("countries_cultural_dna", [])
existing_codes = {c["code"]: c for c in existing_entries}
print(f"[INFO] Existing entries in cultural registry: {len(existing_codes)}")

all_new = (
    EUROPE_26 +
    MIDDLE_EAST_11 +
    ASIA_21 +
    AMERICAS_26 +
    OCEANIA_13 +
    AFRICA_PART1_24 +
    AFRICA_PART2_24
)
print(f"[INFO] Newly prepared entries: {len(all_new)}")

# Verify all new codes are valid and not duplicates
seen = set(existing_codes.keys())
added_count = 0
for entry in all_new:
    code = entry["code"]
    if code not in expected_codes:
        print(f"[WARNING] Unknown country code in new data: {code} ({entry.get('country')})")
    if code in seen:
        print(f"[WARNING] Duplicate country code: {code} ({entry.get('country')})")
    seen.add(code)
    existing_codes[code] = entry
    added_count += 1

print(f"[SUCCESS] Combined total unique country entries: {len(existing_codes)}")

# Reorder according to countries_registry sequence
ordered_dna = []
missing_from_final = []
for c in countries_registry:
    code = c["code"]
    if code in existing_codes:
        ordered_dna.append(existing_codes[code])
    else:
        missing_from_final.append(f"{c['name']} ({code})")

if missing_from_final:
    print(f"[ERROR] Missing {len(missing_from_final)} countries: {missing_from_final}")
    sys.exit(1)

culture_registry["countries_cultural_dna"] = ordered_dna

# Save updated registry
with open(DATA_DIR / "cultural_codes_and_civilizations_registry.json", "w", encoding="utf-8") as f:
    json.dump(culture_registry, f, ensure_ascii=False, indent=2)

print(f"[COMPLETE] Saved {len(ordered_dna)} countries into cultural_codes_and_civilizations_registry.json with 100% coverage!")
