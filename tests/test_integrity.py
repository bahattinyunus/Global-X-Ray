#!/usr/bin/env python3
"""
tests/test_integrity.py
Küresel Röntgen Veri Bütünlüğü ve Standart Uygunluk Testleri
"""

import unittest
import json
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class TestGlobalXRayIntegrity(unittest.TestCase):
    def setUp(self):
        self.regions_dir = BASE_DIR / "regions"
        self.datasets_dir = BASE_DIR / "global_datasets"
        
    def test_global_datasets_exist(self):
        """Temel küresel dataset dosyalarının varlığı ve geçerliliği kontrol edilir."""
        registry = self.datasets_dir / "countries_registry.json"
        shadow = self.datasets_dir / "global_shadow_economy.csv"
        press = self.datasets_dir / "press_freedom_real_index.json"
        
        self.assertTrue(registry.exists(), "countries_registry.json bulunamadı!")
        self.assertTrue(shadow.exists(), "global_shadow_economy.csv bulunamadı!")
        self.assertTrue(press.exists(), "press_freedom_real_index.json bulunamadı!")
        
        # JSON syntax kontrolü
        with open(registry, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertIsInstance(data, list)
            self.assertGreaterEqual(len(data), 190, "Kayıtlı ülke sayısı 190'dan az olamaz!")

    def test_country_directory_structure(self):
        """Her ülkenin 4 katman ve 8 standart dosyaya sahip olduğu doğrulanır."""
        registry = self.datasets_dir / "countries_registry.json"
        with open(registry, "r", encoding="utf-8") as f:
            countries = json.load(f)
            
        required_files = [
            "README.md",
            "01_culture_demographics/society_history.md",
            "01_culture_demographics/demographics.csv",
            "02_official_state/constitution_gov.md",
            "03_official_economy/macroeconomics.json",
            "04_shadow_power_osint/real_power_dynamics.md",
            "04_shadow_power_osint/oligarch_network.csv",
            "04_shadow_power_osint/media_censorship_matrix.md"
        ]
        
        for c in countries:
            c_dir = BASE_DIR / c["path"]
            self.assertTrue(c_dir.exists(), f"Ülke klasörü bulunamadı: {c_dir}")
            
            for rf in required_files:
                fpath = c_dir / rf
                self.assertTrue(fpath.exists(), f"{c['name']} için eksik dosya: {rf}")
                self.assertGreater(fpath.stat().st_size, 0, f"{fpath} dosyası boş olamaz!")

    def test_direct_countries_directory(self):
        """countries/ dizini ve ana kök dizin altındaki 205 bağımsız klasör ve README dosyaları doğrulanır."""
        countries_dir = BASE_DIR / "countries"
        self.assertTrue(countries_dir.exists(), "countries/ dizini bulunamadı!")
        
        country_folders = [d for d in countries_dir.iterdir() if d.is_dir()]
        self.assertGreaterEqual(len(country_folders), 205, "countries/ dizininde en az 205 ülke klasörü olmalıdır!")
        
        registry = self.datasets_dir / "countries_registry.json"
        with open(registry, "r", encoding="utf-8") as f:
            countries = json.load(f)

        for c in countries:
            # Hem countries/ hem kök dizindeki klasör ve README doğrulanır
            root_c_dir = BASE_DIR / c["slug"]
            self.assertTrue(root_c_dir.exists(), f"Kök dizinde {c['slug']} klasörü bulunamadı!")
            root_readme = root_c_dir / "README.md"
            self.assertTrue(root_readme.exists(), f"Kök {c['slug']} için README.md bulunamadı!")
            self.assertGreater(root_readme.stat().st_size, 1000, f"Kök {c['slug']} README.md boş veya yetersiz olamaz!")

    def test_macroeconomics_json_validity(self):
        """Kritik ülkelerin macroeconomics.json dosyalarının doğruluğu."""
        sample_countries = [
            "regions/middle_east/turkey",
            "regions/americas/united_states",
            "regions/asia/china",
            "regions/europe/russia"
        ]
        for c_rel in sample_countries:
            m_path = BASE_DIR / c_rel / "03_official_economy" / "macroeconomics.json"
            with open(m_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.assertIn("gdp_nominal_billion_usd", data)
                self.assertIn("top_exports", data)
                self.assertIn("shadow_economy_pct_gdp", data)

if __name__ == "__main__":
    unittest.main()
