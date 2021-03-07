#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# menu_multizaehlen_ini.py

# (C) Günter Partzosch 2017-2021

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
# 1.1.9: 2020-08-20: Ausgabe-Strings überarbeitet
# 1.1.10: 2020-08-26: ini-datei kann jetzt robust geladen werden
# 1.1.11: 2020-08-27: Konstrukt für Programm-Versionen und -Daten vereinheitlicht
# 1.1.12: 2021-03-06: kl. Fehlerkorrektur

# Todos:
# + Laden der ini-Datei robuster gestalten

# --------------------------------------------------------
# Abhängigkeiten:
# menu_multizaehlen_ini.py
# + wird von menu_multizaehlen.py als Modul geladen
# + lädt multizaehlen_ini.py als Modul


# ----------------------------------------------------
     
# do not touch!

instverz         = '.'
program_name     = "multizaehlen.py"
program_name2    = "zaehlen.py"

menu_multizaehlen_date       = "2020-08-27" # menu_multizaehlen.py
menu_multizaehlen_vers       = "1.2.10"     # menu_multizaehlen.py

menu_multizaehlen_ini_date   = "2021-03-06" # menu_multizaehlen_ini.py
menu_multizaehlen_ini_vers   = "1.1.12"     # menu_multizaehlen_ini.py

menu_zaehlen_date            = "2018-08-30" # menu_zaehlen.py

menu_zaehlen_ini_date        = "2020-08-30" # menu_zaehlen_ini.py

multizaehlen_date            = "2020-08-26" # multizaehlen.py
multizaehlen_vers            = "1.11.2"     # multizaehlen.py

multizaehlen_ini_date        = "2020-08-26" # multizaehlen_ini.py

zaehlen_date                 = "2020-08-30" # zaehlen.py
zaehlen_vers                 = "2.15.1"     # zaehlen.py

zaehlen_ini_date             = "2020-08-30" # zaehlen_ini.py

# ----------------------------------------------------
# Ausgabe-Strings

programmtitle                 = "Vergleich von Textauszählungen; Eingabemenü für das Programm "
                                                                        # Comparison of text countings; Menu for the program
msg1                          = "Eingabefelder/Checkboxen"              # Input fileds/check boxes
msg2                          = "Schaltflächen"                         # Buttons
msg3                          = "Erläuterungen"                         # INformations
msg4                          = "Version(en)"                           # Version(s)
tuple_text                    = 'Tupel mit {0} Datei(en)'               # Tuple with {0} file(s)
error_text                    = "Fehler"                                # Error
execution_text                = "Bearbeitung"                           # Processing
end_text                      = "Programm menu_zaehlen beendet"         # Program menu_zaehlen finished
call_text                     = "Aufruf"                                # Call
pickle_files                  = "Pickle-Dateien"                        # Pickle file(s)
all_files                     = "Alle Dateien"                          # All files

# ----------------------------------------------------
# Strings für Schaltflächen

B0_text                       = 'Durchsuchen... [Eingabedatei(en)]'     # Browse..., [input file(s)]
B1_text                       = 'Zurücksetzen'                          # Reset
B2_text                       = 'Löschen'                               # Delete all
B3_text                       = 'Start'                                 # Start
B4_text                       = 'Beenden'                               # Finish
B5_text                       = 'Eingabefelder/Checkboxen'              # Input fields / check boxes 
B6_text                       = 'Schaltflächen'                         # Buttons
B7_text                       = 'Erläuterungen'                         # Informations
B8_text                       = 'Version(en)'                           # Version(s)
               
# ----------------------------------------------------
# Ausgabe-Strings für Hilfe

tmp1 = "verarbeitet pkl-Dateien, die durch Aufrufe von"                 # processes pkl files, by calls of 
tmp2 = "erzeugt wurden, weiter"                                         # have been generated
tmp3 = "Es gibt folgende Eingabefelder/Checkboxen von"                  # There are the following input fields/check boxes in
tmp4 = "(Voreinstellungen jeweils in eckigen Klammern)"                 # (Defaults always in brackets)
tmp5 = "für Parameter"                                                  # for parameter
tmp6 = "Es gibt folgende Schaltflächen"                                 # There are the following buttons
tmp7 = "ruft"                                                           # calls

# ----------------------------------------------------
# Konfiguration für Labels und Felder                                   # Configuration of labels and fields
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

# do not touch!

conf = [
("[E0] Eingabedatei(en)",  in_name,               "",   0),
("[E1] (-s1) " + sort1_text,     sort_first,            "-s1",2),
("[E2] (-s2) " + sort2_text,     sort_second,           "-s2",2),
("[E3] (-o) "  + out_text,       out_name,              "-o", 1),
("[E4] (-t) "  + template_text,  word_template,         "-t", 2),
("[E5] (-l) "  + lengths_text,   p_lengths,             "-l", 2),
("[E6] (-r) "  + rank_text,      p_rank,                "-r", 2),
("[E7] (-f) "  + freq_text,      p_frequency,           "-f", 2),
("[E8] (-fi) " + files_anz_text, p_files,               "-fi",2),
("[C0] (-fd) " + fd_text,        frequency_distribution,"-fd",4),
("[C1] (-ld) " + ld_text,        length_distribution,   "-ld",4),
("[C2] (-sd) " + sd_text,        separator_distribution,"-sd",4),
("[C3] (-cd) " + cd_text,        character_distribution,"-cd",4)
]

# ----------------------------------------------------
# Konfiguration für Buttons (Schaltflächen)                              # Configuration of buttons

# do not touch!

button_conf =[
('[B0] ' + B0_text, "ask_in_file",          0, 2),
('[B1] ' + B1_text, "reset_entry_fields",  13, 0),
('[B2] ' + B2_text, "clear_entry_fields",  13, 1),
('[B3] ' + B3_text, "start",               14, 0),
('[B4] ' + B4_text, "mm.destroy",          14, 1),
('[B5] ' + B5_text, "hilfe1",              13, 2),
('[B6] ' + B6_text, "hilfe2",              13, 3),
('[B7] ' + B7_text, "hilfe3",              14, 2),
('[B8] ' + B8_text, "version",             14, 3)
]


# ----------------------------------------------------
# Hilfe

# Text für Hilfetext 1

hilfe_text1 = programmtitle + program_name + ':\n\n'
hilfe_text1 += "{3}\n(*) {0} {1} {2}".format(tmp1, program_name2, tmp2, program_name) + ".\n\n"
hilfe_text1 += "{0} {1} {2}".format(tmp3, program_name, tmp4) + ":\n\n"
for f in range(len(conf)):
    hilfe_text1 += "{0} [{1}]; {2} {3}".format(str(conf[f][0]), str(conf[f][1]), tmp5, conf[f][2]) + "\n"

# --------------------------------------------------------
# Text für Hilfetext 2

hilfe_text2 = tmp6 + ":\n\n"
for f in range(len(button_conf)): 
    hilfe_text2 += "{0} {1} '{2}'".format(str(button_conf[f][0]), tmp7, str(button_conf[f][1])) + "\n"

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
version_text += "   " + menu_multizaehlen_vers + ": " + menu_multizaehlen_date
version_text += "\nmultizaehlen.py [vergleichende Darstellung mehrerer Aufrufe von zaehlen]\n"
version_text += "   " + multizaehlen_vers + ": " + multizaehlen_date
version_text += "\nzaehlen.py [Programm zum Auszählen von Texten]\n"
version_text += "   " + zaehlen_vers + ": " + zaehlen_date
version_text += """\n\nVersionen der beteiligten Konfigurationsdateien:
===============================
menu_multizaehlen_ini.py [Konfiguration für menu_multizaehlen.py]\n"""
version_text += "   " + menu_zaehlen_ini_date
version_text += "\nmultizaehlen_ini.py [Konfiguration für multizaehlen.py]\n"
version_text += "   " + multizaehlen_ini_date
version_text += "\nzaehlen_ini.py [Konfiguration für zaehlen.py]\n"
version_text += "   " + zaehlen_ini_date

