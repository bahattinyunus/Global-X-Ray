# Medeniyet Atlası - Otomasyon ve Geliştirici Makefile

PYTHON = python
TEST_SCRIPT = tests/test_integrity.py
CLI_SCRIPT = scripts/xray_cli.py
README_GEN = scripts/generate_master_readme.py
CULTURE_BUILDER = scripts/build_culture_dossiers.py
WEB_GEN = scripts/generate_web_atlas.py

.PHONY: all test readme culture cli stats web help briefing sim matrix clean

all: test

help:
	@echo "=========================================================="
	@echo "🏛️  MEDENİYET ATLASI - GELİŞTİRİCİ KOMUT REHBERİ"
	@echo "=========================================================="
	@echo "  make test      - Bütünlük ve veri doğrulama testlerini çalıştırır"
	@echo "  make web       - İnteraktif Web Atlası (index.html) oluşturur"
	@echo "  make briefing  - Türkiye yönetici istihbarat brifingini gösterir"
	@echo "  make sim       - Jeopolitik kriz & boğum simülatörünü listeler"
	@echo "  make matrix    - 9 medeniyet havzası ve felsefi güç matrisini açar"
	@echo "  make culture   - Kültür kütüphanesi dosyalarını derler"
	@echo "  make readme    - Master README.md dosyasını otomatik üretir"
	@echo "  make stats     - Küresel veri tabanı istatistiklerini gösterir"
	@echo "  make cli       - CLI terminalini interaktif/yardım modunda açar"
	@echo "=========================================================="

test:
	$(PYTHON) $(TEST_SCRIPT) -v

web:
	$(PYTHON) $(WEB_GEN)

briefing:
	$(PYTHON) $(CLI_SCRIPT) briefing turkiye

sim:
	$(PYTHON) $(CLI_SCRIPT) crisis-sim

matrix:
	$(PYTHON) $(CLI_SCRIPT) matrix

culture:
	$(PYTHON) $(CULTURE_BUILDER)

readme:
	$(PYTHON) $(README_GEN)

stats:
	$(PYTHON) $(CLI_SCRIPT) stats

cli:
	$(PYTHON) $(CLI_SCRIPT)
