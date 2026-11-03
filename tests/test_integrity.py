#!/usr/bin/env python3
"""
tests/test_integrity.py
Medeniyet Atlası Veri Bütünlüğü ve Standart Uygunluk Testleri
"""

import unittest
import json
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class TestMedeniyetAtlasiIntegrity(unittest.TestCase):
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
            "regions/middle_east/turkiye",
            "regions/americas/amerika_birlesik_devletleri",
            "regions/asia/cin",
            "regions/europe/rusya"
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
            "WHISTLEBLOWERS_LEAKS_AND_FORENSIC_STANDARDS.md",
            "DE_DOLLARIZATION_AND_GEOECONOMIC_CURRENCY_WARS.md",
            "AI_SURVEILLANCE_ALGORITHMIC_WARFARE_AND_PALANTIR_NEXUS.md",
            "NARCO_KLEPTOCRACY_CARTEL_STATE_CONVERGENCE_AND_DRY_CORRIDORS.md",
            "BIOLOGICAL_WARFARE_GENOMICS_AND_DEEP_BIOSECURITY.md"
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
            "CASE_STUDY_PEGASUS_PROJECT.md",
            "CASE_STUDY_PANDORA_PAPERS_AND_OFFSHORE_SECRECY.md",
            "CASE_STUDY_NORD_STREAM_SABOTAGE_AND_ENERGY_WARFARE.md",
            "CASE_STUDY_OPERATION_GLADIO_AND_STAY_BEHIND_NETWORKS.md",
            "CASE_STUDY_BCCI_THE_BANK_OF_CROOKS_AND_CLINICS.md",
            "CASE_STUDY_STUXNET_OLYMPIC_GAMES_CYBER_SABOTAGE.md",
            "CASE_STUDY_CAMBRIDGE_ANALYTICA_AND_PSYCHOGRAPHIC_WARFARE.md",
            "CASE_STUDY_PROMIS_SOFTWARE_AND_INSLAW_AFFAIR.md",
            "CASE_STUDY_OPERATION_CYBERSCOOP_AND_PROJECT_RAVEN.md"
        ]
        for case in expected_cases:
            case_path = dossiers_dir / case
            self.assertTrue(case_path.exists(), f"Eksik vaka analizi: {case}")
            self.assertGreater(case_path.stat().st_size, 2000, f"{case} dosyası en az 2KB olmalıdır!")

        # Stratejik küresel veri setleri
        choke_file = self.datasets_dir / "chokepoints_registry.json"
        pmc_file = self.datasets_dir / "pmc_mercenary_groups.json"
        alliances_file = self.datasets_dir / "defense_alliances_and_treaties.json"
        sanctions_file = self.datasets_dir / "sanctions_and_embargoes_registry.json"
        minerals_file = self.datasets_dir / "critical_raw_materials_supply_chain.json"
        cables_file = self.datasets_dir / "subsea_cables_and_sigint_stations.json"
        swf_file = self.datasets_dir / "sovereign_wealth_funds_registry.json"
        darkfleet_file = self.datasets_dir / "shadow_fleet_maritime_registry.json"
        nuclear_file = self.datasets_dir / "nuclear_arsenals_and_triad_registry.json"
        armstrade_file = self.datasets_dir / "global_arms_trade_and_contractors.json"
        culture_file = self.datasets_dir / "cultural_codes_and_civilizations_registry.json"

        self.assertTrue(choke_file.exists(), "chokepoints_registry.json eksik!")
        self.assertTrue(pmc_file.exists(), "pmc_mercenary_groups.json eksik!")
        self.assertTrue(alliances_file.exists(), "defense_alliances_and_treaties.json eksik!")
        self.assertTrue(sanctions_file.exists(), "sanctions_and_embargoes_registry.json eksik!")
        self.assertTrue(minerals_file.exists(), "critical_raw_materials_supply_chain.json eksik!")
        self.assertTrue(cables_file.exists(), "subsea_cables_and_sigint_stations.json eksik!")
        self.assertTrue(swf_file.exists(), "sovereign_wealth_funds_registry.json eksik!")
        self.assertTrue(darkfleet_file.exists(), "shadow_fleet_maritime_registry.json eksik!")
        self.assertTrue(nuclear_file.exists(), "nuclear_arsenals_and_triad_registry.json eksik!")
        self.assertTrue(armstrade_file.exists(), "global_arms_trade_and_contractors.json eksik!")
        self.assertTrue(culture_file.exists(), "cultural_codes_and_civilizations_registry.json eksik!")

    def test_strategic_datasets_structure(self):
        """Yeni stratejik veri setlerinin JSON içerik ve şema bütünlüğü test edilir."""
        # 1. Alliances
        with open(self.datasets_dir / "defense_alliances_and_treaties.json", "r", encoding="utf-8") as f:
            alliances = json.load(f)
            self.assertIn("alliances", alliances)
            self.assertGreaterEqual(len(alliances["alliances"]), 8)

        # 2. Sanctions
        with open(self.datasets_dir / "sanctions_and_embargoes_registry.json", "r", encoding="utf-8") as f:
            sanctions = json.load(f)
            self.assertIn("targeted_states", sanctions)
            self.assertGreaterEqual(len(sanctions["targeted_states"]), 5)

        # 3. Minerals
        with open(self.datasets_dir / "critical_raw_materials_supply_chain.json", "r", encoding="utf-8") as f:
            minerals = json.load(f)
            self.assertIn("minerals", minerals)
            self.assertGreaterEqual(len(minerals["minerals"]), 7)

        # 4. Cables
        with open(self.datasets_dir / "subsea_cables_and_sigint_stations.json", "r", encoding="utf-8") as f:
            cables = json.load(f)
            self.assertIn("critical_cable_corridors", cables)
            self.assertIn("global_sigint_interception_stations", cables)

        # 5. SWF
        with open(self.datasets_dir / "sovereign_wealth_funds_registry.json", "r", encoding="utf-8") as f:
            swfs = json.load(f)
            self.assertIn("funds", swfs)
            self.assertGreaterEqual(len(swfs["funds"]), 10)

        # 6. Shadow Fleet
        with open(self.datasets_dir / "shadow_fleet_maritime_registry.json", "r", encoding="utf-8") as f:
            darkfleet = json.load(f)
            self.assertIn("fleet_metrics", darkfleet)
            self.assertIn("flags_of_convenience", darkfleet)
            self.assertIn("sts_transfer_chokepoints", darkfleet)
            self.assertGreaterEqual(len(cables["critical_cable_corridors"]), 4)

        # 7. Nuclear Arsenals & Triad
        with open(self.datasets_dir / "nuclear_arsenals_and_triad_registry.json", "r", encoding="utf-8") as f:
            nuclear = json.load(f)
            self.assertIn("strategic_overview", nuclear)
            self.assertIn("nuclear_powers", nuclear)
            self.assertEqual(len(nuclear["nuclear_powers"]), 9)
            self.assertIn("nato_nuclear_sharing", nuclear)

        # 8. Global Arms Trade & Contractors
        with open(self.datasets_dir / "global_arms_trade_and_contractors.json", "r", encoding="utf-8") as f:
            armstrade = json.load(f)
            self.assertIn("market_overview", armstrade)
            self.assertIn("top_prime_contractors", armstrade)
            self.assertGreaterEqual(len(armstrade["top_prime_contractors"]), 12)
            self.assertIn("top_exporters_vs_importers", armstrade)

        # 9. Cultural Codes & Civilizations
        with open(self.datasets_dir / "cultural_codes_and_civilizations_registry.json", "r", encoding="utf-8") as f:
            culture = json.load(f)
            self.assertIn("civilization_realms", culture)
            self.assertIn("countries_cultural_dna", culture)
            self.assertEqual(len(culture["civilization_realms"]), 9)
            self.assertEqual(len(culture["countries_cultural_dna"]), 205)

    def test_geopolitics_and_intelligence_dossiers(self):
        """geopolitics_and_intelligence/ altındaki 11 stratejik dosya ve README doğrulanır."""
        geo_dir = BASE_DIR / "geopolitics_and_intelligence"
        self.assertTrue(geo_dir.exists(), "geopolitics_and_intelligence/ dizini bulunamadı!")

        expected_files = [
            "README.md",
            "NUCLEAR_TRIAD_AND_STRATEGIC_ARSENALS.md",
            "GLOBAL_ARMS_TRADE_AND_MIC_OLIGOPOLY.md",
            "DEFENSE_ALLIANCES_AND_SECURITY_PACTS.md",
            "SANCTIONS_REGIMES_AND_BYPASS_CORRIDORS.md",
            "CRITICAL_RAW_MATERIALS_AND_REFINING_MONOPOLIES.md",
            "SUBSEA_CABLES_AND_GLOBAL_SIGINT_STATIONS.md",
            "SOVEREIGN_WEALTH_FUNDS_AND_STATE_CAPITALISM.md",
            "SHADOW_FLEET_MARITIME_AND_STS_HUBS.md",
            "MARITIME_CHOKEPOINTS_AND_TRANSIT_VULNERABILITIES.md",
            "PMC_MERCENARY_GROUPS_AND_PROXY_WARFARE.md",
            "GLOBAL_INTELLIGENCE_AGENCIES_AND_BLACK_BUDGETS.md"
        ]
        for fname in expected_files:
            fpath = geo_dir / fname
            self.assertTrue(fpath.exists(), f"Eksik jeopolitik/istihbarat dosyası: {fname}")
            self.assertGreater(fpath.stat().st_size, 1500, f"{fname} içeriği yetersiz veya boş olamaz!")

    def test_culture_dossiers(self):
        """culture/ altındaki medeniyet ve kültürel kodlar kütüphanesi dosyaları doğrulanır."""
        culture_dir = BASE_DIR / "culture"
        self.assertTrue(culture_dir.exists(), "culture/ dizini bulunamadı!")

        expected_files = [
            "README.md",
            "CIVILIZATION_REALMS_AND_PHILOSOPHIES.md",
            "UNTRANSLATABLE_CONCEPTS_ENCYCLOPEDIA.md",
            "GLOBAL_GASTRONOMY_AND_TABLE_RITUALS.md",
            "WORLD_ETIQUETTE_AND_TABOOS_GUIDE.md",
            "GLOBAL_FOLKLORE_MYTHOLOGY_AND_EPICS.md",
            "WORLD_ARCHITECTURE_AND_SACRED_SPACES.md",
            "GLOBAL_MUSIC_INSTRUMENTS_AND_SONIC_HERITAGE.md",
            "WORLD_FESTIVALS_CALENDARS_AND_RITUALS.md"
        ]
        for fname in expected_files:
            fpath = culture_dir / fname
            self.assertTrue(fpath.exists(), f"Eksik kültür dosyası: {fname}")
            self.assertGreater(fpath.stat().st_size, 1500, f"{fname} içeriği yetersiz veya boş olamaz!")

    def test_subdirectories_readme_indexes(self):
        """Tüm ana alt dizinlerde kapsamlı README.md indeks dosyalarının varlığı test edilir."""
        target_dirs = [
            "culture",
            "geopolitics_and_intelligence",
            "methodology",
            "research",
            "dossiers",
            "regions",
            "economies",
            "global_datasets",
            "scripts"
        ]
        for d in target_dirs:
            readme_path = BASE_DIR / d / "README.md"
            self.assertTrue(readme_path.exists(), f"{d}/README.md indeks dosyası bulunamadı!")
            self.assertGreater(readme_path.stat().st_size, 300, f"{d}/README.md içeriği yetersiz veya boş!")

    def test_artwork_images_integrity(self):
        """assets/images/ altındaki 17 kritik görselin varlığı ve boyutu test edilir."""
        images_dir = BASE_DIR / "assets" / "images"
        self.assertTrue(images_dir.exists(), "assets/images dizini bulunamadı!")
        expected_images = [
            "hero_banner.jpg",
            "4_layer_power_architecture.jpg",
            "world_civilizations_cultural_realms.jpg",
            "untranslatable_soul_concepts_wisdom.jpg",
            "global_gastronomy_table_rituals.jpg",
            "global_folklore_mythology_epics.jpg",
            "world_sacred_architecture_monuments.jpg",
            "intercultural_etiquette_and_greeting_rituals.jpg",
            "subsea_cables_and_cyber_sigint_nexus.jpg",
            "nuclear_triad_strategic_deterrence.jpg",
            "geopolitical_chokepoints.jpg",
            "offshore_kleptocracy_network.jpg",
            "cognitive_warfare_surveillance.jpg",
            "global_music_instruments_sonic_heritage.jpg",
            "world_festivals_and_sacred_rituals.jpg",
            "critical_raw_materials_semiconductors.jpg",
            "global_defense_alliances_security.jpg"
        ]
        for img in expected_images:
            img_path = images_dir / img
            self.assertTrue(img_path.exists(), f"Eksik görsel: assets/images/{img}")
            self.assertGreater(img_path.stat().st_size, 50000, f"Görsel boyutu çok küçük: {img}")

    def test_readme_all_artwork_images_referenced(self):
        """README.md dosyasında 17 eserin tamamının referans verildiği doğrulanır."""
        readme_path = BASE_DIR / "README.md"
        self.assertTrue(readme_path.exists(), "README.md bulunamadı!")
        readme_text = readme_path.read_text(encoding="utf-8")
        
        expected_images = [
            "hero_banner.jpg",
            "4_layer_power_architecture.jpg",
            "world_civilizations_cultural_realms.jpg",
            "untranslatable_soul_concepts_wisdom.jpg",
            "global_gastronomy_table_rituals.jpg",
            "global_folklore_mythology_epics.jpg",
            "world_sacred_architecture_monuments.jpg",
            "intercultural_etiquette_and_greeting_rituals.jpg",
            "subsea_cables_and_cyber_sigint_nexus.jpg",
            "nuclear_triad_strategic_deterrence.jpg",
            "geopolitical_chokepoints.jpg",
            "offshore_kleptocracy_network.jpg",
            "cognitive_warfare_surveillance.jpg",
            "global_music_instruments_sonic_heritage.jpg",
            "world_festivals_and_sacred_rituals.jpg",
            "critical_raw_materials_semiconductors.jpg",
            "global_defense_alliances_security.jpg"
        ]
        for img in expected_images:
            self.assertIn(f"assets/images/{img}", readme_text, f"README.md içinde {img} referansı eksik!")

    def test_xray_cli_capabilities(self):
        """xray_cli.py modülünün ve yeni yeteneklerinin (rank, export, stats, json) doğrulanması."""
        import subprocess
        
        # 1. stats --json
        res_stats = subprocess.run(["python", str(BASE_DIR / "scripts" / "xray_cli.py"), "stats", "--json"], capture_output=True, encoding="utf-8")
        self.assertEqual(res_stats.returncode, 0, f"CLI stats başarısız: {res_stats.stderr}")
        stats_obj = json.loads(res_stats.stdout)
        self.assertEqual(stats_obj["country_count"], 205)
        self.assertEqual(stats_obj["artwork_images_count"], 17)

        # 2. rank gdp 5 --json
        res_rank = subprocess.run(["python", str(BASE_DIR / "scripts" / "xray_cli.py"), "rank", "gdp", "5", "--json"], capture_output=True, encoding="utf-8")
        self.assertEqual(res_rank.returncode, 0, f"CLI rank başarısız: {res_rank.stderr}")
        rank_arr = json.loads(res_rank.stdout)
        self.assertEqual(len(rank_arr), 5)
        self.assertEqual(rank_arr[0]["code"], "USA")

        # 3. export turkiye --format json
        res_exp = subprocess.run(["python", str(BASE_DIR / "scripts" / "xray_cli.py"), "export", "turkiye", "--format", "json"], capture_output=True, encoding="utf-8")
        self.assertEqual(res_exp.returncode, 0, f"CLI export başarısız: {res_exp.stderr}")
        exp_obj = json.loads(res_exp.stdout)
        self.assertEqual(exp_obj["metadata"]["code"], "TUR")
        self.assertIn("cultural_dna", exp_obj)

        # 4. graph turkiye
        res_graph = subprocess.run(["python", str(BASE_DIR / "scripts" / "xray_cli.py"), "graph", "turkiye"], capture_output=True, encoding="utf-8")
        self.assertEqual(res_graph.returncode, 0, f"CLI graph başarısız: {res_graph.stderr}")
        self.assertIn("graph TD", res_graph.stdout)
        self.assertIn("Cengiz Holding", res_graph.stdout)

    def test_interactive_web_atlas_integrity(self):
        """index.html dosyasının varlığı, boyutu ve veri bütünlüğü doğrulanır."""
        web_path = BASE_DIR / "index.html"
        self.assertTrue(web_path.exists(), "index.html bulunamadı! 'python scripts/generate_web_atlas.py' çalıştırılmalı.")
        self.assertGreater(web_path.stat().st_size, 500000, "index.html boyutu 500KB'den küçük olamaz!")
        
        html_text = web_path.read_text(encoding="utf-8")
        self.assertIn("MEDENİYET ATLASI", html_text)
        self.assertIn("TUR", html_text)
        self.assertIn("Gönül", html_text)
        self.assertIn("critical_raw_materials_semiconductors.jpg", html_text)
        self.assertIn("tab-simulator", html_text)
        self.assertIn("exportFilteredCSV", html_text)
        self.assertIn("hormuz_blockade", html_text)
        self.assertIn("currency-tbody", html_text)
        self.assertIn("apt-units-grid", html_text)
        self.assertIn("mBridge", html_text)

    def test_geopolitical_crisis_scenarios_dataset(self):
        """geopolitical_crisis_scenarios.json dosyasının varlığı ve senaryo yapısı doğrulanır."""
        crisis_path = self.datasets_dir / "geopolitical_crisis_scenarios.json"
        self.assertTrue(crisis_path.exists(), "geopolitical_crisis_scenarios.json bulunamadı!")
        
        with open(crisis_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        scenarios = data.get("scenarios", [])
        self.assertGreaterEqual(len(scenarios), 8, "En az 8 kriz senaryosu bulunmalıdır!")
        
        required_keys = ["id", "title", "severity", "category", "core_trigger", "strategic_exposure", "most_vulnerable_countries", "mitigation_corridors"]
        for s in scenarios:
            for k in required_keys:
                self.assertIn(k, s, f"{s.get('id', 'Bilinmeyen')} senaryosunda '{k}' alanı eksik!")
            self.assertGreater(len(s["most_vulnerable_countries"]), 0, f"{s['id']} için en az 1 etkilenen ülke tanımlanmalıdır!")

    def test_cli_briefing_and_crisis_sim(self):
        """CLI briefing, crisis-sim ve matrix komutlarının çıktısı ve JSON modu doğrulanır."""
        import subprocess
        
        # 1. briefing turkiye --json
        res_brf = subprocess.run(["python", str(BASE_DIR / "scripts" / "xray_cli.py"), "briefing", "turkiye", "--json"], capture_output=True, encoding="utf-8")
        self.assertEqual(res_brf.returncode, 0, f"CLI briefing başarısız: {res_brf.stderr}")
        brf_obj = json.loads(res_brf.stdout)
        self.assertEqual(brf_obj["country"]["code"], "TUR")
        self.assertIn("cultural_dna", brf_obj)
        self.assertIn("alliances", brf_obj)
        
        # 2. crisis-sim hormuz_blockade --json
        res_sim = subprocess.run(["python", str(BASE_DIR / "scripts" / "xray_cli.py"), "crisis-sim", "hormuz_blockade", "--json"], capture_output=True, encoding="utf-8")
        self.assertEqual(res_sim.returncode, 0, f"CLI crisis-sim başarısız: {res_sim.stderr}")
        sim_arr = json.loads(res_sim.stdout)
        self.assertTrue(any(s["id"] == "hormuz_blockade" for s in sim_arr))
        
        # 3. matrix --json
        res_mat = subprocess.run(["python", str(BASE_DIR / "scripts" / "xray_cli.py"), "matrix", "--json"], capture_output=True, encoding="utf-8")
        self.assertEqual(res_mat.returncode, 0, f"CLI matrix başarısız: {res_mat.stderr}")
        mat_arr = json.loads(res_mat.stdout)
        self.assertEqual(len(mat_arr), 9, "9 küresel medeniyet havzası bulunmalıdır!")

    def test_currency_and_dedollarization_dataset(self):
        """currency_hegemony_and_dedollarization.json dosyasının varlığı ve bütünlüğü doğrulanır."""
        curr_path = self.datasets_dir / "currency_hegemony_and_dedollarization.json"
        self.assertTrue(curr_path.exists(), "currency_hegemony_and_dedollarization.json bulunamadı!")
        
        with open(curr_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        currencies = data.get("global_reserve_currencies", [])
        networks = data.get("alternative_clearing_networks", [])
        gold = data.get("top_central_bank_gold_buyers_metric_tons", [])
        
        self.assertGreaterEqual(len(currencies), 5, "En az 5 rezerv para tanımlanmalıdır!")
        self.assertGreaterEqual(len(networks), 4, "CIPS, SPFS, mBridge, BRICS_Pay ağları bulunmalıdır!")
        self.assertGreaterEqual(len(gold), 5, "En az 5 merkez bankası altın alıcısı listelenmelidir!")

    def test_cognitive_warfare_and_cyber_dataset(self):
        """cognitive_warfare_and_cyber_arsenals.json dosyasının varlığı ve bütünlüğü doğrulanır."""
        cyber_path = self.datasets_dir / "cognitive_warfare_and_cyber_arsenals.json"
        self.assertTrue(cyber_path.exists(), "cognitive_warfare_and_cyber_arsenals.json bulunamadı!")
        
        with open(cyber_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        apts = data.get("apt_units", [])
        spyware = data.get("commercial_spyware_cartel", [])
        
        self.assertGreaterEqual(len(apts), 6, "En az 6 küresel APT grubu tanımlanmalıdır!")
        self.assertGreaterEqual(len(spyware), 3, "Pegasus, Predator, Candiru casus yazılımları bulunmalıdır!")

    def test_cli_currency_cyber_and_audit(self):
        """CLI currency, cyber ve audit komutlarının JSON çıktı bütünlüğü doğrulanır."""
        import subprocess
        
        # 1. currency --json
        res_curr = subprocess.run(["python", str(BASE_DIR / "scripts" / "xray_cli.py"), "currency", "--json"], capture_output=True, encoding="utf-8")
        self.assertEqual(res_curr.returncode, 0, f"CLI currency başarısız: {res_curr.stderr}")
        curr_obj = json.loads(res_curr.stdout)
        self.assertIn("global_reserve_currencies", curr_obj)
        
        # 2. cyber --json
        res_cyb = subprocess.run(["python", str(BASE_DIR / "scripts" / "xray_cli.py"), "cyber", "--json"], capture_output=True, encoding="utf-8")
        self.assertEqual(res_cyb.returncode, 0, f"CLI cyber başarısız: {res_cyb.stderr}")
        cyb_obj = json.loads(res_cyb.stdout)
        self.assertIn("apt_units", cyb_obj)
        
        # 3. audit turkiye --json
        res_aud = subprocess.run(["python", str(BASE_DIR / "scripts" / "xray_cli.py"), "audit", "turkiye", "--json"], capture_output=True, encoding="utf-8")
        self.assertEqual(res_aud.returncode, 0, f"CLI audit başarısız: {res_aud.stderr}")
        aud_obj = json.loads(res_aud.stdout)
        self.assertEqual(aud_obj["country"]["code"], "TUR")
        self.assertIn("csfi_fragility", aud_obj)

    def test_case_studies_and_research_counts(self):
        """dossiers/ ve research/ altındaki dosyaların asgari sayıları doğrulanır."""
        dossiers_dir = BASE_DIR / "dossiers"
        research_dir = BASE_DIR / "research"
        cases = list(dossiers_dir.glob("CASE_STUDY_*.md"))
        theses = [f for f in research_dir.glob("*.md") if f.name != "README.md"]
        self.assertGreaterEqual(len(cases), 12, "En az 12 adli vaka analizi bulunmalıdır!")
        self.assertGreaterEqual(len(theses), 12, "En az 12 araştırma tezi bulunmalıdır!")

if __name__ == "__main__":
    unittest.main()
