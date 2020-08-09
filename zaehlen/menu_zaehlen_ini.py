#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# (C) Günter Partosch 2018-2020

# menu_zaehlen_ini.py

# Stand: 2018-08-20
# Stand: 2019-12-12
# Stand: 2020-07-27
# Stand: 2020-08-04
# Stand: 2020-08-07
# Stand: 2020-08-08 (Ausgabe-Strings parametrisiert)
# Stand: 2020-08-08 (ini-Datei jetzt robuster geladen)
# Stand: 2020-08-09 (Überprüfung der Eingabewerte)

# --------------------------------------------------------
# verschiedene strings

# anpassen: instverz
#instverz      = 'D:/Python/zaehlen'
instverz     = '.'                                              # Pfad zum ausführbaren Pogramm, ggf. anpassen
programmname = "zaehlen.py"

menue_zaehlen_ini_Datum  = "2020-08-09"                         # Datum der letzten Änderung 
menue_zaehlen_Datum      = "2020-08-09"                         # Datum der letzten Änderung

programm_vers            = "2.13.3"                             # zaehlen.py: Version
programm_datum           = "2020-08-02 "                        # zaehlen.py: Datum der letzten Änderung
zaehlen_ini_Datum        = "2020-08-02"                         # zaehlen_ini.py: Datum der letzten Änderung

msg1                     = "Hilfe 1"
msg2                     = "Hilfe 2"
msg3                     = "Hilfe 3"
tuple_text               = 'Tupel mit {0} Datei(en)'
error_text               = "Fehler"
execution_text           = "Bearbeitung"
end_text                 = "Programm menu_zaehlen beendet"
call_text                = "Aufruf"

programmtitle            = "Auszählen eines Textes; Eingabemenü für das Programm "
E0_text                  = "[E0] Eingabedatei(en)"
E1_text                  = "[E1] Wort-Trennzeichen [Muster]"
E2_text                  = "[E2] Datei mit Stop-Wörter"
E3_text                  = "[E3] Datei mit Go-Wörter"
E4_text                  = "[E4] 1. (alph.) Sortierung [a+|a-|A+|A-]"
E5_text                  = "[E5] 2. Sortierung [L+|L-|F+|F-]"
E6_text                  = "[E6] Ausgabedatei(en)"
E7_text                  = "[E7] Beschränkung auf bestimmte Wörter [Muster]"
E8_text                  = "[E8] Beschränkung auf bestimmte Wortlängen"
E9_text                  = "[E9] Beschränkung auf bestimmte Rangfolge"
E10_text                 = "[E10] Beschränkung auf best. Worthäufigkeiten"

C0_text                  = "[C0] Worthäufigkeiten-Verteilung berechnen"
C1_text                  = "[C1] Wortlängen-Verteilung berechnen"
C2_text                  = "[C2] Trennzeichen-Verteilung berechnen"
C3_text                  = "[C3] Zeichen-Verteilung berechnen"

B0_text                  = '[B0] Durchsuchen... [Eingabedatei(en)]'
B1_text                  = '[B1] Durchsuchen... [Stop-Datei]'
B2_text                  = '[B2] Durchsuchen... [Go-Datei]'
B4_text                  = '[B4] Zurücksetzen'
B5_text                  = '[B5] Löschen'
B6_text                  = '[B6] Start'
B7_text                  = '[B7] Beenden'
B8_text                  = '[B8] Eingabefelder/Checkboxen'
B9_text                  = '[B9] Schaltflächen'
B10_text                 = '[B10] Erläuterungen'
B11_text                 = '[B11] Version(en)'

err_ini_text             = "--- Warnung: Initialisierungsdatei {0} kann nicht geladen werden; --> Voreinstellungen genommen"
err_value_text           = "Fehler '{1}' bei '{0}'; --> Voreinstellung genommen"
err1_file_text           = "Datei '{1}' bei '{0}' kann nicht geöffnet werden; --> Voreinstellung genommen"
err2_file_text           = "Datei '{1}' bei '{0}' kann nicht geöffnet werden; --> korrigieren + Neustart"

# --------------------------------------------------------
# Abhängigkeiten
# menu_zaehlen_ini.py
# + wird von menu_zaehlen.py als Modul geladen
# + lädt zaehlen_ini.py als Modul

try:                             # Initialisierung für Programm-Parameter und Variablen einlesen
    from zaehlen_ini import *    # Konfiguration/Initialisierung von zaehlen.py
except ImportError:
    print(err_ini_text.format("zaehlen_ini"))
    in_name                = "./in.txt"
    out_name               = "./out.txt"
    stop_name              = ""
    go_name                = ""
    separator              = """[\s.,;:!?<>()\[\]{}"'…—–“”„‘’`+»«‹–›0-9|/=_%*$&]+"""
    word_template          = """^.+$"""
    p_lengths              = "1,100"
    p_frequency            = "1,12000"
    p_rank                 = "1,50000"
    sort_first             = "a+"
    sort_second            = ""
    frequency_distribution = False
    length_distribution    = False
    separator_distribution = False
    character_distribution = False

    integer_breite         = 7  # Ausgabebreite für Integer
    integer_breite_kl      = 3  # Ausgabebreite für kleine Integer
    string_breite          = 3  # voreingestellte Ausgabebreite für Strings
    string_breite_la       = 43 # Länge von Eingabeaufforderungen
    real_breite            = 6  # Ausgabebreite für Reals
    rndg                   = 2  # Zahl der Nachkommastellen für Reals/Floats

# --------------------------------------------------------
# Konfiguration für Labels und Felder/Checkboxen:
#
# Sequenz von 4-elementigen Listen:
# (Label, assoziierte Variable, assoziierter Aufruf-Parameter, Parameter-Typ)
#   + Label: Text, der das Feld kennzeichnet
#   + assoziierte Variable: Vorbesetzung des Feldes (aus zaehlen_ini.py)
#   + assoziierter Aufruf-Parameter: Aufruf-Parameter, den zaehlen.py erwartet
#   + Parameter-Typ: Hinweis, wie Eingaben weiter bearbeitet werden
#     1: Parameter erwartet einen Wert; spezielle Behandlung bei leerer Eingabe
#     2: Parameter erwartet einen Wert; wird normal weiter verarbeitet
#     3: Parameter erwartet keinen Wert
#     4: wie 3; zusätzlich wird eine Checkbox abgefragt

conf = [
(E0_text,   in_name,                "-i",  1),
(E1_text,   separator,              "-s",  2),
(E2_text,   stop_name,              "-S",  2),
(E3_text,   go_name,                "-G",  2),
(E4_text,   sort_first,             "-s1", 2),
(E5_text,   sort_second,            "-s2", 2),
(E6_text,   out_name,               "-o",  1),
(E7_text,   word_template,          "-t",  2),
(E8_text,   p_lengths,              "-l",  2),
(E9_text,   p_rank,                 "-r",  2),
(E10_text,  p_frequency,            "-f",  2),
(C0_text,   frequency_distribution, "-fd", 4),
(C1_text,   length_distribution,    "-ld", 4),
(C2_text,   separator_distribution, "-sd", 4),
(C3_text,   character_distribution, "-cd", 4)
]

# --------------------------------------------------------
# Konfiguration für Buttons

button_conf = [
(B0_text,  "ask_in_file",         0, 2),
(B1_text,  "ask_stop_file",       2, 2),
(B2_text,  "ask_go_file",         3, 2),
##('[B3] Durchsuchen... (Ausgabedatei)', "ask_out_file",        6, 2),
(B4_text,  "reset_entry_fields", 16, 0),
(B5_text,  "clear_entry_fields", 16, 1),
(B6_text,  "start",              17, 0),
(B7_text,  "mm.destroy",         17, 1),
(B8_text,  "hilfe1",             16, 2),
(B9_text,  "hilfe2",             17, 2),
(B10_text, "hilfe3",             16, 3),
(B11_text, "version",            17, 3)
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
# Texte für Hilfetext "version"

version_text = """
Aufrufkette:
============
menu_zaehlen.py
    ---ruft---> menu_zaehlen_ini.py
    ---ruft---> zaehlen.py
zaehlen.py
    ---ruft---> zaehlen_ini.py

Versionen der beteiligten Programme:
==========================
zaehlen.py [Programm zum Auszählen von Texten]
    """ + programm_vers + ", " + programm_datum + """
menu_zaehlen.py [Menü für den Aufruf von zaehlen.py]
    """ + menue_zaehlen_Datum + """

Versionen der beteiligten Konfigurationsdateien:
======================================
menu_zaehlen_ini.py [Konfiguration für menu_zaehlen.py]
    """ + menue_zaehlen_ini_Datum + """
zaehlen_ini.py [Konfiguration für zaehlen.py]
    """ + zaehlen_ini_Datum + """
"""
