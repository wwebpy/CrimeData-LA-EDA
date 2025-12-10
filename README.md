# 🚔 Los Angeles Crime Analysis & Dashboard

Interaktive Analyse von Kriminalitätsdaten der Los Angeles Police Department (LAPD) zwischen 2020 und heute.  
Dieses Projekt kombiniert eine **Explorative Datenanalyse (EDA)** mit einem **interaktiven Streamlit-Dashboard**, um Muster, Trends und Zusammenhänge zu visualisieren.

## 📸 Dashboard Preview

<p align="center">
  <img src="img/Crimes Overview.png" width="49%">
  <img src="img/C1.png" width="49%">
</p>
<p align="center">
  <img src="img/Time Analysis.png" width="33%">
  <img src="img/T1.png" width="33%">
  <img src="img/T2.png" width="33%">
</p>
<p align="center">
  <img src="img/Location Analysis.png" width="49%">
  <img src="img/L1.png" width="49%">
</p>
<p align="center">
  <img src="img/Victims Analysis.png" width="33%">
  <img src="img/V1.png" width="33%">
  <img src="img/V2.png" width="33%">
</p>
---

## 📌 Projektziel

Ziel des Projektes ist es, zentrale Fragen zur Kriminalität in Los Angeles aus einer Datenperspektive zu beantworten:

- Welche Straftaten treten am häufigsten auf?
- Welche Delikte beinhalten den Einsatz von Waffen?
- Wie verteilt sich Kriminalität über **Tageszeit und Wochentag**?
- Wo befinden sich **Hotspots** innerhalb von Los Angeles?
- Welche **Opfergruppen** sind besonders betroffen (Alter, Geschlecht, Herkunft)?

Das Projekt folgt einer typischen **Data-Science-Pipeline**:
**Datenbereinigung → Feature Engineering → EDA → Visualisierung → Dashboard**

---
## 🧠 Erkenntnisse

Anhand der EDA konnten folgende Erkenntnise gezogen werden.

Crimes Overview:
- In Los Angeles sind Autodiebstähle mit großem Abstand das häufigste Verbrechen (mit 13,3%), gefolgt von einfachen Körperangriffen (8,6%) und Diebstählen aus Fahrzeugen (7,3%), was zeigt, dass vor allem Alltags- und Eigentumskriminalität das Stadtbild prägen.
- Bei Straftaten mit Waffen treten einfache Körperangriffe und schwere Übergriffe am häufigsten auf, gefolgt von Raub und Bedrohungen, was zeigt, dass Waffeneinsatz in Los Angeles vor allem bei körperlichen Auseinandersetzungen und Raubsituationen vorkommt.

Times Analysis:
- Die meisten Straftaten passieren in Los Angeles Mittags um 12 Uhr (6,7% aller Straftaten) und Nachmittags um 18 Uhr (6,0% aller Straftaten), während die frühen Morgenstunden deutlich weniger betroffen sind, was zeigt, dass Kriminalität stark mit aktiven Tageszeiten und sozialem Leben zusammenhängt.
- Am meisten Kriminalität gibt es freitags und samstags, während Dienstag und Sonntag am niedrigsten liegen, was zeigt, dass Ausgehzeiten und Nachtleben ein höheres Risiko für Straftaten mit sich bringt.

Location:
- Die Kriminalität konzentriert sich aufgrund der Einwohneranzahl stark auf bestimmte Stadtbereiche, besonders in dicht besiedelten Zonen rund um Downtown und zentrale Stadtteile, während Außenbereiche deutlich weniger betroffen sind.
- Im Vergleich aller LAPD-Bezirke treten die meisten Straftaten in Central (6,7%), 77th Street (6,1%) und Pacific (5,9%) auf, während Bezirke wie Foothill und Hollenbeck deutlich weniger betroffen sind, was zeigt, dass Kriminalität in Los Angeles stark von der Lage und urbanen Dichte abhängt.

Victim Profile:
- Die meisten Opfer sind junge Erwachsene zwischen etwa 30 und 40 Jahren, was zeigt, dass diese Altersgruppe am häufigsten von Straftaten betroffen ist.
- Die Mehrheit der Opfer sind Männer.
- Die meisten Opfer gehören zur Gruppe Hispanic/Latin/Mexican, gefolgt von White und Black, was sowohl die Bevölkerungsstruktur in Los Angeles widerspiegelt.

---

## 📊 Explorative Datenanalyse (EDA)

Die EDA wurde in Jupyter Notebook durchgeführt und umfasst:

### 🧹 Datenbereinigung
- Entfernen ungültiger Koordinaten (`LAT/LON = 0`)
- Konvertierung von Datumsfeldern
- Umgang mit Nullwerten bei Waffenfeldern
- Mapping von Ethnizitätscodes (`VICT_DESCENT_FULL`)
- Filtern unvollständiger Daten (2024/2025)

### 🧠 Feature Engineering
- `OCC_YEAR`, `OCC_MONTH`, `OCC_WEEKDAY`
- `OCC_HOUR`: Stunde der Tat (0–23)
- `IS_WEEKEND`: Wochenende vs. Wochentag

### 📈 Analysen
- Top-20 Straftaten
- Top-15 Delikte mit Waffe
- Crime-Verteilung über Tagesstunden
- Crime-Verteilung über Wochentage
- Heatmap: Hour × Weekday
- Hotspots auf Kartenbasis (LAT/LON)
- Analyse der Opfer nach Alter, Geschlecht und Herkunft

---

## 🖥️ Dashboard (Streamlit)

Das Dashboard bietet **interaktive Filter**:

- Mehrfachselektion nach Jahr
- Mehrfachselektion nach LAPD-Area

### 🔎 Tabs
- **Crimes Overview**
- **Time Analysis**
- **Location**
- **Victim Profile**

