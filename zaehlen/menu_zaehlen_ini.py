#!/usr/bin/python
# -*- coding: utf-8 -*-

# menu_zaehlen_ini.py
# Stand: 2018-08-20

# --------------------------------------------------------
# Abhängigkeiten
# menu_zaehlen_ini.py
# + wird von menu_zaehlen.py als Modul geladen
# + lädt zaehlen_ini.py als Modul

from zaehlen_ini import * # Konfiguration/Initialisierung von zaehlen.py

# --------------------------------------------------------
instverz      = 'D:/Python/zaehlen'
programmname = "zaehlen.py"
programmtitle= "Auszählen eines Textes; Eingabemenü für das Programm "

# Konfiguration für Labels und Felder/Checkboxen
# Sequenz von 4-elementigen Listen:
# (Label, assoziierte Variable, assoziierter Aufruf-Parameter, Parameter-Typ)
#   Label: Text, der das Feld kennzeichnet
#   assoziierte Variable: Vorbesetzung des Feldes (aus zaehlen_ini.py)
#   assoziierter Aufruf-Parameter: Aufruf-Parameter, den zaehlen.py erwartet
#   Parameter-Typ: Hinweis, wie Eingaben weiter bearbeitet werden
#     1: Parameter erwartet einen Wert; spezielle Behandlung bei leerer Eingabe
#     2: Parameter erwartet einen Wert; wird normal weiter verarbeitet
#     3: Parameter erwartet keinen Wert
#     4: wie 3; zusätzlich wird eine Checkbox abgefragt

conf = [
("[E0] Eingabedatei(en)",                           in_name,               "-i", 1),
("[E1] Wort-Trennzeichen [Muster]",                 separator,             "-s", 2),
("[E2] Datei mit Stop-Wörter",                      stop_name,             "-S", 2),
("[E3] Datei mit Go-Wörter",                        go_name,               "-G", 2),
("[E4] 1. (alph.) Sortierung [a+|a-|A+|A-]",        sort_first,            "-s1",2),
("[E5] 2. Sortierung [L+|L-|F+|F-]",                sort_second,           "-s2",2),
("[E6] Ausgabedatei(en)",                           out_name,              "-o", 1),
("[E7] Beschränkung auf bestimmte Wörter [Muster]", word_template,         "-t", 2),
("[E8] Beschränkung auf bestimmte Wortlängen",      p_lengths,             "-l", 2),
("[E9] Beschränkung auf bestimmte Rangfolge",       p_rank,                "-r", 2),
("[E10] Beschränkung auf best. Worthäufigkeiten",   p_frequency,           "-f", 2),
("[C0] Worthäufigkeiten-Verteilung berechnen",      frequency_distribution,"-fd",4),
("[C1] Wortlängen-Verteilung berechnen",            length_distribution,   "-ld",4),
("[C2] Trennzeichen-Verteilung berechnen",          separator_distribution,"-sd",4),
("[C3] Zeichen-Verteilung berechnen",               character_distribution,"-cd",4)
]

# Konfiguration für Buttons
button_conf = [
('[B0] Durchsuchen... [Eingabedatei(en)]', "ask_in_file",         0, 2),
('[B1] Durchsuchen... [Stop-Datei]',   "ask_stop_file",       2, 2),
('[B2] Durchsuchen... [Go-Datei]',     "ask_go_file",         3, 2),
##('[B3] Durchsuchen... (Ausgabedatei)', "ask_out_file",        6, 2),
('[B4] Zurücksetzen',                  "reset_entry_fields", 16, 0),
('[B5] Löschen',                       "clear_entry_fields", 16, 1),
('[B6] Start',                         "start",              17, 0),
('[B7] Beenden',                       "mm.destroy",         17, 1),
('[B8] Eingabefelder/Checkboxen',      "hilfe1",             16, 2),
('[B9] Schaltflächen',                 "hilfe2",             17, 2),
('[B10] Erläuterungen',                "hilfe3",             16, 3),
('[B11] Version(en)',                  "version",            17, 3)
]

# --------------------------------------------------------
# Text für Hilfetext 1
hilfe_text1 = programmtitle + programmname + ':\n\n'
hilfe_text1 += "Es stehen folgende Eingabefelder/Checkboxen zur Verfügung (Voreinstellung in runden Klammern):\n\n"
for f in range(len(conf)):
    hilfe_text1 += str(conf[f][0]) + " (" + str(conf[f][1]) + "); für Parameter " + conf[f][2] + "\n"

# --------------------------------------------------------
# Text für Hilfetext 2
hilfe_text2 = "Es gibt folgende Schaltflächen:\n\n"
for f in range(len(button_conf)): 
    hilfe_text2 += str(button_conf[f][0]) + "; ruft '" + str(button_conf[f][1]) + "'\n"

# --------------------------------------------------------
# Text für Hilfetext 3
hilfe_text3 = """
Erläuterungen:

(*) zu [E0], [E2], [E3] und [E6]: erwartet werden korrekte Namen für Dateien
(*) zu [E2] und [E3]: mittels einer Schaltfläche ([B1] bzw. [B2]) kann eine einzelne Datei ausgewählt werden
(*) zu [E0]: mittels der Schaltfläche [B0] können mehrere Eingabedateien ausgewählt werden. Für jede Datei wird das Programm ausgeführt.
(*) zu [E2]: Wörter in dieser Datei (jeweils ein Wort pro Zeile) werden nicht berücksichtigt.
(*) zu [E3]: Nur Wörter in dieser Datei (jeweils ein Wort pro Zeile) werden berücksichtigt.
(*) zu [E1] und [E7]: Erwartet werden korrekte Muster (reguläre Ausdrücke).
(*) zu [E1]: Bei diesen Zeichen werden Eingabezeilen in "Wörter" aufgespalten.
(*) zu [E4] und [E5]: Angaben für Sortierungen; nur die aufgeführten Angaben sind möglich; "+" aufsteigend, "-" absteigend
(*) zu [E4]: erstrangige (alphabetische) Sortierung:
    a+/a-: Groß-/Kleinbuchstaben sind eingereiht;
    A+/A-: Groß-/Kleinbuchstaben sind nicht eingereiht
(*) zu [E5]: zweitrangige Sortierung:
    L+/L-: Sortierung nach Wortlängen;
    F+/F-: Sortierung nach Worthäufigkeiten
(*) zu [E7]-[E10]: Beschränkung der Ausgabe:
(*) zu [E7]: Beschränkung auf bestimmte Wortmuster; die Voreinstellung bedeutet: alle Wörter aus mindestens einem beliebigen Zeichen.
    Beispiel: '^[aeiou]+en$': nur Wörter, die mit einem kleinen Vokal beginnen und auf "en" enden
(*) zu [E8]: Beschränkung auf bestimmte Wortlängen
    Beispiel: '2,10': alle Wörter mit 2-9 Zeichen
(*) zu [E9]: Beschränkung auf bestimmte Rangfolgen
(*) zu [E10]: Beschränkung auf bestimmte Worthäufigkeiten
    Beispiel: '2,200': alle Wörter, die 2-mal bis 199-mal vorkommen
(*) zu [C0]: Verteilung der Worthäufigkeiten wird berechnet; keine Berechnung, wenn nicht ausgewählt
(*) zu [C1]: Verteilung der Wortlängen wird berechnet; keine Berechnung, wenn nicht ausgewählt
(*) zu [C2]: Verteilung der Trennzeichenhäufigkeiten wird berechnet; keine Berechnung, wenn nicht ausgewählt
(*) zu [C3]: Verteilung der Zeichenhäufigkeiten wird berechnet; keine Berechnung, wenn nicht ausgewählt

(*) zu [B0]-[B2]: Schaltflächen für die Auswahl von Dateien
(*) zu [B4]-[B7]: Schaltflächen zum Steuern des Programms
(*) zu [B4]: setzt alle Eingabefelder auf Voreinstellungen zurück
(*) zu [B5]: löscht alle Eingabefelder
(*) zu [B6]: Start des Programms mit eingegebenen Werten
(*) zu [B7]: Beendigung des Programms ohne Berechnung;
(*) zu [B8]: Hilfetext: hier für Eingabefelder/Checkboxen
(*) zu [B9]: Hilfetext: hier für Schaltflächen
(*) zu [B10]: Hilfetext: hier für zusätzliche Erläuterungen
(*) zu [B11]: Ausgabe eines Informationstextes: Version(en) der beteiligten Programme
"""

# --------------------------------------------------------
# Text für Hilfetext "version"
version_text = """
menu_zaehlen.py     ---ruft---> menu_zaehlen_ini.py2
                    ---ruft---> zaehlen.py
zaehlen.py          ---ruft---> zaehlen_ini.py

Versionen der beteiligten Programme:

zaehlen.py [Programm zum Auszählen von Texten]
    2.11.7: 2018-08-17
menu_zaehlen.py [Menü für den Aufruf von zaehlen.py]
    2018-08-19

Versionen der beteiligten Konfigurationsdateien:

menu_zaehlen_ini.py [Konfiguration für menu_zaehlen.py]
    2018-08-19
zaehlen_ini.py [Konfiguration für zaehlen.py]
    2018-08-17
"""
