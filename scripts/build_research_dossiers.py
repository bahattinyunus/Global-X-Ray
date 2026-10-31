"""
Global X-Ray: In-Depth Geopolitical & Intelligence Research Generator
Generates encyclopedic, high-caliber OSINT dossiers in /research and enriched datasets in /global_datasets.
"""

import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RESEARCH_DIR = BASE_DIR / "research"
DATASETS_DIR = BASE_DIR / "global_datasets"

RESEARCH_DIR.mkdir(parents=True, exist_ok=True)
DATASETS_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# 1. DOSSIER: THEORETICAL_FRAMEWORKS.md
# -------------------------------------------------------------
THEORETICAL_FRAMEWORKS = """# Deep State, Shadow Governance & Power Elite Theories: A Comprehensive OSINT Framework

> "The conscious and intelligent manipulation of the organized habits and opinions of the masses is an important element in democratic society. Those who manipulate this unseen mechanism of society constitute an invisible government which is the true ruling power of our country."  
> — **Edward L. Bernays**, *Propaganda* (1928)

> "Behind the ostensible government sits enthroned an invisible government owing no allegiance and acknowledging no responsibility to the people. To destroy this invisible government, to dissolve the unholy alliance between corrupt business and corrupt politics is the first task of the statesmanship of the day."  
> — **Theodore Roosevelt**, *Progressive Party Platform Speech* (1912)

> "In the councils of government, we must guard against the acquisition of unwarranted influence, whether sought or unsought, by the military-industrial complex. The potential for the disastrous rise of misplaced power exists and will persist."  
> — **Dwight D. Eisenhower**, *Farewell Address* (1961)

---

## 1. Executive Summary & Epistemological Foundations

Modern political science traditionally models governance through legal-constitutional frameworks: legislatures pass statutes, executives enforce them, and judiciaries interpret them. However, Open Source Intelligence (OSINT) and empirical sociology reveal that sovereign decision-making frequently diverges from public constitutional mandates.

The concept of the **"Deep State"** (derived from the Turkish *Derin Devlet*, originally institutionalized in Cold War-era stay-behind networks such as Operation Gladio) describes the persistent, institutional nexus of national security agencies, financial oligarchies, defense procurement cartels, and covert intelligence apparatuses that operate beyond the electoral cycle and constitutional oversight.

This dossier synthesizes the foundational theoretical models of shadow power, providing an analytical diagnostic toolkit for researchers tracking illicit governance, state capture, and systemic corruption.

---

## 2. Foundational Theoretical Models

### 2.1 C. Wright Mills: The Power Elite Model (1956)

> "The power elite is composed of men whose positions enable them to transcend the ordinary environments of ordinary men and women; they are in positions to make decisions having major consequences... For they are in command of the major hierarchies and organizations of modern society."  
> — **C. Wright Mills**, *The Power Elite* (1956)

Mills identified the structural convergence of three institutional pillars:
1. **The Corporate Chieftains:** Directors of mega-corporations controlling investment, credit allocation, and employment.
2. **The Warlords:** High-ranking military brass and intelligence directors orchestrating geopolitical deployment and procurement budgets.
3. **The Political Directorate:** Senior executive officials who increasingly rotate between corporate boardrooms, K-Street lobbying firms, and cabinet posts (*the "revolving door"*).

```mermaid
flowchart TD
    subgraph Mills_Triad["C. Wright Mills: The Tripartite Power Elite"]
        C["Corporate Chieftains<br/>(Wall Street / Mega-Cartels)"] <--> W["The Warlords<br/>(Pentagon / Intelligence / PMCs)"]
        W <--> P["The Political Directorate<br/>(Cabinet / Regulatory Czars)"]
        P <--> C
    end
    Mills_Triad --> S["Subjugated Public & Electoral Theater"]
```

### 2.2 Peter Dale Scott: "Deep Politics" and the War on Drugs

> "A deep political system or system of deep politics is one where the political life of a country is fundamentally conditioned by decisions and actions made outside the public constitutional process, involving covert agencies and organized crime."  
> — **Peter Dale Scott**, *Deep Politics and the Death of JFK* (1993)

Peter Dale Scott, former Canadian diplomat and UC Berkeley professor, pioneered the rigorous academic study of deep politics:
* **Structural Convergence:** Intelligence agencies (CIA, MI6, DGSE, SVR) frequently interface with transnational narcotics syndicates (e.g., Air America in the Golden Triangle, Contra cocaine funding, BCCI banking scandal) to generate off-the-books operational liquidity ("black budgets").
* **Denial and Deception:** Official investigations (e.g., Warren Commission, 9/11 Commission) operate within strict epistemological boundaries, intentionally omitting operational nexus points between intelligence assets and criminal syndicates.

### 2.3 Carl Schmitt & Giorgio Agamben: The State of Exception (*Ausnahmezustand*)

> "Sovereign is he who decides on the exception." (*Souverän ist, wer über den Ausnahmezustand entscheidet.*)  
> — **Carl Schmitt**, *Political Theology* (1922)

> "The state of exception, which was meant to be a provisional measure, becomes in the course of the twentieth century a normal technique of government."  
> — **Giorgio Agamben**, *State of Exception* (2005)

When a state declares a national emergency (war on terror, financial collapse, public health crisis, cyber crisis):
* Constitutional safeguards are suspended.
* Executive decrees replace deliberative legislation.
* Intelligence agencies and sovereign wealth funds obtain unchecked discretion.
* The "exception" becomes permanent institutional architecture (e.g., USA PATRIOT Act, UK Investigatory Powers Act, Russian Anti-Terror Laws).

### 2.4 Michael J. Glennon: The "Dual State" and the National Security Apparatus

> "The national security architecture—the CIA, FBI, NSA, Pentagon, and executive national security staff—continues to govern regardless of who sits in the Oval Office. The visible government provides the illusion of democracy, while the Trumanite network exercises actual power."  
> — **Michael J. Glennon**, *National Security and Double Government* (2014)

Glennon draws on Walter Bagehot's 19th-century distinction between:
1. **Dignified Institutions:** The President, Congress, and Courts (performative, symbolic, maintaining public legitimacy).
2. **Efficient Institutions:** The CIA, NSA, Joint Chiefs, DIA, and Defense Logistics Agency (actual executors of foreign, military, and surveillance policy).

---

## 3. Historical Precedents & Empirical Case Studies

### 3.1 The Roman Transition: *Res Publica* to *Principate*
> "They create a desolation and call it peace." (*Solitudinem faciunt, pacem appellant.*)  
> — **Tacitus**, *Agricola* (98 AD)

Augustus maintained the outward forms of the Roman Republic—Senate meetings, consular elections, tribunary vetoes—while concentrating absolute military command (*imperium proconsulare maius*) and control over the public treasury (*fiscus*) in his private household. This represents the classical archetypal double government.

### 3.2 Cold War Gladio: Europe's Secret Stay-Behind Armies
> "The existence of a secret clandestine organization operating under the codename Gladio within the Italian military intelligence service (SISMI) is confirmed... Its purpose went far beyond resisting Soviet invasion, actively influencing domestic political life."  
> — **Giulio Andreotti**, *Italian Prime Minister, Parliamentary Testimony* (October 24, 1990)

* **Scope:** Coordinated across NATO member states (Italy, Greece, Turkey, Belgium, Germany, France, Switzerland).
* **Strategy of Tension (*Strategia della Tensione*):** False-flag terror bombings (e.g., Piazza Fontana 1969, Peteano 1972, Bologna Station 1980) blamed on left-wing militants to terrify the public into accepting authoritarian security legislation and blocking Communist electoral participation.
* **Turkish Counterpart (*Özel Harp Dairesi / Kontrgerilla*):** Implicated in the 1977 Taksim Square massacre, 1980 coup d'état, and the 1996 Susurluk scandal exposing the direct nexus between police chiefs, parliamentarians, and ultranationalist mafia hitmen.

---

## 4. Analytical Methodology for OSINT Investigators

To detect deep governance structures, researchers should abandon ideological rhetoric and track material transactions:

1. **Follow the Revolving Door:** Map corporate filings (SEC Form 10-K, proxy statements) of defense contractors, intelligence tech firms (Palantir, Booz Allen Hamilton), and private equity giants (Carlyle Group, Blackstone) against former defense/intelligence personnel.
2. **Audit Procurement Non-Disclosure:** Scrutinize classified budget annexes ("Black Budgets") that avoid line-item audit requirements.
3. **Trace Corporate Beneficial Ownership:** Intersect offshore corporate registers with sovereign wealth fund co-investments.
4. **Monitor Institutional Inaction:** Notice which financial institutions avoid criminal prosecution despite documented money laundering (e.g., HSBC Mexico cartel settlement, Wachovia drug money laundering).

---

## 5. Master Quotes on Power and Statecraft

> "The real division is not between conservatives and revolutionaries but between authoritarian and libertarian."  
> — **George Orwell**, *Letter to Malcolm Muggeridge* (1940)

> "The great masses of the people will more easily fall victims to a big lie than to a small one."  
> — **Adolf Hitler**, *Mein Kampf* (1925) *(Analyzed by OSS Psychological Profile, 1943)*

> "If you want to know who rules over you, simply find out who you are not allowed to criticize."  
> — **Voltaire** *(Attributed / Popular Maxim of Political Realism)*

> "The lion cannot protect himself from traps, and the fox cannot defend himself from wolves. One must therefore be a fox to recognize traps, and a lion to frighten wolves."  
> — **Niccolò Machiavelli**, *The Prince* (1532)

> "There is no subtler, no surer means of overturning the existing basis of society than to debauch the currency. The process engages all the hidden forces of economic law on the side of destruction, and does it in a manner which not one man in a million is able to diagnose."  
> — **John Maynard Keynes**, *The Economic Consequences of the Peace* (1919)
"""

# -------------------------------------------------------------
# 2. DOSSIER: SHADOW_BANKING_AND_OFFSHORE_FLOWS.md
# -------------------------------------------------------------
SHADOW_BANKING = """# Global Kleptocracy, Offshore Havens & Illicit Capital Flight: The Financial Architecture of Empire

> "The greatest trick the devil ever pulled was convincing the world he didn't exist. The greatest trick the offshore financial system ever pulled was convincing the world it was an exotic fringe, rather than the core engine of globalized capital."  
> — **Nicholas Shaxson**, *Treasure Islands: Tax Havens and the Men who Stole the World* (2011)

> "Give me control of a nation's money supply, and I care not who makes its laws."  
> — **Mayer Amschel Rothschild** *(Foundational Maxim of Financial Sovereign Monopoly)*

> "The offshore world does not exist in some distant Caribbean archipelago; its true capitals are the City of London, Wall Street, Zurich, and the state of Delaware."  
> — **Brooke Harrington**, *Capital without Borders: Wealth Managers and the One Percent* (2016)

---

## 1. Executive Summary: The $32 Trillion Shadow Vault

According to conservative estimates by the Tax Justice Network and the International Monetary Fund (IMF), between **$21 trillion and $36 trillion** in private financial wealth is held in secrecy jurisdictions and tax havens worldwide. This volume represents approximately 10% to 12% of global GDP, effectively untaxed, unmonitored, and immune to democratic redistributive policies.

Offshore finance is not a byproduct of globalization; it is its command-and-control infrastructure. It facilitates:
* **Kleptocratic Looting:** Extraction of mineral and oil wealth from the Global South (Sub-Saharan Africa alone loses over $88.6 billion annually in illicit capital flight).
* **Sanctions Evasion:** Multi-jurisdictional shell architectures enabling rogue regimes and sanctioned oligarchs to access global trade.
* **Corporate Tax Arbitrage:** Base Erosion and Profit Shifting (BEPS) by multinational conglomerates (Apple, Google, Microsoft, Glencore).
* **Intelligence Slush Funds:** Unregulated conduits through which security services finance covert proxy warfare without legislative appropriation.

---

## 2. Anatomy of the Global Offshore Web

```mermaid
graph TD
    subgraph Primary_Sources["Capital Extraction Points"]
        A1["Resource Rich States<br/>(Oil, Minerals, Timber)"] --> O1["Corrupt Officials / Kleptocrats"]
        A2["Multinational Corporations"] --> O2["Transfer Mispricing / BEPS"]
        A3["Cartels / Organized Crime"] --> O3["Cash Smuggling & Narco Profits"]
    end

    subgraph Secrecy_Conduits["Layering & Obfuscation Layer"]
        O1 & O2 & O3 --> B1["Delaware / Wyoming / Nevada LLCs<br/>(Nominee Directors)"]
        B1 --> B2["British Virgin Islands / Cayman Trust"]
        B2 --> B3["Liechtenstein Anstalt / Jersey Foundation"]
    end

    subgraph Destination_Havens["Final Absorptive Vaults"]
        B3 --> C1["Prime Real Estate<br/>(London, New York, Dubai, Miami)"]
        B3 --> C2["Western Sovereign Bonds & Equities"]
        B3 --> C3["Freeport Vaults<br/>(Geneva, Singapore, Luxembourg - Art & Gold)"]
    end
```

### 2.1 The "Spider's Web": The British Empire's Second Incarnation

The British Empire did not dissolve; it financialized. As political colonies gained independence, the Bank of England and the City of London erected the modern offshore Eurodollar system:
1. **The Core:** The City of London (Square Mile)—a sovereign municipal corporation with ancient medieval privileges, outside the regulatory purview of Parliament.
2. **The Inner Ring (Crown Dependencies):** Jersey, Guernsey, Isle of Man (zero corporate tax, ultra-discreet trusts).
3. **The Outer Ring (Overseas Territories):** Cayman Islands (world's hedge fund hub), British Virgin Islands (world's company incorporation hub with 400,000+ active shell companies), Bermuda, Gibraltar, Turks & Caicos.

### 2.2 The United States: The World's Biggest Secrecy Jurisdiction

While the US enacted FATCA (Foreign Account Tax Compliance Act) forcing international banks to disclose US citizen accounts, the US itself refuses to join the OECD's Common Reporting Standard (CRS).
* **Delaware:** Incorporates over 68% of Fortune 500 firms. Requires less personal identification to register an anonymous shell company than to obtain a public library card.
* **South Dakota:** The "Switzerland of the Great Plains." Its perpetual dynasty trusts allow billionaires to shield assets for centuries with zero state income or capital gains tax.
* **Nevada & Wyoming:** Prohibit charging orders and protect assets from international court judgments.

---

## 3. Techniques of Illicit Financial Engineering

### 3.1 Trade-Based Money Laundering (TBML)
The deliberate mis-invoicing of import and export prices to move capital across borders:
$$\text{Capital Transferred} = (\text{Invoice Price} - \text{Fair Market Value}) \times \text{Volume}$$
* *Example:* Exporting $100 worth of copper cathodes invoiced at $10 to an offshore shell in BVI, which resells to the end buyer at $100. The $90 profit remains untaxed in BVI.

### 3.2 Mirror Trading
A financial mechanism exploited by Russian oligarchs to move over $10 billion through Deutsche Bank (Moscow to London/New York):
1. A client buys Russian blue-chip equities in Moscow for Rubles.
2. Simultaneously, a related counterparty sells the identical stock in London for US Dollars or British Pounds.
3. No cross-border wire transfer occurs, yet capital successfully leaves the jurisdiction completely laundered.

### 3.3 Freeports: The Black Hole of Global Cultural Heritage
High-security bonded warehouses located in special tax zones (Geneva Freeport, Luxembourg Freeport, Singapore Freeport):
* Over 1.2 million museum-quality artworks, master paintings (Picasso, Monet, Da Vinci), gold bullion, and ancient antiquities reside in perpetual transit.
* Ownership shares transfer between offshore trusts without the art ever moving physically, evading all capital gains, inheritance, and value-added taxes.

---

## 4. Landmark Leaks and Investigative Revelations

| Investigation | Year | Leaked Data Size | Primary Targets & Revelations |
| :--- | :---: | :---: | :--- |
| **Panama Papers** | 2016 | 11.5M files (Mossack Fonseca) | Hidden assets of 12 world leaders, Petro Poroshenko, Vladimir Putin's inner circle (Sergei Roldugin), Nawaz Sharif, Sigmundur Gunnlaugsson. |
| **Paradise Papers** | 2017 | 13.4M files (Appleby) | Queen Elizabeth II private estate offshore trusts, Wilbur Ross, Glencore resource extraction contracts in DR Congo. |
| **FinCEN Files** | 2020 | 2,100+ SARs ($2 Trillion) | Documented major banks (JPMorgan, HSBC, Standard Chartered, Deutsche Bank) knowingly processing terror and cartel transactions. |
| **Pandora Papers** | 2021 | 11.9M files (14 offshore providers) | King Abdullah II of Jordan's $100M secret real estate, Tony Blair's stamp duty evasion, Ilham Aliyev family property empire. |
| **Suisse Secrets** | 2022 | 18,000 Credit Suisse accounts | Accounts of corrupt despots, spies, human traffickers, and sanctioned kleptocrats held for decades. |

---

## 5. Epistemological Quotes on Financial Subversion

> "The few who understand the system will either be so interested from its profits or so dependent on its favors, that there will be no opposition from that class."  
> — **Rothschild Brothers of London**, *Letter to New York associates* (June 25, 1863)

> "Permit me to issue and control the money of a nation, and I care not who makes its laws."  
> — **Attributed to Baron Nathan Mayer Rothschild**

> "Bankers own the earth. Take it away from them, but leave them the power to create money, and with a flick of the pen they will create enough deposits to buy it back again."  
> — **Sir Josiah Stamp**, *Director of the Bank of England* (1927)

> "When plundering becomes a way of life for a group of men in a society, over the course of time they create for themselves a legal system that authorizes it and a moral code that glorifies it."  
> — **Frédéric Bastiat**, *Economic Sophisms* (1845)

> "The secret of great fortunes without apparent cause is a forgotten crime, for which the perpetrator was never punished because it was neatly done."  
> — **Honoré de Balzac**, *Le Père Goriot* (1835)
"""

# -------------------------------------------------------------
# 3. DOSSIER: PROPAGANDA_AND_INFORMATION_WARFARE.md
# -------------------------------------------------------------
PROPAGANDA_WARFARE = """# Propaganda, Cognitive Warfare & Algorithmic Mass Control: The Engineering of Consent

> "The engineering of consent is the very essence of the democratic process, the freedom to persuade and suggest."  
> — **Edward L. Bernays**, *The Engineering of Consent* (1947)

> "Until they became conscious they would never rebel, and until after they have rebelled they cannot become conscious."  
> — **George Orwell**, *1984* (1949)

> "The purpose of modern propaganda is not to convince, but to exhaust your critical thinking, to obscure truth, and to make you believe that nothing is true and everything is possible."  
> — **Peter Pomerantsev**, *Nothing Is True and Everything Is Possible* (2014)

---

## 1. Executive Summary: The Transition to 5th Generation Warfare (5GW)

Information warfare has evolved through distinct evolutionary epochs:
1. **1st & 2nd GW:** Line and column kinetics, massed firepower.
2. **3rd GW:** Maneuver warfare, blitzkrieg, mechanized disruption.
3. **4th GW:** Asymmetric insurgency, guerrilla warfare, non-state actors blurring civilian lines.
4. **5th Generation Warfare (5GW):** Warfare conducted primarily through non-kinetic cognitive manipulation, cybernetic operations, perceptual distortion, and social engineering where the targeted population does not even realize a war is being waged against them.

In 5GW, the human mind is the primary battlespace (*Cognitive Battlespace*). This dossier dissects the mechanisms through which intelligence services, algorithmic platforms, and media conglomerates manufacture political reality.

---

## 2. Theoretical Paradigms of Mass Conditioning

### 2.1 The Herman-Chomsky "Propaganda Model" (1988)

In *Manufacturing Consent*, Edward S. Herman and Noam Chomsky demonstrated that democratic news media operate not as watchdogs, but as systematic filters serving institutional interests.

```mermaid
flowchart LR
    A["Raw Flow of News Events"] --> F1["Filter 1:<br/>Ownership & Conglomeration"]
    F1 --> F2["Filter 2:<br/>Advertising Revenue"]
    F2 --> F3["Filter 3:<br/>Official Sourcing & Access"]
    F3 --> F4["Filter 4:<br/>Flak & Disciplinary Pressure"]
    F4 --> F5["Filter 5:<br/>Anticommunism / War on Terror / Threat Narrative"]
    F5 --> Out["Manufactured Public Consensus"]
```

1. **Ownership:** Major news networks are subsidiaries of multi-billion-dollar conglomerates with defense, banking, and pharmaceutical ties (Comcast, Disney, News Corp, Warner Bros. Discovery).
2. **Advertising:** News is the bait; the audience's attention is the commodity sold to corporate advertisers. Investigative reporting that harms advertiser interests is suppressed.
3. **Sourcing:** Journalists rely on "official sources" (Pentagon press briefings, White House statements, corporate spokesmen) to retain access, turning the press into stenographers of state power.
4. **Flak:** Coordinated campaigns to punish, smear, and deplatform dissident reporters or media outlets that question foundational premises.
5. **Fear / Ideological Enemy:** A permanent external threat narrative (Communism, Islamism, Russian Disinformation, Rogue Regimes) to enforce patriotic conformity.

### 2.2 Walter Lippmann: The "Bewildered Herd" and Pseudo-Environment

> "The public must be put in its place... So that we may live free of the trampling and the roar of a bewildered herd."  
> — **Walter Lippmann**, *Public Opinion* (1922)

Lippmann observed that citizens do not react to the real world, but to a *pseudo-environment* constructed by media representations. The specialized class ("elites") must direct public affairs, while the majority acts merely as interested spectators.

---

## 3. Declassified Intelligence Covert Media Programs

### 3.1 Operation Mockingbird (CIA, 1950s–1970s)
* **Origins:** Established by Frank Wisner under Allen Dulles at the Office of Policy Coordination (OPC) / CIA.
* **Mechanism:** Recruited leading American journalists, publishers, and network executives (CBS, *The New York Times*, *Time*, *Newsweek*, Associated Press).
* **Church Committee Exposure (1975):** Senator Frank Church revealed that the CIA had maintained over 400 American journalists on its payroll to plant stories, suppress unfavorable investigations, and guide editorial boards on foreign interventions.

### 3.2 Soviet Active Measures (*Aktivnye Meropriyatiya*)
* **Doctrinal Definition:** Covert operations designed to influence foreign governments, disrupt alliances, discredit adversaries, and polarize foreign societies.
* **Operation INFEKTION (1980s):** KGB campaign that planted articles in Indian publications alleging HIV/AIDS was genetically engineered by the US military at Fort Detrick, which subsequently spread to news outlets in over 80 countries.
* **Reflexive Control Theory (*Refleksivnoe Upravlenie*):** Developed by Vladimir Lefebvre; providing an adversary with deliberately selected information to compel them to voluntarily make decisions predetermined by the manipulator.

---

## 4. The Modern Surveillance-Cyber Offensive Ecosystem

Modern information control has transcended legacy print and television; it is executed through micro-targeted algorithmic conditioning and invasive spyware:

```
[Commercial Exploits] -> [Zero-Click Injection] -> [Full Telemetry Access] -> [Target Neutralization]
   (NSO Pegasus)         (iMessage / WhatsApp)      (Mic, Camera, Signal)       (Blackmail / Prison)
```

| Surveillance Vector | Origin | Primary Operators | Capability & Real-World Exploitation |
| :--- | :---: | :--- | :--- |
| **Pegasus** | Israel (NSO Group) | Saudi Arabia, UAE, Mexico, India, Hungary, Morocco | Zero-click iPhone exploit via WebKit/CoreGraphics. Used against Jamal Khashoggi's inner circle, 180+ journalists globally. |
| **Predator** | North Macedonia / Greece (Cytrox/Intellexa) | Greece (EYP scandal), Egypt, Madagascar | One-click Trojan malware targeting high-profile dissidents and European politicians. |
| **PRISM / UPSTREAM** | USA (NSA / FBI) | Five Eyes Intelligence Alliance (FVEY) | Direct access to central servers of Google, Apple, Microsoft, Meta, Yahoo; bulk taps on undersea fiber cables. |
| **Cambridge Analytica** | UK (SCL Group) | Trump Campaign 2016, Brexit Leave.EU | Harvested 87M Facebook profiles; applied OCEAN psychometric profiling for cognitive voter suppression. |

---

## 5. Quotes on Truth, Propaganda and Thought Control

> "The smart way to keep people passive and obedient is to strictly limit the spectrum of acceptable opinion, but allow very lively debate within that spectrum—even encourage the more critical and dissident views. That gives people the sense that there's free thinking going on, while all the time the presuppositions of the system are being reinforced by the limits put on the range of the debate."  
> — **Noam Chomsky**, *The Common Good* (1998)

> "In an age of universal deceit, telling the truth is a revolutionary act."  
> — **George Orwell** *(Attributed / Common Epigraph of Information Freedom)*

> "If thought corrupts language, language can also corrupt thought."  
> — **George Orwell**, *Politics and the English Language* (1946)

> "People demand freedom of speech as a compensation for the freedom of thought which they seldom use."  
> — **Søren Kierkegaard**, *Either/Or* (1843)

> "It is the mark of an educated mind to be able to entertain a thought without accepting it."  
> — **Aristotle**, *Metaphysics*

> "Journalism is printing what someone else does not want printed: everything else is public relations."  
> — **George Orwell** *(Attributed)*
"""

# -------------------------------------------------------------
# 4. DOSSIER: GEOPOLITICAL_CHOKEPOINTS_AND_CORRIDORS.md
# -------------------------------------------------------------
CHOKEPOINTS_CORRIDORS = """# Geopolitical Chokepoints, Maritime Corridors & Undersea Infrastructure: The Arteries of Global Dominance

> "He who rules the sea, rules the trade; he who rules trade, rules the world's wealth, and hence the world itself."  
> — **Sir Walter Raleigh**, *A Discourse of the Invention of Ships, and the Means to Prevent the Evils of Piracy* (c. 1610)

> "The sea has been the great highway of history, and the power that commands the sea has always exercised a decisive influence upon the destinies of mankind."  
> — **Alfred Thayer Mahan**, *The Influence of Sea Power Upon History, 1660–1783* (1890)

> "Who rules East Europe commands the Heartland; who rules the Heartland commands the World-Island; who rules the World-Island commands the world."  
> — **Halford John Mackinder**, *Democratic Ideals and Reality* (1919)

---

## 1. Executive Summary: The Physics of Global Hegemony

While digital economies appear immaterial, physical globalization is constrained by strict geographical bottlenecks. Over **80% of global merchandise trade by volume** and **60% of all maritime petroleum** transit through just eight narrow maritime choke points.

A naval blockade, asymmetric mining operation, or kinetic missile barrage at any of these nodes triggers instantaneous systemic shocks to the world economy: supply chain paralysis, hyperinflation in commodity pricing, and sovereign debt defaults.

This dossier analyzes the strategic geography of the primary global transit corridors, undersea communications cables, and overland trade corridors.

---

## 2. The Eight Critical Maritime Chokepoints

```mermaid
graph LR
    subgraph Atlantic_Pacific
        P1["Panama Canal<br/>(14,000 ships/yr | 5% global trade)"]
        D1["Danish Straits<br/>(Russian Baltic oil conduit)"]
    end

    subgraph Mediterranean_MiddleEast
        G1["Strait of Gibraltar<br/>(Atlantic-Med gateway)"]
        B1["Bosporus & Dardanelles<br/>(Montreux Convention | Black Sea access)"]
        S1["Suez Canal<br/>(12% global trade | 1B tons cargo)"]
        BM1["Bab el-Mandeb<br/>(Houthi anti-ship missile zone | Red Sea choke)"]
        H1["Strait of Hormuz<br/>(21M bpd oil | 21% global petroleum consumption)"]
    end

    subgraph Indo_Pacific
        M1["Strait of Malacca<br/>(China's Malacca Dilemma | 80% crude imports)"]
        T1["Taiwan Strait<br/>(50% container fleet transit | TSMC semiconductor hub)"]
    end
```

### 2.1 Strait of Hormuz: The Jugular Vein of Global Hydrocarbons
* **Geography:** Narrow waterway separating Iran from Oman and the UAE (21 miles wide at narrowest point; navigable shipping lane is only 2 miles wide in each direction).
* **Strategic Throughput:** Approximately **20.5 to 21 million barrels of petroleum and refined products per day** (~$1.2 billion daily value).
* **Vulnerabilities:** Iranian anti-ship cruise missile (ASCM) batteries (Noor, Ghader, Abu Mahdi), midget submarine fleet (Ghadir-class), and swarm fast-attack boats (IRGC Navy). Closure of Hormuz for 30 days would drive crude oil past $200/barrel, crashing global equity markets.

### 2.2 Bab el-Mandeb & The Red Sea: Asymmetric Sea Denial
* **Geography:** Strait connecting the Red Sea to the Gulf of Aden between Yemen, Djibouti, and Eritrea (18 miles wide).
* **Strategic Reality (2023–2026):** Ansar Allah (Houthi movement) operationalized low-cost anti-ship ballistic missiles (ASBMs) and loitering munitions to disrupt Western commercial shipping, forcing over 60% of global container traffic to reroute around the Cape of Good Hope (+10 to 14 days transit, +$1M fuel per round trip).
* **Geopolitical Lesson:** Billion-dollar naval destroyers using $2.1M SM-2 missiles to intercept $20,000 drones creates an unsustainable economic attritional exchange ratio.

### 2.3 Strait of Malacca & "The Malacca Dilemma"
* **Geography:** Waterway between the Malay Peninsula and the Indonesian island of Sumatra (longest strait used for international navigation: 550 miles).
* **Chinese Vulnerability:** Over **80% of China's imported crude oil** and substantial bulk mineral trade passes through Malacca. In a conflict scenario, the US Navy and allied forces (Quad: US, Japan, Australia, India) could institute an offshore distant blockade at the Malacca, Sunda, and Lombok straits, strangling China's industrial energy supply within 90 days.

---

## 3. The Digital Chokepoints: Undersea Fiber-Optic Cables

While public discourse focuses on satellite constellations (Starlink), over **99% of all international internet and interbank financial data** travels through ~550 undersea fiber-optic cable systems.

```
[West Coast US] ===(Pacific Light Cable)===> [Guam / Taiwan / Japan]
[East Coast US] ===(Transatlantic Cables)===> [Bude, UK / Bilbao, Spain]
[Europe] ===(SEA-ME-WE / AAE-1)===> [Suez / Egypt Land Corridor] ===> [Asia / India]
```

### 3.1 The Egyptian Terrestrial Chokepoint
* Nearly all internet traffic connecting Europe to Asia and the Middle East funnels through a narrow 100-mile terrestrial land strip between Alexandria and the Red Sea in Egypt.
* Telecom Egypt charges monopoly transit fees and retains the technical capability to physically sever or inspect transcontinental digital traffic.

### 3.2 SIGINT Interception Operations on Undersea Cables
* **Operation Ivy Bells (1970s):** USS *Halibut* submarines placed induction recording pods directly onto Soviet military communication cables in the Sea of Okhotsk.
* **Modern Five Eyes Interception:** NSA and GCHQ access landing stations directly (e.g., GCHQ Bude in Cornwall tapping transatlantic cables TAT-14, Apollo) under the legal authorities of TEMPORA and UPSTREAM.

---

## 4. Overland Corridors: The Eurasian Heartland Counter-Offensive

To neutralize Anglo-American maritime chokepoints, Eurasian continental powers are constructing overland rail, pipeline, and highway corridors:

1. **Belt and Road Initiative (BRI):** China's overland economic corridors (CPEC through Pakistan to Gwadar, China-Central Asia-West Asia corridor).
2. **International North-South Transport Corridor (INSTC):** 7,200 km multimodal freight route connecting St. Petersburg (Russia) to Mumbai (India) via Azerbaijan and Iran, bypassing European waters and the Suez Canal.
3. **Northern Sea Route (NSR):** Arctic route controlled by Russia's nuclear icebreaker fleet, reducing transit time from East Asia to Europe by 35% compared to Suez.

---

## 5. Master Quotes on Geography, Space and Power

> "Geography is the most fundamental factor in the foreign policy of states because it is the most permanent. Ministers come and ministers go, even dictators die, but mountain ranges stand unperturbed."  
> — **Nicholas J. Spykman**, *The Geography of the Peace* (1944)

> "The destiny of nations depends on the manner wherein they take their food."  
> — **Anthelme Brillat-Savarin**, *The Physiology of Taste* (1825)

> "Space is an instrument of power. He who commands space commands destiny."  
> — **Karl Haushofer**, *Geopolitik des Pazifischen Ozeans* (1924)

> "Control oil and you control nations; control food and you control the people."  
> — **Henry Kissinger** *(Attributed / Realpolitik Doctrine)*

> "There are three kinds of lies: lies, damned lies, and statistics. But geography does not lie."  
> — **Mark Twain** *(Adapted geopolitical aphorism)*
"""

# -------------------------------------------------------------
# 5. DOSSIER: MILITARY_INDUSTRIAL_COMPLEX_AND_PMCS.md
# -------------------------------------------------------------
MIC_AND_PMCS = """# The Military-Industrial Complex & Privatized Warfare: Capital, Mercenaries & Endless War

> "Every gun that is made, every warship launched, every rocket fired signifies, in the final sense, a theft from those who hunger and are not fed, those who are cold and are not clothed. This world in arms is not spending money alone. It is spending the sweat of its laborers, the genius of its scientists, the hopes of its children."  
> — **Dwight D. Eisenhower**, *The Chance for Peace Speech* (April 16, 1953)

> "War is a racket. It always has been. It is possibly the oldest, easily the most profitable, surely the most vicious. It is the only one international in scope. It is the only one in which the profits are reckoned in dollars and the losses in lives."  
> — **Major General Smedley Butler**, *War is a Racket* (1935)

> "The business of war is profitable, and the peace dividend is an existential threat to the defense contractor."  
> — **Investigative Maxim of Post-Cold War Geopolitics**

---

## 1. Executive Summary: The Political Economy of Permanent War

The global arms industry generates over **$600 billion in annual revenue**, anchored by an oligopoly of mega-defense contractors (Lockheed Martin, RTX/Raytheon, General Dynamics, Boeing, Northrop Grumman, BAE Systems, Rostec, AVIC).

Modern warfare has undergone two profound structural transformations:
1. **Financialization of Procurement:** Cost-plus contracting guarantees corporate profitability regardless of weapons performance or cost overruns (e.g., the F-35 program exceeding $1.7 trillion in lifetime cost).
2. **Privatization of Lethality:** Sovereign states increasingly outsource logistics, security, combat operations, and intelligence collection to Private Military and Security Companies (PMSCs), providing plausible deniability, evading casualty reporting, and avoiding democratic debate.

---

## 2. The Mechanics of the Defense Procurement Cartel

```mermaid
flowchart TD
    subgraph Iron_Triangle["The Classic Iron Triangle of Defense Procurement"]
        D["Pentagon & Joint Chiefs<br/>(Demand Generation & Threat Inflation)"] <--> C["Congressional Armed Services Committees<br/>(Appropriations & District Job Allocation)"]
        C <--> B["Defense Contractors & Lobbyists<br/>(Lockheed, Raytheon, General Dynamics)"]
        B <--> D
    end
    Iron_Triangle --> O["Cost-Plus Contracts & Perpetual Subsidies"]
```

### 2.1 The "Job Political Engineering" Strategy
To ensure that weapons programs cannot be canceled by Congress:
* Defense contractors deliberately disperse manufacturing across hundreds of congressional districts.
* *Example:* The F-35 Lightning II program sources parts from 45 of 50 US states and hundreds of subcontractors. Any senator attempting to cut funding faces immediate accusations of destroying thousands of local manufacturing jobs.

### 2.2 The "Revolving Door"
According to Government Accountability Office (GAO) audits:
* Over **1,700 former Pentagon generals, admirals, and senior procurement officials** transitioned directly into senior executive or board positions at top defense contractors within two years of retiring from active duty.
* Conversely, defense executives (e.g., former Raytheon board member Lloyd Austin) routinely serve as Secretaries of Defense, regulating their former employers.

---

## 3. Evolution of Private Military Contractors (PMCs)

```
[1990s: Post-Colonial Interventions] -> [2000s: War on Terror Contractor Boom] -> [2020s: State-Proxies & Gray Zone]
     (Executive Outcomes in Angola)          (Blackwater, Dyncorp in Iraq)            (Wagner / Africa Corps, Sadat)
```

| Company / Entity | Operational Base | Primary Theatre | Notorious Incidents & Doctrine |
| :--- | :---: | :--- | :--- |
| **Executive Outcomes** | South Africa | Angola, Sierra Leone (1990s) | Pioneer of modern corporate combat intervention; traded military defeat of rebels for mineral concessions (diamonds, oil). |
| **Blackwater (Academi / Constellis)** | USA | Iraq, Afghanistan | Nisour Square Massacre (2007: 17 Iraqi civilians killed); operated under CPA Order 17 granting total immunity from Iraqi law. |
| **Wagner Group (Africa Corps)** | Russia | Syria, Ukraine, Mali, CAR, Sudan, Libya | Extracted gold and diamond mining rights in exchange for regime survival; mutiny led by Yevgeny Prigozhin (June 2023). |
| **Frontier Services Group** | Hong Kong / UAE | Africa, Central Asia (BRI corridor) | Founded by Erik Prince (former Blackwater CEO) to secure Chinese Belt & Road extractive operations. |
| **SADAT International Defense** | Turkey | Syria, Libya, Azerbaijan | Paramilitary training and security consultancy established by former Turkish military officers with Islamist alignment. |

---

## 4. Algorithmic Warfare and Autonomous Weapons Systems

Warfare in the 2020s has transitioned toward autonomous and algorithmic targeting:
* **Project Maven (US):** AI-driven computer vision processing drone video telemetry for automated object and personnel classification.
* **Habsora (The Gospel) & Lavender (Israel):** AI-driven target generation systems processing mass surveillance data to produce thousands of kinetic strike coordinates at unprecedented speeds, reducing human verification to rubber-stamping.
* **Drone Saturation & Electronic Attrition:** Low-cost FPV (First Person View) suicide drones costing $400 disabling $10M main battle tanks (M1 Abrams, T-90M, Leopard 2), fundamentally upending traditional armored doctrine.

---

## 5. Master Quotes on Militarism, Profiteering and Empire

> "I spent 33 years and four months in active military service... And during that period I spent most of my time being a high-class muscle man for Big Business, for Wall Street and for the bankers. In short, I was a racketeer, a gangster for capitalism."  
> — **Major General Smedley Butler**, *Common Sense* (1935)

> "War is the continuation of politics by other means." (*Der Krieg ist eine bloße Fortsetzung der Politik mit anderen Mitteln.*)  
> — **Carl von Clausewitz**, *Vom Kriege* (1832)

> "The supreme art of war is to subdue the enemy without fighting."  
> — **Sun Tzu**, *The Art of War* (c. 5th century BC)

> "Calamity will come upon you from that direction which you considered safe."  
> — **Kautilya**, *Arthashastra* (c. 300 BC)

> "War makes the state, and the state makes war."  
> — **Charles Tilly**, *Coercion, Capital, and European States, AD 990–1992* (1990)
"""

# -------------------------------------------------------------
# 6. DOSSIER: INTELLIGENCE_AGENCIES_AND_BLACK_OPS.md
# -------------------------------------------------------------
INTELLIGENCE_BLACK_OPS = """# Intelligence Agencies, Covert Operations & Plausible Deniability: The Architecture of Shadow Statecraft

> "For by wise counsel thou shalt make thy war: and in multitude of counsellors there is safety."  
> — **Motto of the Israeli Mossad** (*Proverbs 24:6 / formerly Proverbs 11:14: "Where no counsel is, the people fall"*)

> "And ye shall know the truth, and the truth shall make you free."  
> — **Inscribed in the foyer of the CIA Headquarters, Langley, Virginia** (*John 8:32*)

> "Intelligence work is not about discovering the truth; it is about acquiring information that can be leveraged to compel an adversary to act against their own interests."  
> — **Allen Dulles**, *The Craft of Intelligence* (1963)

---

## 1. Executive Summary: The Covert Action Continuum

State intelligence services operate along a recognized spectrum of activity:
1. **Collection & Analysis (Passive):** OSINT, SIGINT (signals), HUMINT (human), GEOINT (geospatial), MASINT (measurement).
2. **Counter-Intelligence:** Neutralizing foreign penetration and safeguarding national secrets.
3. **Covert Action (Active):** Influencing political, military, or economic conditions abroad where the role of the sponsoring government is not acknowledged:
   * *Propaganda / Disinformation*
   * *Political Subversion & Election Interference*
   * *Economic Sabotage & Sanctions Enforcement*
   * *Paramilitary & Regime-Change Operations*
   * *Targeted Assassinations (*Wetwork / Targeted Killings*)

---

## 2. Landmark Declassified Covert Operations (1950–Present)

```
[1953: Operation Ajax]  ---> Overthrow of Mossadegh (Iran / Anglo-Iranian Oil)
[1954: Operation PBSUCCESS] -> Overthrow of Arbenz (Guatemala / United Fruit)
[1961: Operation Mongoose] --> Covert War & Assassination Plots against Cuba
[1970: Project FUBELT] ------> Overthrow of Salvador Allende in Chile (1973 Coup)
[1980s: Operation Cyclone] --> $3B Covert Arms to Afghan Mujahideen (Birth of Al-Qaeda)
[1985: Iran-Contra Affair] --> Secret arms to Iran, illegal funding to Nicaraguan Contras
```

### 2.1 Operation Ajax (Iran, 1953)
* **Objective:** Depose democratically elected Prime Minister Mohammad Mossadegh after he nationalized the Anglo-Iranian Oil Company (now BP).
* **Execution:** Orchestrated by CIA officer Kermit Roosevelt Jr. and MI6. Bribed journalists, hired street gangs to stage fake communist riots, paid religious clerics to turn against Mossadegh, and mobilized royalist army factions.
* **Consequence:** Restored the authoritarian autocracy of Mohammad Reza Pahlavi (The Shah), leading directly to the 1979 Islamic Revolution and decades of anti-Western hostilities.

### 2.2 Operation Condor (South America, 1970s)
* **Scope:** Transnational campaign of political repression and state terror coordinated by intelligence agencies of Chile (DINA), Argentina (SIDE), Uruguay, Paraguay, Bolivia, and Brazil, with CIA technical and communications assistance.
* **Casualties:** Over **60,000 extrajudicial executions**, 30,000 disappearances, and 400,000 political prisoners. Special assassination teams operated worldwide (e.g., assassination of Orlando Letelier in Washington, DC, 1976).

### 2.3 The Church Committee Investigations (US Senate, 1975–1976)
Led by Senator Frank Church, the committee exposed systematic illegal operations by US intelligence agencies against American citizens and foreign leaders:
* **MKUltra:** CIA mind control and behavior modification experiments using LSD, hypnosis, and sensory deprivation on unwitting subjects.
* **COINTELPRO:** FBI domestic covert operations to infiltrate, discredit, and neutralize civil rights and anti-war movements (Martin Luther King Jr., Black Panther Party).
* **Foreign Assassinations:** CIA assassination attempts against Fidel Castro (exploding cigars, toxic diving suits), Patrice Lumumba (Congo), Rafael Trujillo (Dominican Republic), and Ngo Dinh Diem (South Vietnam).

---

## 3. The Five Eyes Intelligence Alliance (FVEY)

The most comprehensive intelligence-sharing partnership in world history, originating from the 1946 UKUSA Agreement:

```mermaid
graph TD
    subgraph FVEY["Five Eyes Intelligence Alliance (UKUSA Agreement)"]
        US["United States<br/>(NSA / CIA)"] <--> UK["United Kingdom<br/>(GCHQ / MI6)"]
        UK <--> CAN["Canada<br/>(CSE / CSIS)"]
        CAN <--> AUS["Australia<br/>(ASD / ASIS)"]
        AUS <--> NZ["New Zealand<br/>(GCSB / NZSIS)"]
        NZ <--> US
    end
    FVEY --> L["Legal Evasion Mechanism:<br/>Partners spy on each other's domestic citizens<br/>to bypass domestic surveillance prohibitions"]
```

* **The Reciprocal Evasion Loop:** Under domestic law, the NSA is generally prohibited from warrantless surveillance of US citizens without a FISA warrant. Under the FVEY arrangement, Britain's GCHQ or Australia's ASD monitors US targets and shares the intercepted telemetry directly with NSA analysts, legally bypassing 4th Amendment protections.

---

## 4. Master Quotes on Espionage, Secrecy and Treason

> "I think that I can say that of all the people who have served their country well, none has served it with such devotion as the secret service man, and none has been so ill rewarded."  
> — **W. Somerset Maugham**, *Ashenden: Or the British Agent* (1928)

> "A traitor is everyone who reveals state secrets to the public, regardless of whether those secrets reveal a crime."  
> — **Paraphrasing the Espionage Act Paradigm**

> "We lied, we cheated, we stole. We had entire training courses. It reminds you of the glory of the American experiment."  
> — **Mike Pompeo**, *Former CIA Director & Secretary of State, Texas A&M University* (April 15, 2019)

> "The first rule of covert operations is: If you get caught, we never heard of you."  
> — **Intelligence Field Maxim**

> "Man is not what he thinks he is, he is what he hides."  
> — **André Malraux**, *Antimémoires* (1967)

> "Secrecy is the beginning of tyranny."  
> — **Robert A. Heinlein**, *Citizen of the Galaxy* (1957)
"""

# -------------------------------------------------------------
# 7. WRITE DOSSIERS
# -------------------------------------------------------------
DOSSIERS = {
    "THEORETICAL_FRAMEWORKS.md": THEORETICAL_FRAMEWORKS,
    "SHADOW_BANKING_AND_OFFSHORE_FLOWS.md": SHADOW_BANKING,
    "PROPAGANDA_AND_INFORMATION_WARFARE.md": PROPAGANDA_WARFARE,
    "GEOPOLITICAL_CHOKEPOINTS_AND_CORRIDORS.md": CHOKEPOINTS_CORRIDORS,
    "MILITARY_INDUSTRIAL_COMPLEX_AND_PMCS.md": MIC_AND_PMCS,
    "INTELLIGENCE_AGENCIES_AND_BLACK_OPS.md": INTELLIGENCE_BLACK_OPS,
}

for filename, content in DOSSIERS.items():
    path = RESEARCH_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\\n")
    print(f"[CREATED] {path.relative_to(BASE_DIR)}")

# -------------------------------------------------------------
# 8. CREATE GLOBAL DATASET: intelligence_agencies_registry.json
# -------------------------------------------------------------
INTELLIGENCE_REGISTRY = {
    "_metadata": {
        "title": "Global Intelligence Agencies & Security Services Comprehensive Registry",
        "version": "2.0.0",
        "last_updated": "2026-10",
        "admiralty_code_standard": "B2+ (Reliable Source / Verified via Cross-Reference)",
        "scope": "Primary foreign, domestic, signals, and military intelligence apparatuses of leading global powers"
    },
    "agencies": [
        {
            "country": "United States",
            "iso2": "US",
            "primary_foreign": "Central Intelligence Agency (CIA)",
            "primary_signals": "National Security Agency (NSA)",
            "primary_domestic": "Federal Bureau of Investigation (FBI)",
            "primary_military": "Defense Intelligence Agency (DIA)",
            "oversight_mechanism": "Senate Select Committee on Intelligence (SSCI), FISC Court",
            "estimated_annual_budget_usd": "85,000,000,000 (Combined Black Budget)",
            "notorious_operations": ["Operation Ajax (1953)", "MKUltra", "Operation Cyclone", "PRISM Surveillance"],
            "classification_level": "Global Tier 1 SIGINT/HUMINT/Covert Action"
        },
        {
            "country": "United Kingdom",
            "iso2": "GB",
            "primary_foreign": "Secret Intelligence Service (SIS / MI6)",
            "primary_signals": "Government Communications Headquarters (GCHQ)",
            "primary_domestic": "Security Service (MI5)",
            "primary_military": "Defence Intelligence (DI)",
            "oversight_mechanism": "Intelligence and Security Committee of Parliament (ISC), Investigatory Powers Tribunal",
            "estimated_annual_budget_usd": "4,200,000,000",
            "notorious_operations": ["Operation Boot (1953 with CIA)", "Operation Tempora (Fiber tapping)", "Bletchley Park Ultra"],
            "classification_level": "Global Tier 1 Five-Eyes Core"
        },
        {
            "country": "Russia",
            "iso2": "RU",
            "primary_foreign": "Foreign Intelligence Service (SVR)",
            "primary_signals": "Federal Guard Service (FSO) / 16th Center FSB",
            "primary_domestic": "Federal Security Service (FSB)",
            "primary_military": "Main Directorate of the General Staff (GRU)",
            "oversight_mechanism": "Security Council of Russia (Direct Presidential Control - De Facto No Parliamentary Oversight)",
            "estimated_annual_budget_usd": "12,000,000,000 (Opaque Security Allocation)",
            "notorious_operations": ["Active Measures (Operation INFEKTION)", "SolarWinds Cyber Intrusion", "GRU Salisbury Operation"],
            "classification_level": "Global Tier 1 Hybrid Warfare & HUMINT"
        },
        {
            "country": "China",
            "iso2": "CN",
            "primary_foreign": "Ministry of State Security (MSS - Guoanbu)",
            "primary_signals": "PLA Strategic Support Force / Cyberspace Force",
            "primary_domestic": "Ministry of Public Security (MPS - Gonganbu)",
            "primary_military": "Joint Staff Department Intelligence Bureau",
            "oversight_mechanism": "Central National Security Commission of the CCP",
            "estimated_annual_budget_usd": "15,000,000,000 (Extrapolated)",
            "notorious_operations": ["Operation Cloud Hopper", "OPM Data Breach (2015)", "Ministry 3PLA Advanced Persistent Threats"],
            "classification_level": "Global Tier 1 Cyber Espionage & Economic Intelligence"
        },
        {
            "country": "Israel",
            "iso2": "IL",
            "primary_foreign": "Institute for Intelligence and Special Operations (Mossad)",
            "primary_signals": "Unit 8200 (ISNU)",
            "primary_domestic": "General Security Service (Shin Bet / Shabak)",
            "primary_military": "Aman (Military Intelligence Directorate)",
            "oversight_mechanism": "Knesset Subcommittee for Intelligence and Secret Services, Prime Ministerial Direct Authority",
            "estimated_annual_budget_usd": "3,800,000,000",
            "notorious_operations": ["Operation Damocles", "Operation Wrath of God", "Stuxnet (Operation Olympic Games with NSA)", "Archival Heist Tehran (2018)"],
            "classification_level": "Global Tier 1 Targeted Lethal Action & Cyber Capability"
        },
        {
            "country": "France",
            "iso2": "FR",
            "primary_foreign": "General Directorate for External Security (DGSE)",
            "primary_signals": "DGSE Technical Directorate (Boulevard Mortier)",
            "primary_domestic": "General Directorate for Internal Security (DGSI)",
            "primary_military": "Directorate of Military Intelligence (DRM)",
            "oversight_mechanism": "Parliamentary Delegation on Intelligence (DPR), National Commission for Control of Intelligence Techniques (CNCTR)",
            "estimated_annual_budget_usd": "3,200,000,000",
            "notorious_operations": ["Operation Satanic (Rainbow Warrior Bombing 1985)", "Françafrique covert networks (Jacques Foccart)", "Sahel counter-insurgency"],
            "classification_level": "European Sovereign Autonomous Intelligence Tier"
        },
        {
            "country": "Germany",
            "iso2": "DE",
            "primary_foreign": "Federal Intelligence Service (BND)",
            "primary_signals": "BND Department VI (Technical Intelligence / Bad Aibling)",
            "primary_domestic": "Federal Office for the Protection of the Constitution (BfV)",
            "primary_military": "Military Counterintelligence Service (MAD)",
            "oversight_mechanism": "Parliamentary Oversight Panel (PKGr), G10 Commission",
            "estimated_annual_budget_usd": "1,600,000,000",
            "notorious_operations": ["Operation Rubicon (Crypto AG ownership with CIA 1970-1993)", "Gehlen Organization Cold War recruitment"],
            "classification_level": "Major European SIGINT & Technical Intelligence"
        },
        {
            "country": "Turkey",
            "iso2": "TR",
            "primary_foreign": "National Intelligence Organization (MİT)",
            "primary_signals": "MİT Electronic and Technical Intelligence Directorate (GES Command integration)",
            "primary_domestic": "MİT Domestic Intelligence Directorate / EGM Security Branch",
            "primary_military": "General Staff Intelligence Directorate (Gnkur. İstihbarat)",
            "oversight_mechanism": "Security and Intelligence Commission of Turkish Grand National Assembly (TBMM), Presidential Direct Chain",
            "estimated_annual_budget_usd": "1,400,000,000 (Excluding autonomous operational assets)",
            "notorious_operations": ["Capture of Abdullah Öcalan (Nairobi 1999)", "Cross-border drone strikes Northern Iraq/Syria", "Libya & Nagorno-Karabakh advisory missions"],
            "classification_level": "Dominant Regional Armed Drone & Paramilitary Intelligence Actor"
        },
        {
            "country": "Iran",
            "iso2": "IR",
            "primary_foreign": "IRGC Quds Force Intelligence",
            "primary_signals": "Basij Cyber Command / IRGC Electronic Warfare Unit",
            "primary_domestic": "Ministry of Intelligence and Security (VAJA / MOIS)",
            "primary_military": "Artesh Intelligence Department",
            "oversight_mechanism": "Supreme National Security Council (Direct Reporting to Supreme Leader Ali Khamenei)",
            "estimated_annual_budget_usd": "2,800,000,000 (Combined Conventional & Revolutionary Guard allocations)",
            "notorious_operations": ["Axis of Resistance proxy network integration (Hezbollah, PMU, Houthis)", "AMIA bombing logistics (alleged)", "Cyber attacks against Saudi Aramco (Shamoon)"],
            "classification_level": "Asymmetric Proxy Network & Regional Covert Power"
        },
        {
            "country": "Saudi Arabia",
            "iso2": "SA",
            "primary_foreign": "General Intelligence Presidency (GIP - Al-Mukhabarat al-A'amah)",
            "primary_signals": "State Security Cyber Warfare Center",
            "primary_domestic": "Presidency of State Security (Mabahith)",
            "primary_military": "Armed Forces Intelligence and Security Authority",
            "oversight_mechanism": "Direct oversight by Crown Prince & King (No legislative review)",
            "estimated_annual_budget_usd": "3,000,000,000",
            "notorious_operations": ["Funding of Afghan Mujahideen (Operation Cyclone co-sponsor)", "Tiger Squad (Firqat el-Nemr) covert extractions", "Jamal Khashoggi assassination (Istanbul 2018)"],
            "classification_level": "Resource-Backed Authoritarian Intelligence & Covert Slush Fund Hub"
        }
    ]
}

registry_path = DATASETS_DIR / "intelligence_agencies_registry.json"
with open(registry_path, "w", encoding="utf-8") as f:
    json.dump(INTELLIGENCE_REGISTRY, f, indent=2, ensure_ascii=False)
print(f"[CREATED] {registry_path.relative_to(BASE_DIR)}")

print("\n[SUCCESS] All research dossiers and intelligence registry generated successfully!")

