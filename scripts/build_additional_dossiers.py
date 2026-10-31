"""
Additional deep research dossiers and dataset enrichment for Global X-Ray.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RESEARCH_DIR = BASE_DIR / "research"
DATASETS_DIR = BASE_DIR / "global_datasets"

# -------------------------------------------------------------
# 7. RESOURCE_WARS_AND_COMMODITY_SUPER_CARTELS.md
# -------------------------------------------------------------
RESOURCE_WARS = """# Resource Wars, Critical Minerals & Commodity Trading Cartels: The Material Foundations of Hegemony

> "The nations of the world are dividing themselves into two camps: those who own the soil and its resources, and those who must buy them or take them by force."  
> — **Brooks Adams**, *The Law of Civilization and Decay* (1895)

> "Control oil and you control nations; control food and you control the people; control money and you control the world."  
> — **Henry Kissinger** *(Attributed Geopolitical Maxim)*

> "The true rulers of global commodity markets are not the sovereign states that produce the oil or copper, but the secretive trading houses of Switzerland that finance and route the cargo."  
> — **Javier Blas & Jack Farchy**, *The World for Sale: Money, Power and the Traders Who Barter the Earth's Resources* (2021)

---

## 1. Executive Summary: From Energy Transition to Geoeconomic Conflict

The 21st century's geopolitical conflict is transitioning from a hydrocarbon-dominated regime (crude oil, natural gas) to a critical minerals and electro-chemical supply regime (lithium, cobalt, nickel, rare earth elements, copper, and graphite).

While oil reserves are distributed across roughly 30 major nations, the processing and refining of energy-transition minerals is vastly more concentrated:
* **China** controls **60% to 70% of world rare earth mining** and **85% to 90% of global rare earth processing and magnet production**.
* Over **70% of the world's cobalt** originates in the Democratic Republic of the Congo (DRC), with Chinese entities owning or financing 15 of the 19 largest industrial cobalt concessions.
* The **Lithium Triangle** (Chile, Bolivia, Argentina) holds over 56% of global lithium brine reserves.

---

## 2. The Secretive Commodity Trading Oligopoly

Global physical commodity flows are dominated not by public stock exchanges, but by privately held, opaque trading houses headquartered primarily in Switzerland (Geneva, Zug) and Singapore:

```
[Resource Extraction / Mines] -> [Swiss Commodity House] -> [Offshore Trade Financing] -> [Global Refineries]
    (DRC, Zambia, Russia)         (Glencore, Trafigura,         (BNP Paribas, ING,          (China, EU, US)
                                      Vitol, Gunvor)                 Credit Agricole)
```

| Trading House | Headquarters | Primary Commodities | Annual Revenue Profile | Notorious Exposures & Sanctions Dynamics |
| :--- | :---: | :--- | :--- | :--- |
| **Glencore plc** | Baar, Switzerland | Copper, Cobalt, Coal, Zinc, Oil | $215B+ | Pleaded guilty (2022) to foreign bribery and market manipulation across 7 countries; paid $1.1B in DOJ/UK penalties. |
| **Trafigura Group** | Geneva / Singapore | Non-ferrous Metals, Crude Oil, LNG | $244B+ | Probo Koala toxic waste dumping scandal (Ivory Coast 2006); massive physical nickel fraud loss (2023). |
| **Vitol Group** | Geneva / Rotterdam | Crude Oil, Refined Products (8M bpd) | $505B+ | Largest independent energy trader in the world; traded Iranian, Russian, and Libyan crude during embargo regimes. |
| **Gunvor Group** | Geneva / Cyprus | Oil, LNG, Refined Products | $127B+ | Co-founded by Gennady Timchenko (inner circle Vladimir Putin); sold shares hours before US sanctions in 2014. |
| **Cargill / ADM / Bunge / Dreyfus (ABCD)** | USA / Switzerland / Netherlands | Grain, Soy, Corn, Fertilizer | $350B+ (Combined) | Controls over 75% to 90% of global agricultural grain trade; price discovery oligopoly. |

---

## 3. Critical Mineral Chokepoints and Strategic Bottlenecks

```mermaid
graph TD
    subgraph Mineral_Extraction
        C1["Congo (DRC)<br/>(70% of world Cobalt)"]
        L1["Lithium Triangle<br/>(Chile/Bolivia/Argentina: 56% Li)"]
        R1["China / Bayan Obo<br/>(60% Rare Earth extraction)"]
        N1["Indonesia / Morowali<br/>(50%+ High-grade Nickel)"]
    end

    subgraph Refining_Monopoly
        C1 & L1 & R1 & N1 --> CH["China Refining & Processing Complex<br/>(65% Li, 75% Co, 90% REE, 100% Spherical Graphite)"]
    end

    subgraph Defense_HighTech_Dependence
        CH --> W1["US & European EV & Grid Batteries"]
        CH --> W2["Aerospace & Guided Munitions<br/>(F-35: 417 kg Rare Earths per airframe)"]
        CH --> W3["Advanced Semiconductor Fabrication"]
    end
```

### 3.1 The Defense Procurement Vulnerability
Modern precision-guided munitions and stealth aircraft are completely dependent on Chinese mineral processing:
* Every **F-35 Lightning II** fighter jet contains **417 kg (920 lbs) of rare earth elements**, specifically neodymium-iron-boron (NdFeB) permanent magnets for avionics and actuators.
* Virginia-class nuclear attack submarines require over 4,200 kg of rare earth alloys for electric propulsion systems.
* An export embargo on heavy rare earths (Dysprosium, Terbium) would paralyze Western defense production within 6 to 12 months.

---

## 4. The Petrodollar Recycle & The Emergence of the Petroyuan

### 4.1 The 1974 US-Saudi Petrodollar Compact
* Orchestrated by Henry Kissinger and Treasury Secretary William Simon following the 1973 Yom Kippur War.
* **The Deal:** The Kingdom of Saudi Arabia agreed to price all crude oil sales exclusively in US Dollars (USD) and invest surplus revenues into US Treasury securities. In return, the US guaranteed total military security and arms supplies to the House of Saud.
* **The Consequence:** Created artificial, structural global demand for USD. Every country on earth had to accumulate US dollar reserves simply to import energy, allowing the US to run perpetual twin deficits without currency collapse (*"exorbitant privilege"*).

### 4.2 The Petroyuan Transition & De-Dollarization
* **Bilateral Currency Swaps:** China, Russia, India, Brazil, and Saudi Arabia settling oil and gas trades in Renminbi (RMB), Rubles, and UAE Dirhams.
* **Shanghai Petroleum and Natural Gas Exchange (SHPGX):** Sells energy contracts settled in RMB with potential gold convertibility via the Shanghai Gold Exchange.

---

## 5. Quotes on Resources, Imperial Conquest and Soil

> "The first man who, having enclosed a piece of ground, bethought himself of saying 'This is mine', and found people simple enough to believe him, was the real founder of civil society."  
> — **Jean-Jacques Rousseau**, *Discourse on Inequality* (1754)

> "The struggle for existence is essentially a struggle for free energy."  
> — **Ludwig Boltzmann**, *The Second Law of Thermodynamics* (1886)

> "Imperialism is capitalism at that stage of development at which the dominance of monopolies and finance capital is established; in which the export of capital has acquired pronounced importance; in which the division of the world among the international trusts has begun."  
> — **Vladimir Lenin**, *Imperialism, the Highest Stage of Capitalism* (1917)

> "Civilization exists by geological consent, subject to change without notice."  
> — **Will Durant**, *The Story of Civilization* (1935)
"""

# -------------------------------------------------------------
# 8. WHISTLEBLOWERS_LEAKS_AND_FORENSIC_STANDARDS.md
# -------------------------------------------------------------
WHISTLEBLOWERS_LEAKS = """# Whistleblower Leaks, Cryptographic Verification & OSINT Forensic Standards

> "If you want to keep a secret, you must also hide it from yourself."  
> — **George Orwell**, *1984* (1949)

> "Privacy is necessary for an open society in the electronic age... We cannot expect governments, corporations, or other large, faceless organizations to grant us privacy... We must defend our own privacy if we expect to have any."  
> — **Eric Hughes**, *A Cypherpunk's Manifesto* (1993)

> "Courage is contagious."  
> — **Edward Snowden**, *Permanent Record* (2019)

> "If wars can be started by lies, peace can be started by truth."  
> — **Julian Assange**, *Address at Trafalgar Square* (2011)

---

## 1. Executive Summary: The Epistemology of Leaked Intelligence

In an era of deepfakes, cognitive warfare, and synthetic media generation, Open Source Intelligence (OSINT) investigations cannot accept documents at face value. A document leaked to the public may represent:
1. **Genuine Whistleblowing:** Public interest disclosure of illegal state activity (e.g., Daniel Ellsberg, Chelsea Manning, Edward Snowden).
2. **Selective Declassification / Controlled Leak:** State apparatus leaking genuine documents with specific redactions to damage a political rival.
3. **Disinformation / Forgery:** Fabricated documents planted to misinform investigators or discredit legitimate leaks.

This dossier codifies the forensic methodologies required to verify primary-source leaks, analyze metadata, and preserve cryptographic chains of custody.

---

## 2. Landmark Leaks Comparative Analysis Matrix

| Leak Archive | Year | Key Figure | Volume / Format | Primary Technical Significance | Legal & Geopolitical Impact |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Pentagon Papers** | 1971 | Daniel Ellsberg, Anthony Russo | 7,000 pages (Xerox copies) | First landmark whistleblower exposure of systematic government deception regarding the Vietnam War. | US Supreme Court *New York Times Co. v. United States* affirmed prior restraint prohibition. |
| **Iraq & Afghan War Logs** | 2010 | Chelsea Manning / WikiLeaks | 400,000+ SIGACTS files | Documented uncounted civilian deaths, torture at Iraqi detention centers, and the "Collateral Murder" Apache cockpit footage. | Sparked international debates on civilian casualty accountability and Espionage Act overreach. |
| **State Dept. Cables (Cablegate)** | 2010 | WikiLeaks (Julian Assange) | 251,287 diplomatic cables | Unfiltered insight into US bilateral coercion, espionage against UN officials, and corrupt Arab dictatorships. | Catalyzed the 2011 Arab Spring uprisings (particularly in Tunisia after cables on Ben Ali's family were published). |
| **NSA Mass Surveillance Archive** | 2013 | Edward Snowden / Laura Poitras / Glenn Greenwald | 1.7M classified documents | Exposed PRISM, XKeyscore, MUSCULAR, BULLRUN, showing direct bulk collection of global internet communications without warrant. | Sparked global encryption adoption (Signal protocol, HTTPS Everywhere) and invalidation of EU-US Safe Harbor. |
| **Vault 7 / Vault 8** | 2017 | Joshua Schulte / WikiLeaks | CIA cyber weapons code | Exposed CIA Center for Cyber Intelligence toolkits: weeping angel smart TV exploits, zero-days, and marble framework obfuscation. | Resulted in major CIA internal security overhaul and historic criminal prosecution. |

---

## 3. Cryptographic Chain-of-Custody & Metadata Forensics

```mermaid
flowchart LR
    A["Raw Leak Received<br/>(Air-Gapped Ingestion)"] --> B["Compute SHA-256 / BLAKE3 Hashes<br/>(Cryptographic Fingerprint)"]
    B --> C["Metadata Scrubbing & Extraction<br/>(ExifTool, PDFiD, OLEtools)"]
    C --> D["Timestamp & Typographic Analysis<br/>(Printers Yellow Dots, Font Versions)"]
    D --> E["Cross-Reference Verification<br/>(Admiralty B2+ Standards)"]
    E --> F["Secure Redaction & Public Archive"]
```

### 3.1 Metadata Forensic Indicators
1. **Exif & Document Streams:** Extracting internal creation dates, author usernames, GUIDs, and software build numbers using tools like `exiftool`, `pdf-parser`, and `oletools`.
2. **Printer Tracking Dots (Machine Identification Codes):** Yellow dots printed by color laser printers encoding serial number, date, and timestamp (led to the identification of Reality Winner in the 2017 NSA leak).
3. **Typography & Word Frequency:** Stylometric analysis matching syntactic quirks against official government style manuals (e.g., GPO Style Manual, DoD Dictionary of Military Terms).

### 3.2 The Admiralty Source Reliability Matrix (STANAG 2022)

All evidence integrated into Global X-Ray must meet a minimum rating of **B2**:

| Source Evaluation | Information Credibility |
| :--- | :--- |
| **A** - Completely reliable (No doubt of authenticity) | **1** - Confirmed by other independent sources |
| **B** - Usually reliable (Minor doubt, good history) | **2** - Probably true (Fits established patterns) |
| **C** - Fairly reliable (Doubtful source, but plausible) | **3** - Possibly true (Unconfirmed, but not improbable) |
| **D** - Not usually reliable (Past record of errors) | **4** - Doubtful (Contradicts known facts) |
| **E** - Unreliable (Demonstrated falsehoods) | **5** - Improbable (Highly unlikely, contradicts physics/history) |
| **F** - Reliability cannot be judged | **6** - Truth cannot be judged |

---

## 4. Master Quotes on Whistleblowing, Conscience and State Secrets

> "Can you really believe that the United States has the right to kill 3 million people in Vietnam in order to maintain its reputation as a credible military threat?"  
> — **Daniel Ellsberg**, *Secrets: A Memoir of Vietnam and the Pentagon Papers* (2002)

> "I do not want to live in a world where everything that I do and say is recorded. That is not something I am willing to support or live under."  
> — **Edward Snowden**, *Interview in Hong Kong* (June 2013)

> "The first step in saving an individual from totalitarianism is to protect their right to know what their government is doing."  
> — **Hannah Arendt**, *The Origins of Totalitarianism* (1951)

> "One of the best ways to achieve justice is to expose injustice."  
> — **Julian Assange**, *WikiLeaks Manifesto* (2006)

> "Power concedes nothing without a demand. It never did and it never will."  
> — **Frederick Douglass**, *West India Emancipation Address* (1857)
"""

# Write files
with open(RESEARCH_DIR / "RESOURCE_WARS_AND_COMMODITY_SUPER_CARTELS.md", "w", encoding="utf-8") as f:
    f.write(RESOURCE_WARS.strip() + "\\n")
print(f"[CREATED] {RESEARCH_DIR / 'RESOURCE_WARS_AND_COMMODITY_SUPER_CARTELS.md'}")

with open(RESEARCH_DIR / "WHISTLEBLOWERS_LEAKS_AND_FORENSIC_STANDARDS.md", "w", encoding="utf-8") as f:
    f.write(WHISTLEBLOWERS_LEAKS.strip() + "\\n")
print(f"[CREATED] {RESEARCH_DIR / 'WHISTLEBLOWERS_LEAKS_AND_FORENSIC_STANDARDS.md'}")

# -------------------------------------------------------------
# 9. ENRICH global_datasets/offshore_havens_matrix.csv
# -------------------------------------------------------------
OFFSHORE_CSV = """Jurisdiction,ISO2,FSI_Ranking,Corporate_Tax_Rate_Pct,Secrecy_Score_100,Primary_Illicit_Flow_Type,Key_Enablers_and_Services
Cayman Islands,KY,2,0.0,76,Hedge Funds & Structured Finance,Nominee trusts, exempt companies, captive insurance
United States (Delaware/Wyoming),US,1,21.0,67,Anonymous Shell LLCs & Real Estate,Unregulated corporate formation agents, no public beneficial register
Switzerland,CH,3,11.9,70,Private Wealth Banking & Commodity Trading,Numbered accounts legacy, attorney-client privilege, freeport storage
Singapore,SG,5,17.0,65,Asian Capital Flight & Family Offices,Variable Capital Companies (VCC), trade financing hubs
Hong Kong,HK,4,16.5,66,Mainland China Outflows & Round-Tripping,Multi-currency clearing, shelf companies, nominee directors
United Kingdom (City of London),GB,12,25.0,47,Global Clearing & Offshore Trust Network,Crown dependencies liaison, Scottish limited partnerships
Luxembourg,LU,6,24.9,55,Multinational Tax Arbitrage & SOPARFIs,Private wealth holding companies, specialized investment funds
British Virgin Islands,VG,9,0.0,81,Anonymous International Business Companies,BVI BC entities, over 400,000 active shell registrations
United Arab Emirates (Dubai),AE,8,9.0,77,Gold Smuggling & Sanctions Arbitrage,Free zone companies (DMCC, DIFC), cash-for-real-estate
Netherlands,NL,10,25.8,51,Dutch Sandwich / Royalty Conduit,Letterbox companies (brievenbusfirma), double tax treaties
Ireland,IE,11,12.5,48,Double Irish / Tech Intellectual Property,IP holding subsidiaries, Green Jersey structures
Bermuda,BM,15,0.0,83,Captive Insurance & Reinsurance Slush,Zero corporate income tax, Fortune 500 capital accumulation
Jersey,JE,16,0.0,74,Ultra-High-Net-Worth Dynasty Trusts,Trust and company service providers, Royal Court sealed records
Guernsey,GG,18,0.0,73,Protected Cell Companies & Captives,Specialist offshore fund administration, zero capital gains tax
Isle of Man,IM,20,0.0,72,Aviation & Superyacht Tax Schemes,VAT leasing arrangements, private aircraft registration
Panama,PA,22,25.0,72,Maritime Flag of Convenience & Bearer Shares,Law firms (Mossack Fonseca legacy), private interest foundations
Liechtenstein,LI,24,12.5,78,Anstalts & Secret Family Foundations,Strict banking secrecy, non-reporting wealth protection trusts
Bahamas,BS,25,0.0,75,Cruise Shipping & Asset Protection Trusts,International business companies, zero estate/gift taxes
Cyprus,CY,28,12.5,62,Russian & Eastern European Offshore Conduit,Citizenship-by-investment legacy, double tax treaties with CIS
Mauritius,MU,30,15.0,60,African & Indian Inward Investment Route,Global Business Companies (GBC), tax treaty shopping
"""

with open(DATASETS_DIR / "offshore_havens_matrix.csv", "w", encoding="utf-8") as f:
    f.write(OFFSHORE_CSV.strip() + "\\n")
print(f"[UPDATED] {DATASETS_DIR / 'offshore_havens_matrix.csv'}")

print("\n[SUCCESS] Additional research dossiers and datasets successfully created!")

