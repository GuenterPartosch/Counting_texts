#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# menu_multizaehlen_ini.py

# (C) Günter Partzosch 2018-2020

# Stand: 2018-08-20
# 1.0.0: 2017-02-19: Anfangsversion; aus menu_zaehlen_ini.py entwickelt
# 1.1.0: 2017-07-18: Erweiterung für -sd, -cd
# 1.1.1: 2017-07-20
# 1.1.2: 2018-08-17
# 1.1.3: 2018-08-21: Variable cd
# 1.1.4: 2020-07-22: erste drei Zeilen dieser Datei
# 1.1.5: 2020-07-27: kleine Korrekturen
# 1.1.6: 2020-08-04: kleine Korrekturen
# 1.1.7: 2020-08-12: Anpassung an Zaehlen.py und zaehlen_ini.py
# 1.1.8: 2020-08-15: Ausgabe-Strings in diese ini-Datei verlagert

# --------------------------------------------------------
# Abhängigkeiten:
# menu_multizaehlen_ini.py
# + wird von menu_multizaehlen.py als Modul geladen
# + lädt multizaehlen_ini.py als Modul

from multizaehlen_ini import * # Konfiguration/Initialisierung von multizaehlen.py

# ----------------------------------------------------
instverz         = '.'
programmname     = "multizaehlen.py"
programmname2    = "zaehlen.py"
programmtitle    = "Vergleich von Textauszählungen; Eingabemenü für das Programm "

menu_multizaehlen_datum       = "2020-08-15" # menu_multizaehlen
menu_multizaehlen_version     = "1.2.8"      # menu_multizaehlen

menu_multizaehlen_ini_datum   = "2020-08-15" # menu_multizaehlen_ini
menu_multizaehlen_ini_version = "1.1.8"      # menu_multizaehlen_ini

menue_zaehlen_datum           = "2018-08-09" # menu_zaehlen

menue_zaehlen_ini_datum       = "2020-08-12" # menu_zaehlen_ini

multizaehlen_datum            = "2020-08-15" # multizaehlen
multizaehlen_version          = "1.11.0"     # multizaehlen

multizaehlen_ini_datum        = "2020-08-15" # multizaehlen_ini

zaehlen_datum                 = "2020-08-12" # zaehlen
zaehlen_vers                  = "2.14.0"     # zaehlen

zaehlen_ini_datum             = "2020-08-12" # zaehlen_ini

msg1                          = "Eingabefelder/Checkboxen"
msg2                          = "Schaltflächen"
msg3                          = "Erläuterungen"
msg4                          = "Version(en)"
tuple_text                    = 'Tupel mit {0} Datei(en)'
error_text                    = "Fehler"
execution_text                = "Bearbeitung"
end_text                      = "Programm menu_zaehlen beendet"
call_text                     = "Aufruf"
pickle_files                  = "Pickle-Dateien"
all_files                     = "Alle Dateien"

# ----------------------------------------------------
# Konfiguration für Labels und Felder
#
# Sequenz von 4-elementigen Listen:
# (Label, assoziierte Variable, assoziierter Aufruf-Parameter, Parameter-Typ)
#   Label: Text, der das Feld kennzeichnet
#   assoziierte Variable: Vorbesetzung des Feldes (aus multizaehlen_ini.py)
#   assoziierter Aufruf-Parameter: Aufruf-Parameter, den multizaehlen.py erwartet
#   Parameter-Typ: Hinweis, wie Eingaben weiter bearbeitet werden
#                  1: Parameter erwartet einen Wert; spezielle Behandlung bei leerer Eingabe
#                  2: Parameter erwartet einen Wert; wird normal weiter verarbeitet
#                  3: Parameter erwartet keinen Wert
#                  4: wie 3; zusätzlich wird eine Checkbox abgefragt

conf = [
("[E0] Eingabedatei(en)",  in_name,               "",   0),
("[E1] " + sort1_text,     sort_first,            "-s1",2),
("[E2] " + sort2_text,     sort_second,           "-s2",2),
("[E3] " + out_text,       out_name,              "-o", 1),
("[E4] " + template_text,  word_template,         "-t", 2),
("[E5] " + lengths_text,   p_lengths,             "-l", 2),
("[E6] " + rank_text,      p_rank,                "-r", 2),
("[E7] " + freq_text,      p_frequency,           "-f", 2),
("[E8] " + files_anz_text, p_files,               "-fi",2),
("[C0] " + fd_text,        frequency_distribution,"-fd",4),
("[C1] " + ld_text,        length_distribution,   "-ld",4),
("[C2] " + sd_text,        separator_distribution,"-sd",4),
("[C3] " + cd_text,        character_distribution,"-cd",4)
]

# ----------------------------------------------------
# Konfiguration für Buttons

button_conf =[
('[B0] Durchsuchen... [Eingabedatei(en)]', "ask_in_file", 0, 2),
('[B1] Zurücksetzen',             "reset_entry_fields",  13, 0),
('[B2] Löschen     ',             "clear_entry_fields",  13, 1),
('[B3] Start       ',             "start",               14, 0),
('[B4] Beenden     ',             "mm.destroy",          14, 1),
('[B5] Eingabefelder/Checkboxen', "hilfe1",              13, 2),
('[B6] Schaltflächen',            "hilfe2",              13, 3),
('[B7] Erläuterungen',            "hilfe3",              14, 2),
('[B8] Version(en)',              "version",             14, 3)
]

# ----------------------------------------------------
# Hilfe
# Text für Hilfetext 1
hilfe_text1 = programmtitle + programmname + ':\n\n'
hilfe_text1 += programmname + """
(*) verarbeitet pkl-Dateien, die durch Aufrufe von """ + programmname2 + """ erzeugt wurden, weiter.\n\n"""
hilfe_text1 += """Es stehen folgende Eingabefelder/Checkboxen von """ + programmname + """ zur Verfügung
(Voreinstellungen jeweils in runden Klammern):\n\n"""
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
(*) zu [E0] und [E3]: erwartet werden korrekte Namen für Dateien
(*) zu [E0]: mittels einer Schaltfläche ([B0]) können Dateien (plk-Dateien) ausgewählt werden
(*) zu [E4]: Erwartet werden korrekte Muster (reguläre Ausdrücke).
(*) zu [E4]: Muster für zu berücksichtigende Wörter;
    Voreinstellung bedeutet: alle Wörter aus mindestens einem beliebigen Zeichen.
    '^[aeiou]+en$' : nur Wörter, die mit einem kleinen Vokal beginnen und auf "en" enden
(*) zu [E1] und [E2]: Angaben für Sortierungen; nur die aufgeführten Angaben sind möglich;
    "+" aufsteigend,
    "-" absteigend
(*) zu [E1]: 1. Sortierung; mögliche Angaben:
    a+/a-: Groß- und Kleinbuchstaben sind eingereiht;
    A+/A-: Groß- und Kleinbuchstaben sind nicht eingereiht
(*) zu [E2]: 2. Sortierung:
    L+/L-: Sortierung nach Wortlängen;
    F+/F-: Sortierung nach Worthäufigkeiten;
    D+/D-: Sortierung nach Dateizahl
(*) zu [E5]-[E8]: Beschränkung der Ausgabe:
    + Wortlängen ([E5]),
    + Rangfolgen ([E6]),
    + Worthäufigkeiten ([E7]) und
    + Dateizahl ([E8])
    z.B. bedeutet '2, 100' bei [E7]: alle Wörter, die 2-mal bis 99-mal vorkommen

(*) zu [B1]-[B4]: Schaltflächen zum Steuern des Programms
(*) [B1]=setzt alle Eingabefelder auf Voreinstellungen zurück
    [B2]=löscht alle Eingabefelder
    [B3]=startet das Programm mit eingegebenen/ausgewählten Werten
    [B4]=beendet das Programm ohne Berechnung
    [B5]=Ausgabe eines Informationstextes: Eingabefelder/Checkboxen
    [B6]=Ausgabe eines Informationstextes: Schaltflächen
    [B7]=Ausgabe eines Informationstextes: Erläuterungen
    [B8]=Ausgabe eines Informationstextes: Version(en) der beteiligten Programme
"""

# --------------------------------------------------------
# Text für Hilfetext "version"
version_text = """
Aufrufkette
=======
menu_multizaehlen.py 
   ---ruft---> menu_multizaehlen_ini.py
   ---ruft---> multizaehlen.py
multizaehlen.py
   ---ruft---> multizaehlen_ini.py
zaehlen.py
   ---ruft---> zaehlen_ini.py

Versionen der beteiligten Programme:
========================
menu_multizaehlen.py [Oberfläche zum Aufruf von multizaehlen]
"""
version_text += "   " + menu_multizaehlen_version + ": " + menu_multizaehlen_datum
version_text += "\nmultizaehlen.py [vergleichende Darstellung mehrerer Aufrufe von zaehlen]\n"
version_text += "   " + multizaehlen_version + ": " + multizaehlen_datum
version_text += "\nzaehlen.py [Programm zum Auszählen von Texten]\n"
version_text += "   " + zaehlen_vers + ": " + zaehlen_datum
version_text += """\n\nVersionen der beteiligten Konfigurationsdateien:
===============================
menu_multizaehlen_ini.py [Konfiguration für menu_multizaehlen.py]\n"""
version_text += "   " + menue_zaehlen_ini_datum
version_text += "\nmultizaehlen_ini.py [Konfiguration für multizaehlen.py]\n"
version_text += "   " + multizaehlen_ini_datum
version_text += "\nzaehlen_ini.py [Konfiguration für zaehlen.py]\n"
version_text += "   " + zaehlen_ini_datum
