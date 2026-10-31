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
        """countries/ dizini altındaki 205 bağımsız klasör ve README dosyaları doğrulanır."""
        countries_dir = BASE_DIR / "countries"
        self.assertTrue(countries_dir.exists(), "countries/ dizini bulunamadı!")
        
        country_folders = [d for d in countries_dir.iterdir() if d.is_dir()]
        self.assertGreaterEqual(len(country_folders), 205, "countries/ dizininde en az 205 ülke klasörü olmalıdır!")
        
        registry = self.datasets_dir / "countries_registry.json"
        with open(registry, "r", encoding="utf-8") as f:
            countries = json.load(f)

        for c in countries:
            c_dir = countries_dir / c["slug"]
            self.assertTrue(c_dir.exists(), f"countries/ altında {c['slug']} klasörü bulunamadı!")
            c_readme = c_dir / "README.md"
            self.assertTrue(c_readme.exists(), f"countries/{c['slug']} için README.md bulunamadı!")
            self.assertGreater(c_readme.stat().st_size, 1000, f"countries/{c['slug']} README.md boş veya yetersiz olamaz!")

    def test_economic_grouping_structure(self):
        """Ülkelerin ekonomilerine göre 8 ana gruba yapılandırılması doğrulanır."""
        expected_groups = [
            "01_ileri_sanayi_g7",
            "02_petro_ve_enerji_devleri",
            "03_gelismekte_olan_devler_ve_brics",
            "04_offshore_ve_finansal_merkezler",
            "05_kritik_maden_ve_hammadde",
            "06_orta_gelir_ve_ureticiler",
            "07_kirilgan_ve_borc_krizindekiler",
            "08_kucuk_ada_ve_turizm_ekonomileri"
        ]

        # 1. Kök dizindeki 8 grup klasörü ve README'leri
        for gid in expected_groups:
            grp_dir = BASE_DIR / gid
            self.assertTrue(grp_dir.exists(), f"Kök ekonomik grup klasörü bulunamadı: {gid}")
            grp_readme = grp_dir / "README.md"
            self.assertTrue(grp_readme.exists(), f"{gid} altında README.md bulunamadı!")
            self.assertGreater(grp_readme.stat().st_size, 500, f"{gid}/README.md yetersiz!")

        # 2. economies/ klasörü ve indeks
        eco_dir = BASE_DIR / "economies"
        self.assertTrue(eco_dir.exists(), "economies/ ana dizini bulunamadı!")
        self.assertTrue((eco_dir / "README.md").exists(), "economies/README.md bulunamadı!")

        # 3. Tüm 205 ülkenin ilgili ekonomik grup içinde varlığı
        registry = self.datasets_dir / "countries_registry.json"
        with open(registry, "r", encoding="utf-8") as f:
            countries = json.load(f)

        for c in countries:
            eco_path = BASE_DIR / c["economy_path"]
            self.assertTrue(eco_path.exists(), f"Ülkenin ekonomik grup klasörü bulunamadı: {c['economy_path']}")
            readme_path = eco_path / "README.md"
            self.assertTrue(readme_path.exists(), f"{c['economy_path']}/README.md bulunamadı!")

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

    def test_research_dossiers_exist_and_non_empty(self):
        """research/ altındaki derin istihbarat ve jeopolitik dosyalarının varlığı ve doluluğu kontrol edilir."""
        research_dir = BASE_DIR / "research"
        self.assertTrue(research_dir.exists(), "research/ dizini bulunamadı!")
        expected_dossiers = [
            "THEORETICAL_FRAMEWORKS.md",
            "SHADOW_BANKING_AND_OFFSHORE_FLOWS.md",
            "PROPAGANDA_AND_INFORMATION_WARFARE.md",
            "GEOPOLITICAL_CHOKEPOINTS_AND_CORRIDORS.md",
            "MILITARY_INDUSTRIAL_COMPLEX_AND_PMCS.md",
            "INTELLIGENCE_AGENCIES_AND_BLACK_OPS.md",
            "RESOURCE_WARS_AND_COMMODITY_SUPER_CARTELS.md",
            "WHISTLEBLOWERS_LEAKS_AND_FORENSIC_STANDARDS.md"
        ]
        for dossier in expected_dossiers:
            d_path = research_dir / dossier
            self.assertTrue(d_path.exists(), f"Eksik araştırma dosyası: {dossier}")
            self.assertGreater(d_path.stat().st_size, 3000, f"{dossier} dosyası kapsamlı ve en az 3KB olmalıdır!")

    def test_intelligence_and_offshore_datasets(self):
        """Yeni istihbarat teşkilatları ve vergi cennetleri datasetlerinin geçerliliği doğrulanır."""
        intel_file = self.datasets_dir / "intelligence_agencies_registry.json"
        offshore_file = self.datasets_dir / "offshore_havens_matrix.csv"

        self.assertTrue(intel_file.exists(), "intelligence_agencies_registry.json bulunamadı!")
        self.assertTrue(offshore_file.exists(), "offshore_havens_matrix.csv bulunamadı!")

        with open(intel_file, "r", encoding="utf-8") as f:
            intel_data = json.load(f)
            self.assertIn("agencies", intel_data)
            self.assertGreaterEqual(len(intel_data["agencies"]), 10)

        with open(offshore_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            self.assertGreaterEqual(len(rows), 15, "Vergi cennetleri matrisi en az 15 merkez içermelidir!")

    def test_rankings_and_methodology(self):
        """Metodoloji kılavuzları ve global sıralama raporu doğrulanır."""
        method_dir = BASE_DIR / "methodology"
        self.assertTrue((method_dir / "CORP_REGISTRY_RECONNAISSANCE.md").exists())
        self.assertTrue((method_dir / "DATA_COLLECTION_GUIDE.md").exists())
        self.assertTrue((method_dir / "OSINT_VERIFICATION.md").exists())

        matrix_file = self.datasets_dir / "global_power_matrix.json"
        report_file = self.datasets_dir / "GLOBAL_RANKINGS_REPORT.md"
        self.assertTrue(matrix_file.exists())
        self.assertTrue(report_file.exists())

        with open(matrix_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(len(data["countries"]), 205)

    def test_regional_dossiers_and_case_studies(self):
        """6 ana bölgenin README dosyaları ve dossiers/ altındaki derin vaka analizleri kontrol edilir."""
        expected_regions = ["middle_east", "europe", "asia", "americas", "africa", "oceania"]
        for reg in expected_regions:
            reg_readme = self.regions_dir / reg / "README.md"
            self.assertTrue(reg_readme.exists(), f"Eksik bölge dosyası: {reg}/README.md")
            self.assertGreater(reg_readme.stat().st_size, 1000, f"{reg}/README.md yetersiz!")

        dossiers_dir = BASE_DIR / "dossiers"
        self.assertTrue(dossiers_dir.exists(), "dossiers/ dizini bulunamadı!")
        expected_cases = [
            "CASE_STUDY_1MDB.md",
            "CASE_STUDY_MAGNITSKY_AND_TROIKA_LAUNDROMAT.md",
            "CASE_STUDY_ODEBRECHT_LAVA_JATO.md",
            "CASE_STUDY_PEGASUS_PROJECT.md"
        ]
        for case in expected_cases:
            case_path = dossiers_dir / case
            self.assertTrue(case_path.exists(), f"Eksik vaka analizi: {case}")
            self.assertGreater(case_path.stat().st_size, 2000, f"{case} dosyası en az 2KB olmalıdır!")

        # Yeni datasetler
        choke_file = self.datasets_dir / "chokepoints_registry.json"
        pmc_file = self.datasets_dir / "pmc_mercenary_groups.json"
        self.assertTrue(choke_file.exists())
        self.assertTrue(pmc_file.exists())

if __name__ == "__main__":
    unittest.main()
