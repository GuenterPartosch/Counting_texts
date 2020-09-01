#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# menu_zaehlen_ini.py

# (C) Günter Partosch 2018-2020

# Stand: 2018-08-20
# Stand: 2019-12-12
# Stand: 2020-07-27
# Stand: 2020-08-04
# Stand: 2020-08-07
# Stand: 2020-08-08 (Ausgabe-Strings parametrisiert)
# Stand: 2020-08-08 (ini-Datei jetzt robuster geladen)
# Stand: 2020-08-09 (Überprüfung der Eingabewerte)
# Stand: 2020-08-12 (Anpassung an zaehlen.py und zahlen_ini.py)
# Stand: 2020-08-15 (Ausgabe-Strings überarbeitet)
# Stand: 2020-08-17 (Ausgabe-Strings überarbeitet)
# Stand: 2020-08-23 (ini-Dateien entkoppelt)
# Stand: 2020-08-24 (argparse, Parameter -sm, -la)
# Stand: 2020-08-25 (vereinheitlichte Konstruktion von Programm-Datum und Programm-Version)
# Stand: 2020-08-28 (kleine Korrekturen)
# Stand: 2020-08-29 (englische Sprachausgabe vorbereitet)
# Stand: 2020-08-30 (weiter...)

# noch:
# + restliche englische Texte
# + Laden von zaehlen_ini.py noch besser abfedern

# --------------------------------------------------------
# do not touch

instverz                 = '.'                                  # Pfad zum ausführbaren Pogramm, ggf. anpassen
remote_program_name      = "zaehlen.py"
program_name             = "menu_zaehlen.py"                    # das aktuelle Menü-Programm menu_zaehlen.py

menu_zaehlen_ini_date    = "2020-08-30"                         # menu_zaehlen_ini.py: Datum der letzten Änderung

# --------------------------------------------------------
# verschiedene strings
# do not touch

E0_pre_text              = "[E0] (-i) "
E1_pre_text              = "[E1] (-s) "
E2_pre_text              = "[E2] (-S) "
E3_pre_text              = "[E3] (-G) "
E4_pre_text              = "[E4] (-s1) "
E5_pre_text              = "[E5] (-s2) "
E6_pre_text              = "[E6] (-o) "
E7_pre_text              = "[E7] (-t) "
E8_pre_text              = "[E8] (-l) "
E9_pre_text              = "[E9] (-r) "
E10_pre_text             = "[10] (-f) "
C0_pre_text              = "[C0] (-fd) "
C1_pre_text              = "[C1] (-ld) "
C2_pre_text              = "[C2] (-sd) "
C3_pre_text              = "[C3] (-cd) "
C4_pre_text              = "[C4] (-sm) "

B0_pre_text              = "[B0] "
B1_pre_text              = "[B1] "
B2_pre_text              = "[B2] "
B4_pre_text              = "[B4] "
B5_pre_text              = "[B5] "
B6_pre_text              = "[B6] "
B7_pre_text              = "[B7] "
B8_pre_text              = "[B8] "
B9_pre_text              = "[B9] "
B10_pre_text             = "[B10] "
B11_pre_text             = "[B11] "

# --------------------------------------------------------
# verschiedene strings
# can be changed

msg1                     = "Eingabefelder/Checkboxen"                         # Input fields/check boxes
msg2                     = "Schaltflächen"                                    # Buttons
msg3                     = "Erläuterungen"                                    # Comments
msg4                     = "Version(en)"                                      # Version(s)
tuple_text               = 'Tupel mit {0} Datei(en)'                          # Tuple with {0} file(s)
error_text               = "Fehler"                                           # Error
execution_text           = "Bearbeitung"                                      # Execution
end_text                 = "Programm menu_zaehlen.py beendet"                 # Program menu_zaehlen.py finioshed
call_text                = "Aufruf"                                           # Call

programmtitle            = "Auszählen eines Textes; Eingabemenü für das Programm " # Counting the words in text files: menu for the program
E0_text                  = "Eingabedatei(en)"                                 # input file(s)
E1_text                  = "Wort-Trennzeichen [Muster]"                       # word separators [template]
E2_text                  = "Datei mit Stop-Wörter"                            # file with stop words
E3_text                  = "Datei mit Go-Wörter"                              # file with go words
E4_text                  = "1. (alph.) Sortierung [a+|a-|A+|A-]"              # 1st sorting [a+|a-|A+|A-]
E5_text                  = "2. Sortierung [L+|L-|F+|F-]"                      # 2nd sorting [L+|L-|F+|F-]
E6_text                  = "Ausgabedatei(en)"                                 # Output file
E7_text                  = "Beschränkung auf bestimmte Wörter [Muster]"       # Limitation by specified word templates
E8_text                  = "Beschränkung auf bestimmte Wortlängen"            # Limitation by specified word lengths
E9_text                  = "Beschränkung auf bestimmte Rangfolge"             # Limitation by specified rank sequence
E10_text                 = "Beschränkung auf best. Worthäufigkeiten"          # Limitation by specified word frequencies

C0_text                  = "Worthäufigkeiten-Verteilung berechnen"            # Generate word frequency distribution
C1_text                  = "Wortlängen-Verteilung berechnen"                  # Generate word lengths distribution
C2_text                  = "Trennzeichen-Verteilung berechnen"                # Generate separators distribution
C3_text                  = "Zeichen-Verteilung berechnen"                     # Generate characters distribution
C4_text                  = "'Stille' Verarbeitung"                            # Silent mode

B0_text                  = 'Durchsuchen... [Eingabedatei(en)]'                # Browse...,
B1_text                  = 'Durchsuchen... [Stop-Datei]'                      # Browse...,
B2_text                  = 'Durchsuchen... [Go-Datei]'                        # Browse...,
B4_text                  = 'Zurücksetzen'                                     # Reset
B5_text                  = 'Löschen'                                          # Delete all
B6_text                  = 'Start'                                            # Start
B7_text                  = 'Beenden'                                          # Terminate
B8_text                  = 'Eingabefelder/Checkboxen'                         # Input fields/check boxes
B9_text                  = 'Schaltflächen'                                    # Buttons
B10_text                 = 'Erläuterungen'                                    # Comments
B11_text                 = 'Version(en)'                                      # Version(s)

fields_boxes_text        = "Es stehen folgende Eingabefelder/Checkboxen zur Verfügung (Voreinstellung in runden Klammern):"
                                                                              # There are the following input fields / check boxes (defaults in parentheses):
buttons_text             = "Es gibt folgende Schaltflächen:"                  # There are the following buttons:
for_parameter            = "für Parameter"                                    # for parameter
calls_text               = "ruft"                                             # calls

# --------------------------------------------------------
# error messages and warnings
# can be changed

err_ini_text             = "--- Warnung: Initialisierungsdatei {0} kann nicht geladen werden; --> Voreinstellungen genommen"
                                                                              # --- Warning: initialization file {0} could not be loaded; --> defaults taken
err_value_text           = "--- Fehler '{1}' bei '{0}'; --> Voreinstellung genommen"
                                                                              # --- Error {1} at {0}; --> defaults taken
err1_file_text           = "--- Datei '{1}' bei '{0}' kann nicht geöffnet werden; --> Voreinstellung genommen"
                                                                              # --- File {1} at {0} could not be opened; defaults taken
err2_file_text           = "--- Datei '{1}' bei '{0}' kann nicht geöffnet werden; --> korrigieren + Neustart"
                                                                              # --- File {1} at {0} could not be opened; please correct and restart
# --------------------------------------------------------
# help texts
# can be changed

comments_text = """
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
(*) zu [B7]: Beendigung des Programms ohne Berechnung
(*) zu [B8]: Hilfetext: hier für Eingabefelder/Checkboxen
(*) zu [B9]: Hilfetext: hier für Schaltflächen
(*) zu [B10]: Hilfetext: hier für zusätzliche Erläuterungen
(*) zu [B11]: Ausgabe eines Informationstextes: Version(en) der beteiligten Programme
"""
# Comments:
#  
# (*) to [E0], [E2], [E3] und [E6]: Correct names for files are exspected.
# (*) to [E2] and [E3]: You can select a file by a button ([B1] a/o [B2]).
# (*) to [E0]: You can select some input files by the button [B0]. The program is executed for every selected file.
# (*) to [E2]: Words which are found in this file (one per line) are not included in the results.
# (*) to [E3]: Only words which are found in this file (one per line) are included in the results.
# (*) to [E1] and [E7]: A correct template (regular expression) is exspected.
# (*) to [E1]: Input lines are split into words byt these characters.
# (*) to [E4] and [E5]: Specification for sorting: only the listed specifications are allowed; "+" means in ascending order, "-" in descending order.
# (*) to [E4]: 1st (alphabetic) sorting:
#     a+/a-: Sorting is not case-sensitive.
#     A+/A-: Sorting is case-sensitive.
# (*) to [E5]: 2nd sorting:
#     L+/L-: Sorting with respect to word lengths
#     F+/F-: Sorting with respect to word frenquencies
# (*) to [E7]-[E10]: Limitation of output:
# (*) to [E7]: Limitation with respect to specified word templates (regular expreession);
#     default means: all words with one character at minimum
#     Example: '^[aeiou]+en$': only words, which begin with a lower vowel [aeiou] and end with "en"
# (*) to [E8]: Limitation with respect to specified word lengths
#     Example: '2,10': all words with 2-9 characters
# (*) to [E9]: Limitation with respect to specified rank sequence
# (*) to [E10]: Limitation with respect to specified word frequencies
#     Example: '2,200': all words which are 1-199 tines listed
# (*) to [C0]: Distribution of word frequencies is calculated; there is no calculation if not choosen
# (*) to [C1]: Distribution of word engths is calculated; there is no calculation if not choosen
# (*) to [C2]: Distribution of separator frequencies is calculated; there is no calculation if not choosen
# (*) to [C3]: Distribution of character frequencies is calculated; there is no calculation if not choosen
# 
# (*) to [B0]-[B2]: Buttons for the choice of files
# (*) to [B4]-[B7]: Buttons for the managing of the program
# (*) to [B4]: Resets all input fields by defaults.
# (*) to [B5]: Clears all input fields.
# (*) to [B6]: Start of the program with the given values
# (*) to [B7]: Terminates the program without any calculation.
# (*) to [B8]: Help text: here for input fields / checkboxes
# (*) to [B9]: Help text: here for buttons
# (*) to [B10]: Help text: here for additional comments)
# (*) to [B11]: Information text: version(s) of the involved program(s)
version_help_text = """
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
    {0}, {1}
menu_zaehlen.py [Menü für den Aufruf von zaehlen.py]
    {2}

Versionen der beteiligten Konfigurationsdateien:
======================================
menu_zaehlen_ini.py [Konfiguration für menu_zaehlen.py]
    {3}
zaehlen_ini.py [Konfiguration für zaehlen.py]
    {4}
"""
# Chain of calls:
# ===============
# menu_zaehlen.py
#     ---calls---> menu_zaehlen_ini.py
#     ---calls---> zaehlen.py
# zaehlen.py
#     ---calls---> zaehlen_ini.py
# 
# Versions of the involved programs:
# ==================================
# zaehlen.py [Program for counting the words of a text]
#     {0}, {1}
# menu_zaehlen.py [Menu for zaehlen.py]
#     {2}
# 
# Versions of the involved configuration files:
# =============================================
# menu_zaehlen_ini.py [configuration for menu_zaehlen.py]
#     {3}
# zaehlen_ini.py [configuration for zaehlen.py]
#     {4}

# --------------------------------------------------------
# Konfiguration für Labels und Felder/Checkboxen:
# do not touch
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
(E0_pre_text  + E0_text,   in_name,                "-i",  1),
(E1_pre_text  + E1_text,   separator,              "-s",  2),
(E2_pre_text  + E2_text,   stop_name,              "-S",  2),
(E3_pre_text  + E3_text,   go_name,                "-G",  2),
(E4_pre_text  + E4_text,   sort_first,             "-s1", 2),
(E5_pre_text  + E5_text,   sort_second,            "-s2", 2),
(E6_pre_text  + E6_text,   out_name,               "-o",  1),
(E7_pre_text  + E7_text,   word_template,          "-t",  2),
(E8_pre_text  + E8_text,   p_lengths,              "-l",  2),
(E9_pre_text  + E9_text,   p_rank,                 "-r",  2),
(E10_pre_text + E10_text,  p_frequency,            "-f",  2),
(C0_pre_text  + C0_text,   frequency_distribution, "-fd", 4),
(C1_pre_text  + C1_text,   length_distribution,    "-ld", 4),
(C2_pre_text  + C2_text,   separator_distribution, "-sd", 4),
(C3_pre_text  + C3_text,   character_distribution, "-cd", 4),
(C4_pre_text  + C4_text,   silent_mode,            "-sm", 4)
]

# --------------------------------------------------------
# Konfiguration für Buttons
# do not touch

button_conf = [
(B0_pre_text  + B0_text,  "ask_in_file",         0, 2),
(B1_pre_text  + B1_text,  "ask_stop_file",       2, 2),
(B2_pre_text  + B2_text,  "ask_go_file",         3, 2),
(B4_pre_text  + B4_text,  "reset_entry_fields", 18, 0),
(B5_pre_text  + B5_text,  "clear_entry_fields", 18, 1),
(B6_pre_text  + B6_text,  "start",              19, 0),
(B7_pre_text  + B7_text,  "mm.destroy",         19, 1),
(B8_pre_text  + B8_text,  "help1",              18, 2),
(B9_pre_text  + B9_text,  "help2",              19, 2),
(B10_pre_text + B10_text, "help3",              18, 3),
(B11_pre_text + B11_text, "version",            19, 3)
]

# --------------------------------------------------------
# Text für Hilfetext 1

help_text1 = programmtitle + remote_program_name + ':\n\n'
help_text1 += fields_boxes_text + "\n\n"
for f in range(len(conf)):
    help_text1 += str(conf[f][0]) + " (" + str(conf[f][1]) + "); {0} ".format(for_parameter) + conf[f][2] + "\n"

# --------------------------------------------------------
# Text für Hilfetext 2

help_text2 = buttons_text + "\n\n"
for f in range(len(button_conf)):
    help_text2 += str(button_conf[f][0]) + "; {0} '".format(calls_text) + str(button_conf[f][1]) + "'\n"

# --------------------------------------------------------
# Text für Hilfetext 3

help_text3 = comments_text

# --------------------------------------------------------
# Texte für Hilfetext "version"

version_msg_text = version_help_text.format(zaehlen_vers, zaehlen_date, menu_zaehlen_date, menu_zaehlen_ini_date, zaehlen_ini_date)

