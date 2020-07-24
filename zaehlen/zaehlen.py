#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# zaehlen.py
# Programm zum Auszählen von Textdateien
# ======================================

# History:
# 1.0.0: 2016-12-16: Anfang
# 1.1.8: 2016-12-17: erste Vollversion
# 1.2.0: 2016-12-18: filtern nach Ausgabemuster
# 1.3.0: 2016-12-18: filtern nach Wortlängen und Häufigkeiten
# 1.4.0: 2016-12-18: Steuerungsparameter interaktiv erfragen
# 1.5.0: 2016-12-18: Dateien erfragen
# 1.6.0: 2016-12-18: Mechanismus für Stop- oder Go-Dateien
# 1.7.0: 2016-12-19: zusätzliche Sortiermöglichkeiten
# 1.8.0: 2016-12-19: Ausgabe von Längen- und Häufigkeitsverteilung
# 1.9.0: 2016-12-25: Beschränkung der Ausgabe auf Rangfolgen
# 2.0.0: 2016-12-25: Programm ermöglicht jetzt auch Aufruf-Parameter
# 2.1.0: 2016-12-28: jetzt auch mit ini-Datei
# 2.2.0: 2017-01-06: interaktive Eingabe kann vorzeitig beendet werden
# 2.3.0: 2017-01-10: interaktive Eingabe vereinfacht
# 2.4.0: 2017-01-15: neu: Optionen -fd und -ld
# 2.5.0: 2017-01-26: Neu: Frequenz- und Längenverteilung auch für Ausgangstext
# 2.6.0: 2017-01-26: Fehlerkontrolle: Öffnen von Dateien
# 2.7.0: 2017-01-31: ini-Datei wird per "import" eingelesen
# 2.8.0: 2017-02-16: Pickle eingebaut
# 2.9.0: 2017-04-19: __new_extension korrigiert
# 2.10.0: 2017-06-30: neu: Trennzeichen-Verteilung
# 2.11.0: 2017-07-09: neu: Zeichen-Verteilung
# 2.12.0: 2019-12-13: in 12-7: Fehlerüberprüfungen
# 2.13.0: 2019-12-13: in 12-8, 12-9, 12-11: Fehlerüberprüfungen
# 2.13.1: 2020-07-22: erste drei Zeilen dieser Datei
# 2.13.2: 2020-07-23: Fehlermeldungen überarbeitet

# --------------------------------------------------------------
# Abhängigkeiten:

# zaehlen.py
# + ruft zaehlen_ini.py als Modul
# + wird aufgerufen in menu_zaehlen.py

# --------------------------------------------------------------
# Workflows:

# (Einlesen) alle_woerter
#            alle_woerter     (alph. Sortierung) alle_woerter2
#                                                alle_woerter2 (Sortierung) (Neuaufbau) 0sortiert
# (Einlesen) ges_alle_zeichen
#            ges_alle_zeichen (Sortierung)       sortiert5a
# (Einlesen) ges_trennzeichen
#            ges_trennzeichen (Sortierung)       sortiert4a
# .....................................................................
# 0sortiert  (2. Sortierung)  sortiert
# 0sortiert  (Neuaufbau)      ges_alle_laengen
#                             ges_alle_laengen   (Sortierung)  sortiert2a
# 0sortiert  (Neuaufbau)      ges_haeufigkeiten
#                             ges_haeufigkeiten  (Sortierung)  sortiert3a 
# .....................................................................
# sortiert   (Filterung)      (Neuaufbau)        alle_laengen
#                                                alle_laengen  (Sortierung) sortiert2
# sortiert   (Filterung)      (Neuaufbau)        alle_zeichen
#                                                alle_zeichen  (Sortierung) sortiert5
# sortiert   (Filterung)      (Neuaufbau)        haeufigkeiten
#                                                haeufigkeiten (Sortierung) sortiert3 

# --------------------------------------------------------------
# Fehlermeldungen:

# ---Warnung: zaehlen_ini.py nicht gefunden; Voreinstellungen genommen
# ---Warnung: nur "","A+", "A-", "a+", "a-" zulässig; Voreinstellung genommen
# ---Warnung; nur "","L+", "L-", "F+", "F-" zulässig;  Voreinstellung genommen
# ---Warnung: Go-Datei und Stop-Datei gleichzeitig angegeben; ignoriert
# ---Warnung: Stop-Datei <stop_name> kann nicht geöffnet werden. Ignoriert.
# ---Warnung: Go-Datei <go_name> kann nicht geöffnet werden. Ignoriert.
#
# ---Eingabedatei <in_name> kann nicht geöffnet werden. Programmabbruch
# ---Ausgabedatei <out_name> kann nicht geöffnet werden. Programmabbruch


# ==============================================================
# (1) Programm-Parameter: global

programm_name    = "zaehlen.py"
programm_vers    = "2.13.2"
programm_datum   = "2020-07-23 "
programm_autor   = "Günter Partosch"
autor_email      = "Guenter.Partosch@hrz.uni-giessen.de"
autor_institution= "Justus-Liebig-Universität Gießen, Hochschulrechenzentrum"

# globale Hilfsvariablen
leer    = " "
trenner = ":"


# ==============================================================
# (2) Module laden
# - Module argparse, re, sys, os, time, pickle werden vollständig geladen
# - aus dem Modul operator nur itemgetter
# - Suchpfad wird gesetzt; die Größen verzeichnis und interaktiv werden festgelegt
# - Zeichenkette aufruf mit Aufruf-Parameter

import argparse                 # Parser für Aufruf-Parameter 
import re                       # reguläre Ausdrücke
import sys                      # Aufruf-Parameter, System-Zugriffe
from operator import itemgetter # Sortieren nach Items 
from time import *              # Datum, Uhrzeit
import os                       # System-Aufrufe
import pickle                   # Pickle

verzeichnis = sys.path[0]
interaktiv  = (len(sys.argv) < 2)

aufruf = ""
for f in range(len(sys.argv)): aufruf += sys.argv[f] + leer

##interaktiv = (sys.argv[0] != programm_name)
##print(__name__ == "__main__")
##print("---sys.argv",sys.argv)
##print(len(sys.argv))

# ==============================================================
# (3) Parameter und Variable:
#
# Eingabedatei (Parameter --input/-i):
#   in_text    : Text für request und Auflistung
#   in_request : Ergebnis des Requests
#   in_name    : Name der Datei
#   ein        : zugehöriges Fileobjekt
# Ausgabedatei (Parameter --output/-o):
#   out_text    : Text für request und Auflistung
#   out_request : Ergebnis des Requests
#   out_name    : Name der Datei
#   aus         : zugehöriges Fileobjekt
# Go-Datei (Parameter --Go/-G):
#   go_text    : Text für request und Auflistung
#   go_request : Ergebnis des Requests
#   go_name    : Name der Datei
#   go         : zugehöriges Fileobjekt
# Stop-Datei (Parameter --Stop/-S):
#   stop_text    : Text für request und Auflistung
#   stop_request : Ergebnis des Requests
#   stop_name    : Name der Datei
#   stop         : zugehöriges Fileobjekt
# Wort-Trennzeichen (Parameter --separator/-s)
#   sep_text         : Text für request und Auflistung
#   sep_request      : Ergebnis des Requests
#   separator -->
#   p                : comp. reg. Ausdruck
# 1. Sortierung (Parameter --sort1/-s1) 
#   sort1_text       : Text für request und Auflistung
#   sort1_request    : Ergebnis des Requests
#   sort_first       : 1. Sortierschlüssel (a+/a-/A+/A-)
# 2. Sortierung (Parameter --sort2/-s2)
#   sort2_text       : Text für request und Auflistung
#   sort2_request    : Ergebnis des Requests
#   sort_second      : 2. Sortierschlüssel (L+/L-/F+/F-)
# Beschränkung auf best. Wort-Muster (Parameter --template/-t)
#   template_text    : Text für request und Auflistung
#   template_request : Ergebnis des Requests
#   word_template -->
#   p2               : comp. reg. Ausdruck
# Beschränkung auf best. Wortlängen (Parameter --lengths/-l)
#   lengths_text     : Text für request und Auflistung
#   lengths_request  : Ergebnis des Requests
#   p_lengths -->
#   re_lengths       : range
# Beschränkung auf best. Rangfolge (Parameter --ranking/-r)
#   rank_text        : Text für request und Auflistung
#   rank_request     : Ergebnis des Requests
#   p_rank -->
#   re_rank          : range
# Beschränkung auf best. Worthäufigkeiten (Parameter --frequencies/-f)
#   freq_text        : Text für request und Auflistung
#   freq_request     : Ergebnis des Requests
#   p_frequency -->
#   re_frequency     . range
# Worthäufigkeiten-Verteilung aktivieren (Parameter --frequency_distribution/-fd)
#   fd_text          : Text für request und Auflistung
#   fd_request       : Ergebnis des Requests
#   frequency_distribution
# Wortlängen-Verteilung aktivieren (Parameter --length_distribution/-ld)
#   ld_text          : Text für request und Auflistung
#   ld_request       : Ergebnis des Requests
#   length_distribution
# Trennzeichen-Verteilung aktivieren (Parameter --separator_distribution/-sd)
#   sd_text          : Text für request und Auflistung
#   sd_request       : Ergebnis des Requests
#   separator_distribution
# Zeichen-Verteilung aktivieren (Parameter --character_distribution/-cd)
#   cd_text          : Text für request und Auflistung
#   cd_request       : Ergebnis des Requests
#   character_distribution

# ==============================================================
# (4)Texte vorbesetzen
# - meist Eingabeaufforderungen

in_text       = "Eingabedatei(en) festlegen"
sep_text      = "Wort-Trennzeichen (Muster) spezifizieren"
stop_text     = "Datei mit Stop-Wörter spezifizieren"
go_text       = "Datei mit Go-Wörter spezifizieren"
sort1_text    = "1. Sortierung (a+|a-|A+|A-) spezifizieren"
sort2_text    = "2. Sortierung (L+|L-|F+|F-) spezifizieren"
out_text      = "Ausgabedatei(en) festlegen"
template_text = "Beschränkung auf best. Wort-Muster (Muster)"
lengths_text  = "Beschränkung auf best. Wortlängen"
rank_text     = "Beschränkung auf best. Rangfolge"
freq_text     = "Beschränkung auf best. Worthäufigkeiten"
version_text  = "Version des Programms ausgeben und Exit"
autor_text    = "Autor des Programms ausgeben und Exit"
text_prompt   = ": "
fd_text       = "Worthäufigkeiten-Verteilung ausgeben"
ld_text       = "Wortlängen-Verteilung ausgeben"
sd_text       = "Trennzeichen-Verteilung ausgeben"
cd_text       = "Zeichen-Verteilung ausgeben"

# ==============================================================
# (5) eigene Methoden:
# + __ueberschrif, __request, __request_text, __new_extension, __chr_hex
# + werden nur programmintern verwendet

OK = False  # wird ggf. durch __request(text) verändert
def __ueberschrift(text,z="-"):
    """dient zum Ausgeben von Überschriften bei der Ausgabe."""
    aus.write("\n" + str(text) + "\n")
    aus.write(z*len(text) + "\n\n")

def __request(text):
    """erleichtert das interaktive Eingeben von Programmparametern;
    verändert auch die globale Variable OK."""
    global OK
    variable = input(text).strip()
    if variable == "OK":
        variable = ""
        OK = True
    return variable

def __request_text(text1=leer, text2=leer):
    """bereitet den bei __request benutzten Text auf.
    Aufruf: __request_text(text1, text2)"""
    return text1.ljust(string_breite_la) + text_prompt + str(text2).ljust(string_breite_la - 8) + text_prompt

def __new_extension(name, ext):
    """versieht den Dateinamen name mit der Extension .ext."""
    p3  = re.compile("[.]") # um Extension bei Dateinamen abzutrennen
    nn  = p3.split(name)
    neu = ""
    for f in range(len(nn)-1):
        neu+=nn[f]+"."
    return neu + ext

def __chr_hex(c):
    """xx"""
    return str(hex(ord(c)))

def __chr_out(c):
    """ """
    if   (c == "\n"): www = r"\n"
    elif (c == "\r"): www = r"\r"
    elif (c == "\f"): www = r"\f"
    elif (c == "\v"): www = r"\v"
    elif (c == "\t"): www = r"\t"
    elif (c == leer):  www = "leer"
    else: www = c
    return www

# ==============================================================
# (6) Programm-Parameter
# - Voreinstellungen, Initialisierung
# - zwei Wege: Initialisierung durch Datei zaehlen-ini.py bzw. lokal im Programm

try:
    # Initialisierung für Programm-Parameter und Variablen einlesen
    from zaehlen_ini import *
except ImportError:
    # lokal Programm-Parameter und Variablen initialisieren
    print("---Warnung: zaehlen_ini.py nicht gefunden; Voreinstellungen genommen")
    in_name          = "D:/ein.txt"
    out_name         = "D:/aus.txt"
    stop_name        = ""
    go_name          = ""
    separator        = """[\s.,;:!?<>()\[\]{}"'…—–“”„‘’`+»«‹–›0-9|/=_%*$&]+"""
    word_template    = """^.+$"""
    p_lengths        = "1,100"
    p_frequency      = "1,12000"
    p_rank           = "1,50000"
    sort_first       = "a+"
    sort_second      = ""
    frequency_distribution = False
    length_distribution    = False
    separator_distribution = False
    character_distribution = False

    integer_breite   = 7  # Ausgabebreite für Integer
    integer_breite_kl= 3  # Ausgabebreite für kleine Integer
    string_breite    = 3  # voreingestellte Ausgabebreite für Strings
    string_breite_la = 43 # Länge von Eingabeaufforderungen
    real_breite      = 6  # Ausgabebreite für Reals
    rndg             = 2  # Zahl der Nachkommastellen für Reals/Floats

# optionaler Hook
try:
    ini = open("zaehlen_ini2.py", encoding="utf-8", mode="r")
    for ff in ini:
        exec(ff)
    ini.close()
except IOError:
    pass

# ==============================================================
# (7) Aufruf des Programms in der Kommandozeile mit Parametern:
# - Definition der Aufruf-Parameter
# - aktuelle Aufruf-Parameter gewinnen
# - an lokale Variablen zuweisen
#
# python zaehlen.py [-h] [-a] [-f P_FREQUENCY] [-fd] [-G GO_NAME] [-i IN_NAME]
#                   [-l P_LENGTHS] [-ld] [-o OUT_NAME] [-r P_RANK]
#                   [-s SEPARATOR] [-S STOP_NAME] [-t WORD_TEMPLATE]
#                   [-s1 {a+,a-,A+,A-}] [-s2 {L+,L-,F+,F-}] [-sd] [-cd] [-v]

# --------------------------------------------------------------
# (7-1) Definition der Aufruf-Parameter

if not interaktiv:
    # Definition der Aufruf-Parameter
    
    # benötigt werden die vorher definierten Größen:
    # autor_email, autor_institution, autor_text, fd_text, freq_text, frequency_distribution, go_name, go_text,
    # in_name, in_text, ld_text, length_distribution, lengths_text, out_name, out_text, p_frequency, p_lengths,
    # p_rank, programm_autor, programm_datum, programm_name, programm_vers, rank_text, sep_text, separator,
    # sort_first, sort_second, sort1_text, sort2_text, stop_name, stop_text, sys.stdin, sys.stdout,
    # template_text, version_text, word_template, separator_distribution, sd_text
    
    parser = argparse.ArgumentParser(description = "Auszählen eines Textes [" + programm_name + "; " +
                                     "Version: " + programm_vers + " (" + programm_datum + ")]")
    parser._positionals.title = 'Positionsparameter'
    parser._optionals.title = 'Optionale Parameter'
    opgroup = parser.add_mutually_exclusive_group() # für die beiden Optionen -G und -S (können nur alternativ verwendet werden)

    parser.add_argument("-a", "--author",
                        help = autor_text,
                        action = 'version',
                        version = programm_autor + " (" + autor_email + ", " + autor_institution + ")") 
    parser.add_argument("-cd", "--character_distribution",
                        help = cd_text + "; Voreinstellung: " + "%(default)s",
                        action = "store_true",
                        default = character_distribution) 
    parser.add_argument("-f", "--frequencies",
                        help = freq_text + "; Voreinstellung: " + "%(default)s",
                        dest = "p_frequency",
                        default = p_frequency) 
    parser.add_argument("-fd", "--frequency_distribution",
                        help = fd_text + "; Voreinstellung: " + "%(default)s",
                        action = "store_true",
                        default = frequency_distribution)
    opgroup.add_argument("-G", "--Go",
                         help = go_text + "; Voreinstellung: " + "%(default)s",
                         dest = "go_name",
                         default = go_name) 
    parser.add_argument("-i", "--input",
                        help = in_text + "; Voreinstellung: " + "%(default)s",
                        type=argparse.FileType(mode = 'r', encoding = "utf-8"),
                        dest = "in_name",
                        default = sys.stdin) 
    parser.add_argument("-l", "--lengths",
                        help = lengths_text + "; Voreinstellung: " + "%(default)s",
                        dest = "p_lengths",
                        default = p_lengths) 
    parser.add_argument("-ld", "--length_distribution",
                        help    = ld_text + "; Voreinstellung: " + "%(default)s",
                        action  = "store_true",
                        default = length_distribution) 
    parser.add_argument("-o", "--output",
                        help    = out_text + "; Voreinstellung: " + "%(default)s",
                        type    = argparse.FileType(mode = 'w', encoding = "utf-8"),
                        dest    = "out_name",
                        default = sys.stdout) 
    parser.add_argument("-r", "--ranking",
                        help = rank_text + "; Voreinstellung: " + "%(default)s",
                        dest = "p_rank",
                        default = p_rank) 
    parser.add_argument("-s", "--separator",
                        help = sep_text + "; Voreinstellung: " + "%(default)s",
                        dest = "separator",
                        default = separator)
    opgroup.add_argument("-S", "--Stop",
                         help = stop_text + "; Voreinstellung: " + "%(default)s",
                         dest = "stop_name",
                         default = stop_name) 
    parser.add_argument("-s1", "--sort1",
                        help = sort1_text + "; Voreinstellung: " + "%(default)s",
                        choices = ["a+", "a-", "A+", "A-"],
                        dest = "sort_first",
                        default = sort_first) 
    parser.add_argument("-s2", "--sort2",
                        help = sort2_text + "; Voreinstellung: " + "%(default)s",
                        choices = ["L+", "L-", "F+", "F-"],
                        dest = "sort_second",
                        default = sort_second) 
    parser.add_argument("-sd", "--separator_distribution",
                        help = sd_text + "; Voreinstellung: " + "%(default)s",
                        action = "store_true",
                        default = separator_distribution) 
    parser.add_argument("-t", "--template",
                        help = template_text + "; Voreinstellung: " + "%(default)s",
                        dest = "word_template",
                        default = word_template) 
    parser.add_argument("-v", "--version",
                        help = version_text,
                        action = 'version',
                        version = '%(prog)s ' + programm_vers + " (" + programm_datum + ")") 

# --------------------------------------------------------------
# (7-2) aktuelle Aufruf-Parameter gewinnen

    args  =  parser.parse_args() # Aufruf-Parameter

# --------------------------------------------------------------
# (7-3) an lokale Variablen zuweisen

    ein           = args.in_name
    in_name       = args.in_name.name
    out_name      = args.out_name.name
    aus           = args.out_name
    stop_name     = args.stop_name
    go_name       = args.go_name
    separator     = args.separator
    word_template = args.word_template
    p_lengths     = args.p_lengths
    p_frequency   = args.p_frequency
    p_rank        = args.p_rank
    sort_first    = args.sort_first
    sort_second   = args.sort_second
    frequency_distribution = args.frequency_distribution
    length_distribution    = args.length_distribution
    separator_distribution = args.separator_distribution
    character_distribution = args.character_distribution

# ==============================================================
# (8) Interaktiver Aufruf des Programms bzw. mit der Python-Flag -i

if interaktiv or (sys.flags.interactive):

    # Abfrage-Variablen vorbesetzen
    in_request       = ""
    sep_request      = ""
    stop_request     = ""
    go_request       = ""
    sort1_request    = ""
    sort2_request    = ""
    out_request      = ""
    template_request = ""
    lengths_request  = ""
    rank_request     = ""
    freq_request     = ""
    fd_request       = ""
    ld_request       = ""
    sd_request       = ""
    cd_request       = ""

    # Parameter interaktiv erfragen
    print("Programm " + programm_name + " zum Zählen von Wörtern in einer Datei\n")
    print("Voreingestellte bzw. übergebene bzw. neue Werte:\n")
    print("""Werte neu setzen:
    <return> bisherigen Wert übernehmen
    OK       weitere Eingabe beenden und Programm starten
    sonst    neuer Wert
    <strg D> Programm-Abbruch
    """)
    
    print("Aufgabe".ljust(string_breite_la) + text_prompt + "bisheriger Wert".ljust(string_breite_la - 8) +
          text_prompt + "neuer Wert".ljust(string_breite_la))
    print("-" * (2 * string_breite_la + 3 * 2))
    if not OK: in_request       = __request(__request_text(in_text, in_name))
    if not OK: sep_request      = __request(__request_text(sep_text, separator))
    if not OK: stop_request     = __request(__request_text(stop_text, stop_name))
    if not OK: go_request       = __request(__request_text(go_text, go_name))

    if not OK: sort1_request    = __request(__request_text(sort1_text, sort_first))
    if not (sort1_request in ["","A+", "A-", "a+", "a-"]):
        print('---Warnung: nur "","A+", "A-", "a+", "a-" zulässig; Voreinstellung genommen')
        sort1_request = ""
    if not OK: sort2_request    = __request(__request_text(sort2_text, sort_second))
    if not (sort2_request in ["","L+", "L-", "F+", "F-"]):
        print('---Warnung; nur "","L+", "L-", "F+", "F-" zulässig;  Voreinstellung genommen')
        sort1_request = ""
        
    if not OK: out_request      = __request(__request_text(out_text, out_name))
    if not OK: template_request = __request(__request_text(template_text, word_template))
    if not OK: lengths_request  = __request(__request_text(lengths_text, p_lengths))
    if not OK: rank_request     = __request(__request_text(rank_text, p_rank))
    if not OK: freq_request     = __request(__request_text(freq_text, p_frequency))
    if not OK: fd_request       = __request(__request_text(fd_text, frequency_distribution))
    if not OK: ld_request       = __request(__request_text(ld_text, length_distribution))
    if not OK: sd_request       = __request(__request_text(sd_text, separator_distribution))
    if not OK: cd_request       = __request(__request_text(cd_text, character_distribution))

    # überprüfen, ob Parameter interaktiv neu gesetzt wurden
    if (in_request != ""):       in_name = in_request
    if (out_request != ""):      out_name = out_request
    if (stop_request != ""):     stop_name = stop_request
    if (go_request != ""):       go_name = go_request
    if (sep_request != ""):      separator = sep_request
    if (template_request != ""): word_template = template_request
    if (lengths_request != ""):  p_lengths = lengths_request
    if (freq_request != ""):     p_frequency = freq_request
    if (rank_request != ""):     p_rank = rank_request
    if (sort1_request != ""):    sort_first = sort1_request
    if (sort2_request != ""):    sort_second = sort2_request
    if (fd_request != ""):       frequency_distribution = fd_request
    if (ld_request != ""):       length_distribution = ld_request
    if (sd_request != ""):       separator_distribution = sd_request
    if (cd_request != ""):       character_distribution = cd_request

    # Eingabe-/Ausgabedatei im Interaktiv-Modus öffnen
    
    try:
        ein = open(in_name, encoding='utf-8', mode='r')   # Eingabedatei
    except IOError:
        sys.stderr("---Eingabedatei " + in_name, " kann nicht geöffnet werden. Programmabbruch")
        exit()
        
    try:
        aus = open(out_name, encoding='utf-8', mode='w+') # Ausgabedatei
    except IOError:
        sys.stderr("---Ausgabedatei " + out_name + " kann nicht geöffnet werden. Programmabbruch")
        exit()

    # prüfen, ob Go-Datei und Stop-Datei gleichzeitig angegeben sind
    
    if (stop_name != "") and (go_name != ""):
        print("---Warnung: Go-Datei und Stop-Datei gleichzeitig angegeben; ignoriert")
        stop_name = ""
        go_name = ""

# ==============================================================
# (9) Programm-Parameter:
# (9-1) Dateien: Stop-Datei bzw. Go-Datei

if (stop_name != ""):
    try:
        stop = open(stop_name, encoding='utf-8', mode='r')# Stop-Datei
    except IOError:
        print("---Warnung: Stop-Datei", stop_name, "kann nicht geöffnet werden. Ignoriert.")
        stop_name = ""
        
if (go_name != ""):
    try:
        go = open(go_name, encoding='utf-8', mode='r')    # Go-Datei
    except IOError:
        print("---Warnung: Go-Datei", go_name, "kann nicht geöffnet werden. Ignoriert.")
        go_name = ""

# --------------------------------------------------------------
# (9-2) Programm-Parameter:
# reguläre Ausdrücke

p                = re.compile(separator)                      # für Wort-Trennzeichen
p2               = re.compile(word_template)                  # für Ausgabe-Muster

# --------------------------------------------------------------
# (9-3) Programm-Parameter:
# Wortlängen, Häufigkeiten und Rangfolge

re_lengths       = eval("range(" + str(p_lengths) + ")")      # range-Ausdruck für Wortlängen
re_frequency     = eval("range(" + str(p_frequency) + ")")    # range-Ausdruck für Wortfrequenzen
re_rank          = eval("range(" + str(p_rank) + ")")         # range-Ausdruck für Rangfolge

# --------------------------------------------------------------
# (9-4) Programm-Parameter:
# Datum und Uhrzeit

lt               = localtime()
jahr,monat,tag   = lt[0:3]
stunde,minute    = lt[3:5]
datum            = "%04i-%02i-%02i" % (jahr,monat,tag)
uhrzeit          = "%02i:%02i" % (stunde,minute)

# ==============================================================
# (10) Initialisieren
# - Zähler/Zeichenketten initialisieren
# - Dictionaries initialisieren
# - Stop- und Go-Datei initialisieren

z_zeilen          = 0  # Zähler für Eingabezeilen
z_ausgabezeile    = 0  # Zähler für Ausgabezeilen
summe_roh_zeichen = 0  # Summe der insgesamt eingelesenen Zeichen
summe_zeichen     = 0  # Summe der verarbeiteten Zeichen
summe_woerter     = 0  # Summe der verarbeiteten Wörter
akk_anz           = 0  # Summe der ausgegebenen Wörter
auswahl_tokens    = 0  # Summe der ausgegebenen Tokens
auswahl_types     = 0  # Summe der ausgegebenen Types

alle_woerter      = {} # Dictionary für die beim Einlesen gewonnenen Wörter
alle_stop_woerter = {} # Dictionary für die optional eingelesenen Stop-Wörter
alle_go_woerter   = {} # Dictionary für die optional eingelesenen Go-Wörter

haeufigkeiten     = {} # Dictionary für die Verteilung der Wort-Häufigkeiten (in der Auswahl nach Filterung)
ges_haeufigkeiten = {} # Dictionary für die Verteilung der Wort-Häufigkeiten (im Gesamttext)

alle_laengen      = {} # Dictionary für die Verteilung der Wort-Längen (in der Auswahl nach Filterung)
ges_alle_laengen  = {} # Dictionary für die Verteilung der Wort-Längen (im Gesamttext)

ges_trennzeichen  = {} # Dictionary für die Verteilung der Trennzeichen-Häufigkeiten (im Gesamttext)

ges_alle_zeichen  = {} # Dictionary für die Verteilung der Zeichen-Häufigkeiten (im Gesamttext)
alle_zeichen      = {} # Dictionary für die Verteilung der Zeichen-Häufigkeiten (in der Auswahl nach Filterung)

# --------------------------------------------------------------
# Stop-Datei einlesen und in Dictionary alle_stop_woerter abspeichern

if (stop_name != ""):
    for line in stop:
        eine_zeile = line.rstrip()
        alle_stop_woerter[eine_zeile] = 1
    stop.close()

# --------------------------------------------------------------
# Go-Datei einlesen und in Dictionary alle_go_woerter abspeichern

if (go_name != ""):
    for line in go:
        eine_zeile = line.rstrip()
        alle_go_woerter[eine_zeile] = 1
    go.close()

# ==============================================================
# (11) eigentliche Arbeitsschleife;
# (11-1) zeilenweises Einlesen der Eingabedatei

for line in ein:
    # ein              : Fileobjekt (Eingabedatei)
    # line             : Hilfsvariable; eine Rohzeile
    # woerter_zeile    : Hilfsvariable; die Wörter der Zeile
    # w                : Hilfsvariable; ein Wort
    # ww               : Hilfsvariable; ein Trennzeichen
    # f                : ein "normales" Zeichen
    # www              : Hilfsvariable; ein modifiziertes Trennzeichen 
    # tz_zeile         : Hilfsvariable; Trennzeichen der aktuellen Zeile
    # alle_woerter     : zum Sammeln der Wörter
    # ges_trennzeichen : zum Sammeln der Trennzeichen
    # z_zeilen         : Zähler für Zeilen
    # summe_roh_zeichen: Zähler für Roh-Zeichen
    # summe_woerter    : Zähler für Wörter
    # summe_zeichen    : Zähler für Zeichen
    
    z_zeilen          += 1
    woerter_zeile      = []
    summe_roh_zeichen += len(line)
    tz_zeile           = p.findall(line)

    for w in tz_zeile:
        for www in w:

            if not(www in ges_trennzeichen):
                ges_trennzeichen[www]  = 1
            else:
                ges_trennzeichen[www] += 1
    
    eine_zeile         = line.rstrip()
    woerter_zeile      = p.split(line)
    for w in woerter_zeile:
        if w != "":
            summe_woerter += 1
            summe_zeichen += len(w)
            if len(w) > string_breite:
                string_breite = len(w)
            if w in alle_woerter:
                alle_woerter[w] += 1
            else:
                alle_woerter[w] = 1
            for f in w:
                if f in ges_alle_zeichen:
                    ges_alle_zeichen[f] += 1
                else:
                    ges_alle_zeichen[f] = 1

# --------------------------------------------------------------
# (11-2) 1. Sortierung
#
# alle_woerter  : gesammelte Wörter
# alle_woerter2 : sortierte Wörter
# sort_first    : global; Kriterium für 1. Sortierung; verschiedene Varianten:
#                 a+ : alphabetisch, Groß/Klein-Schreibung einsortiert; aufsteigend
#                 a- : alphabetisch, Groß/Klein-Schreibung einsortiert; absteigend
#                 A+ : alphabetisch, Groß/Klein-Schreibung nicht einsortiert; aufsteigend
#                 A- : alphabetisch, Groß/Klein-Schreibung nicht einsortiert; absteigend
#                 andere Angaben: wie a+

if (sort_first == "a+"):
    alle_woerter2 = sorted(alle_woerter, key=str.lower, reverse=False)
elif (sort_first == "a-"):
    alle_woerter2 = sorted(alle_woerter, key=str.lower, reverse=True)
elif (sort_first == "A+"):
    alle_woerter2 = sorted(alle_woerter, reverse=False)
elif (sort_first == "A-"):
    alle_woerter2 = sorted(alle_woerter, reverse=True)
else:
    alle_woerter2 = sorted(alle_woerter, key=str.lower, reverse=False)

# --------------------------------------------------------------
# (11-3) Aufbau einer Liste mit Zeichenkette, Anzahl und Länge (für den Gesamttext)
#
# alle_woerter  : gesammelte Wörter
# alle_woerter2 : sortierte Wörter
# sortiert      : daraus sortierte Liste mit Zeichenkette, Anzahl und Länge
#                 [(wort, anzahl, länge), ...]

sortiert = []
for z in range(len(alle_woerter2)):
    ww = alle_woerter2[z]
    sortiert += [(ww, alle_woerter[ww], len(ww))]

# --------------------------------------------------------------
# (11-4) Aufbau von Frequenz- und Häufigkeitsverteilung (für den Gesamttext)
#
# sortiert          : sortierte Liste aller Wörter (für den Gesamttext)
# ges_haeufigkeiten : zum Sammeln der Häufigkeiten
# ges_alle_laengen  : zum Sammeln der Längen
# w                 : Hilfsgröße; steht für ein Wort
# anz               : dafür Anzahl
# laenge            : dafür Länge

for w in range(len(sortiert)):
    anz = sortiert[w][1]
    laenge = sortiert[w][2]
    # Häufigkeiten sammeln
    if anz in ges_haeufigkeiten: 
        ges_haeufigkeiten[anz] += 1
    else:
        ges_haeufigkeiten[anz] = 1

    # Längen sammeln
    if laenge in ges_alle_laengen: 
        ges_alle_laengen[laenge] += 1
    else:
        ges_alle_laengen[laenge] = 1

# --------------------------------------------------------------
# (11-4) 2. Sortierung
#
# sortiert    : sortierte Liste mit Zeichenkette, Anzahl und Länge; wird ggf. neu sortiert
# sort_second : global; Kriterium für 2. Sortierung, verschiedene Varianten:
#               L+ : sortiert nach Länge; aufsteigend
#               L- : sortiert nach Länge; absteigend
#               F+ : sortiert nach Worthäufigkeit; aufsteigend
#               F- : sortiert nach Worthäufigkeit; absteigend
#               andere Angaben: ignoriert (keine 2. Sortierung)

if (sort_second == "L+"):
    sortiert = sorted(sortiert, key=itemgetter(2), reverse=False)
elif (sort_second == "L-"):
    sortiert = sorted(sortiert, key=itemgetter(2), reverse=True)
elif (sort_second == "F+"):
    sortiert = sorted(sortiert, key=itemgetter(1), reverse=False)
elif (sort_second == "F-"):
    sortiert = sorted(sortiert, key=itemgetter(1), reverse=True)
else:
    pass

# ==============================================================
# (12) Ausgabe
# (12-1) Ausgabeformate vorbereiten

ps0 = "{0:" + str(integer_breite) +  "} "
ps1 = "{0:" + str(integer_breite_kl) + "} "
ps2 = "{0:" + str(string_breite) +  "} "
ps3 = "{0:" + str(integer_breite) +  "} "
ps4 = "{0:" + str(real_breite) +  "." + str(rndg) + "f} "
ps5 = ps3
ps6 = ps4

# --------------------------------------------------------------
# (12-2) Ausgabe
# Kopf allgemein
breite = 21

__ueberschrift("Text auszählen","=")
aus.write("Name des Programms   : " + programm_name + "\n")
aus.write("Version des Programms: " + programm_vers + "\n")
aus.write("Bearbeitungsdatum    : " + programm_datum + "\n")
aus.write("Autor des Programms  : " + programm_autor + "\n")
aus.write("E-Mail-Adresse       : " + autor_email + "\n")
aus.write("Institution          : " + autor_institution + "\n\n")

# --------------------------------------------------------------
# (12-3) Kopf
# Ausgabe Programm-Parameter

__ueberschrift("Programm-Parameter","-")
aus.write("Programm-Aufruf                        : " + aufruf + "\n")
aus.write("Eingabedatei                           : " + in_name + "\n")
aus.write("Wort-Trennzeichen (Muster)             : " + separator + "\n")
aus.write("Datei mit Stop-Wörter                  : " + stop_name + "\n")
aus.write("Datei mit Go-Wörter                    : " + go_name + "\n")
aus.write("1. Sortierung (a+|a-|A+|A-)            : " + sort_first + "\n")
aus.write("2. Sortierung (L+|L-|F+|F-)            : " + sort_second + "\n")
aus.write("Ausgabe-Datei                          : " + out_name + "\n")
aus.write("Beschränkung auf best. Wort-Muster     : " + word_template + "\n")
aus.write("Beschränkung auf best. Wortlängen      : [" + p_lengths + ")\n")
aus.write("Beschränkung auf best. Rangfolge       : [" + p_rank + ")\n")
aus.write("Beschränkung auf best. Worthäufigkeiten: [" + p_frequency + ")\n")
aus.write("Worthäufigkeiten-Verteilung aktiviert  : " + str(frequency_distribution) + "\n")
aus.write("Wortlängen-Verteilung aktiviert        : " + str(length_distribution) + "\n")
aus.write("Trennzeichen-Verteilung aktiviert      : " + str(separator_distribution) + "\n")
aus.write("Zeichen-Verteilung aktiviert           : " + str(character_distribution) + "\n")
aus.write("\n")

# --------------------------------------------------------------
# (12-4) Ausgabe
# Kopf der eigentlichen Tabelle

__ueberschrift("Ergebnisse (Wörter in der Auswahl)","-")
aus.write("(" + datum + ", " + uhrzeit + ")\n\n")

aus.write("(1) Rangfolge\n")
aus.write("(2) Länge der Zeichenkette\n")
aus.write("(3) Zeichenkette\n")
aus.write("(4) abs. Häufigkeit\n")
aus.write("(5) proz. Häufigkeit [%]\n")
aus.write("(6) akk. Häufigkeit\n")
aus.write("(7) proz. akk. Häufigkeit [%]\n\n")

aus.write("(1)".rjust(integer_breite))
aus.write("(2)".rjust(integer_breite_kl + 1))
aus.write("(3)".ljust(string_breite + 1))
aus.write("(4)".rjust(integer_breite + 1))
aus.write("(5)".rjust(real_breite + 1))
aus.write("(6)".rjust(integer_breite + 1))
aus.write("(7)".rjust(real_breite + 1))
aus.write("\n")
aus.write(">")
aus.write("-" *(integer_breite_kl + string_breite + 3 * integer_breite + 2 * real_breite + 5) + "\n")

# --------------------------------------------------------------
# (12-5) Ausgabe
# eigentliche Tabelle

for w in range(len(sortiert)):
    # sortiert       : sortierte Wortliste
    # w              : Hilfsvariable; ein Listenelement
    # laenge         : Hilfsvariable; Länge
    # zkette         : Hilfsvariable; Inhalt
    # anz            : Hilfsvariable; Häufigkeit
    # z_ausgabezeile : Zähler für Ausgabezeile (vor Filterung)
    
    laenge = sortiert[w][2]
    zkette = sortiert[w][0]
    anz    = sortiert[w][1]
    z_ausgabezeile += 1

    # Bedingungen für b_stop und b_go setzen
    if stop_name != "":
        b_stop = not (zkette in alle_stop_woerter)
    else:
        b_stop = True
    
    if go_name != "":
        b_go = (zkette in alle_go_woerter)
    else:
        b_go = True
        
    # Bedingungen überprüfen (Filter)
    # + b_stop      : in Stop-Datei?
    # + b_go        : in Go-Datei?
    # + p2          : zulässiges Ausgabemuster
    # + re_frequency: zulässige Häufigkeit
    # + re_lengths  : zulässige Länge
    # + re_rank     : zulässiger Rang
    
    beding = p2.match(zkette) and (anz in re_frequency) and (laenge in re_lengths) and b_stop and b_go and (z_ausgabezeile in re_rank)
    
    # Ausgabe, Schleife
    if beding:
        # akk_anz        : bis dahin akkumulierte Häufigkeit
        # summe_woerter  : Anzahl der eingelesenen Wörter
        # proz_anz       : Proz. Anteil von anz an summe_woerter
        # proz_akk_anz   : Proz. Anteil von akk_anz an summe_woerter
        # auswahl_tokens : Anzahl der Tokens in der Auswahl
        # auswahl_types  : Anzahl der Types in der Auswahl
        # haeufigkeiten  : gesammelte Häufigkeiten
        # alle_laengen   : gesammelte Längen
        # alle_zeichen   : gesammelte Zeichen
        # f              : ein Zeichen
        
        # Summen und Prozente
        akk_anz        += anz
        proz_anz        = float(anz / summe_woerter) * 100.00
        proz_akk_anz    = float(akk_anz / summe_woerter) * 100.00
        auswahl_tokens += anz
        auswahl_types  += 1
        
        if anz in haeufigkeiten: # Häufigkeiten sammeln
            haeufigkeiten[anz] += 1
        else:
            haeufigkeiten[anz] = 1

        if laenge in alle_laengen: # Längen sammeln
            alle_laengen[laenge] += 1
        else:
            alle_laengen[laenge] = 1

        for f in zkette:
            if f in alle_zeichen:
                alle_zeichen[f] += anz
            else:
                alle_zeichen[f] = anz
                    
        # Ausgabe, eine Zeile
        aus.write((ps0).format(z_ausgabezeile))
        aus.write((ps1).format(laenge))
        aus.write((ps2).format(zkette))
        aus.write((ps3).format(anz))
        aus.write((ps4).format(round(proz_anz, rndg)))
        aus.write((ps5).format(akk_anz))
        aus.write((ps6).format(round(proz_akk_anz, rndg)))
        aus.write("\n")

# --------------------------------------------------------------
# (12-6) Ausgabe
# Summe, Abspann

alle_types = len(alle_woerter)

aus.write("<")
aus.write("-" *(integer_breite_kl + string_breite + 3*integer_breite + 2*real_breite + 5) + "\n")
aus.write((ps0).format(leer))
aus.write((ps1).format(leer))
aus.write((ps2).format("Summe"))
aus.write((ps3).format(auswahl_tokens))
aus.write((ps4).format(round(auswahl_tokens/summe_woerter * 100.00, rndg)))
aus.write("\n\n")

# --------------------------------------------------------------
# (12-7) Ausgabe
# Zusammenfassung

__ueberschrift("Ergebnisse (Zusammenfassung der Auswahl)", "-")
##if (summe_roh_zeichen == 0) or (summe_woerter  == 0) or (alle_types  == 0) or (auswahl_tokens == 0):
##    sys.stderr("---Division durch Null: Programmabbruch")   
##    exit()
aus.write(("Zeilen                          : " + ps3 + "\n\n").format(z_zeilen))
aus.write(("Zeichen, insgesamt              : " + ps3 + "\n").format(summe_roh_zeichen))
aus.write(("Zeichen, berücksichtigt         : " + ps3).format(summe_zeichen))
if (summe_roh_zeichen > 0):
    aus.write((" (entspricht " + ps6 + "%)\n\n").format(round(summe_zeichen/summe_roh_zeichen * 100.00, rndg)))
aus.write(("Wörter (Tokens), Gesamttext     : " + ps3 + "\n").format(summe_woerter))
aus.write(("Wörter (Tokens), Auswahl        : " + ps3).format(auswahl_tokens))
if (summe_woerter  > 0):
    aus.write((" (entspricht " + ps6 + "%)\n\n").format(round(auswahl_tokens/summe_woerter * 100.00, rndg)))
aus.write(("Wörter (Types), Gesamttext      : " + ps3 + "\n").format(alle_types))
aus.write(("Wörter (Types), Auswahl         : " + ps3).format(auswahl_types))
if (alle_types  > 0):
    aus.write((" (entspricht " + ps6 + "%)\n\n").format(round(auswahl_types/alle_types * 100.00, rndg)))
aus.write(("Verh. (Types/Tokens), Gesamttext: " + ps6 + "%\n").format(round(alle_types/summe_woerter * 100.0, rndg)))
if (auswahl_tokens > 0):
    aus.write(("Verh. (Types/Tokens), Auswahl   : " + ps6 + "%\n\n").format(round(auswahl_types/auswahl_tokens * 100.0, rndg)))

# --------------------------------------------------------------
# (12-8) Ausgabe
# Längenverteilung
#
# length_distribution : Schalter
# alle_laengen    : gesammelte Längen (in der Auswahl)
# ges_alle_laengen: gesammelte Längen (im Gesamttext)
# sortiert2       : sortierte Längen (in der Auswahl)
# sortiert2a      : sortierte Längen (im Gesamttext)
# s               : lokal; Summe
# maximum         : lokal; größte Länge
# f               : lokal; Schleifenindex
# max_f           : lokal; Index dazu
# auswahl_types   : global; Anzahl der Types in der Auswahl
# alle_types      : global; Anzahl der Types im Gesamttext
# zs              : lokal; aktuelle Länge der Ausgabezeile
# maxzs           : lokal; maximale Länge der Ausgabezeile
# kopfzs          : lokal; Kopf der Ausgabezeile
# breite          : lokal; Breite des Labels bei der Ausgabe

sortiert2a = sorted(ges_alle_laengen)
sortiert2  = sorted(alle_laengen)

if length_distribution:

    breite = 34  
    maxzs  = 120
    kopfzs = "\n" + 17 * leer
    
    __ueberschrift("Ergebnisse (Verteilung der Wortlängen im Gesamttext)","-")

    s       = 0
    maximum = 0
    max_f   = 0
    zs      = 0
    aus.write("<länge>:<anzahl>")
    aus.write(kopfzs)
    for f in sortiert2a:
        s += f * ges_alle_laengen[f]
        if ges_alle_laengen[f] > maximum: maximum = ges_alle_laengen[f]; max_f = f
        zwi = str(f) + trenner + str(ges_alle_laengen[f]) + "  "
        zs += len(zwi)
        if zs >= maxzs: aus.write(kopfzs); zs = 0
        aus.write(zwi)
    aus.write("\n\n")
    aus.write("minimale Länge:".ljust(breite) + str(min(ges_alle_laengen)) + "\n")
    aus.write("maximale Länge:".ljust(breite) + str(max(ges_alle_laengen)) + "\n")
    aus.write("Modus der Längenverteilung:".ljust(breite) + str(max_f) + " mit " + str(ges_alle_laengen[max_f]) + " Vorkommen\n")
    aus.write("Durchschnittliche Länge:".ljust(breite) + str(round(s / alle_types, rndg)) + "\n")
    aus.write("\n")

    __ueberschrift("Ergebnisse (Verteilung der Wortlängen nach dem Filtern)","-")

    s       = 0
    maximum = 0
    max_f   = 0
    zs      = 0

    if len(alle_laengen) > 0:
        aus.write("<länge>:<anzahl>")
        aus.write(kopfzs)
        for f in sortiert2:
            s += f * alle_laengen[f]
            if alle_laengen[f] > maximum: maximum = alle_laengen[f]; max_f = f
            zwi = str(f) + trenner + str(alle_laengen[f]) + "  "
            zs += len(zwi)
            if zs >= maxzs: aus.write(kopfzs); zs = 0
            aus.write(zwi)
        aus.write("\n\n")
        aus.write("minimale Länge:".ljust(breite) + str(min(alle_laengen)) + "\n")
        aus.write("maximale Länge:".ljust(breite) + str(max(alle_laengen)) + "\n")
        aus.write("Modus der Längenverteilung:".ljust(breite) + str(max_f) + " mit " + str(alle_laengen[max_f]) + " Vorkommen\n")
        aus.write("Durchschnittliche Länge:".ljust(breite) + str(round(s / auswahl_types, rndg)) + "\n")
        aus.write("\n")
    else:
        aus.write("Verteilung der Wortlängen nach dem Filtern nicht verfügbar\n")

# --------------------------------------------------------------
# (12-9) Ausgabe
# Häufigkeitsverteilung
#
# frequency_distribution : Schalter
# haeufigkeiten    : gesammelte Häufigkeiten (in der Auswahl)
# ges_haeufigkeiten: gesammelte Häufigkeiten (im Gesamttext)
# sortiert3        : sortierte Häufigkeiten (in der Auswahl)
# sortiert3a       : sortierte Häufigkeiten (im Gesamttext)
# s                : lokal; Summe
# maximum          : lokal; größte Häufigkeit
# f                : lokal; Schleifenindex
# max_f            : lokal; Index dazu
# auswahl_types    : global; Anzahl der Types in der Auswahl
# alle_types       : global; Anzahl der Types im Gesamttext
# zs               : lokal; aktuelle Länge der Ausgabezeile
# maxzs            : lokal; maximale Länge der Ausgabezeile
# kopfzs           : lokal; Kopf der Ausgabezeile
# breite           : lokal; Breite des Labels bei der Ausgabe

sortiert3  = sorted(haeufigkeiten)
sortiert3a = sorted(ges_haeufigkeiten)

if frequency_distribution:

    breite = 34  
    maxzs  = 120
    kopfzs = "\n" + 17 * leer
   
    __ueberschrift("Ergebnisse (Verteilung der Worthäufigkeiten im Gesamttext)","-")
    
    s       = 0
    maximum = 0
    max_f   = 0
    zs      = 0  

    if len(ges_haeufigkeiten) > 0:
        aus.write("<häufigkeit>:<anzahl>")
        aus.write(kopfzs)
        for f in sortiert3a:
            s += f * ges_haeufigkeiten[f]
            if ges_haeufigkeiten[f] > maximum: maximum = ges_haeufigkeiten[f]; max_f = f
            zwi = str(f) + trenner + str(ges_haeufigkeiten[f]) + "  "
            zs += len(zwi)
            if zs >= maxzs:
                aus.write(kopfzs); zs = 0
            aus.write(zwi)
        aus.write("\n\n")
        aus.write("minimale Häufigkeit:".ljust(breite) + str(min(ges_haeufigkeiten)) + "\n")
        aus.write("maximale Häufigkeit:".ljust(breite) + str(max(ges_haeufigkeiten)) + "\n")
        aus.write("Modus der Häufigkeitenverteilung:".ljust(breite) + str(max_f) + " mit " + str(ges_haeufigkeiten[max_f]) + " Vorkommen\n")
        aus.write("\n")
    else:
        aus.write("Verteilung der Worthäufigkeiten im Gesamttext nicht verfügbar\n")

    __ueberschrift("Ergebnisse (Verteilung der Worthäufigkeiten nach dem Filtern)","-")

    s       = 0
    maximum = 0
    max_f   = 0
    zs      = 0

    if len(haeufigkeiten) > 0:
        aus.write("<häufigkeit>:<anzahl>")
        aus.write(kopfzs)
        for f in sortiert3:
            s += f * haeufigkeiten[f]
            if haeufigkeiten[f] > maximum: maximum = haeufigkeiten[f]; max_f = f
            zwi = str(f) + trenner + str(haeufigkeiten[f]) + "  "
            zs += len(zwi)
            if zs >= maxzs: aus.write(kopfzs); zs = 0
            aus.write(zwi)
        aus.write("\n\n")
        aus.write("minimale Häufigkeit:".ljust(breite) + str(min(haeufigkeiten)) + "\n")
        aus.write("maximale Häufigkeit:".ljust(breite) + str(max(haeufigkeiten)) + "\n")
        aus.write("Modus der Häufigkeitenverteilung:".ljust(breite) + str(max_f) + " mit " + str(haeufigkeiten[max_f]) + " Vorkommen\n")
        aus.write("\n")
    else:
        aus.write("Verteilung der Worthäufigkeiten nach dem Filtern nicht verfügbar\n")

# --------------------------------------------------------------
# (12-10) Ausgabe
# Trennzeichenverteilung
#
# separator_distribution : Schalter
# ges_trennzeichen : gesammelte Trennzeichenhäufigkeiten (im Gesamttext)
# sortiert4a       : sortierte Trennzeichenhäufigkeiten (im Gesamttext)
# s                : lokal; Summe
# maximum          : lokal; größte Häufigkeit
# max_f            : lokal; Index dazu
# f                : lokal; Schleifenindex; ein einzelnes Trennzeichen
# ff               : lokal; Schleifenindex; ein einzelnes transformiertes Trennzeichen
# zs               : lokal; aktuelle Länge der Ausgabezeile
# maxzs            : lokal; maximale Länge der Ausgabezeile
# kopfzs           : lokal; Kopf der Ausgabezeile
# breite           : lokal; Breite des Labels bei der Ausgabe

sortiert4a = sorted(ges_trennzeichen)

if separator_distribution:

    breite = 34  
    maxzs  = 120
    kopfzs = "\n" + 17 * leer
    
    __ueberschrift("Ergebnisse (Verteilung der Trennzeichenhäufigkeiten im Gesamttext)", "-")
    
    s       = 0
    maximum = 0
    max_f   = 0
    zs      = 0
    aus.write("<trennzeichen>:<anzahl>")
    aus.write(kopfzs)
    for f in sortiert4a:
        s += ges_trennzeichen[f]
        if ges_trennzeichen[f] > maximum:
            maximum = ges_trennzeichen[f]; max_f = f
        zwi = __chr_out(f) + trenner + __chr_hex(f) + trenner + str(ges_trennzeichen[f]) + 2 * leer
        zs += len(zwi)
        if zs >= maxzs:
            aus.write(kopfzs); zs = 0
        aus.write(zwi)
    aus.write("\n\n")
    aus.write("Modus der Trennzeichenverteilung:".ljust(breite) + "'" + __chr_out(max_f) + "' mit " + str(ges_trennzeichen[max_f]) + " Vorkommen\n")
    aus.write("\n")

# --------------------------------------------------------------
# (12-11) Ausgabe
# Zeichenverteilung
#
# character_distribution  : Schalter
# alle_zeichen     : gesammelte Zeichenhäufigkeiten (in der Auswahl)
# ges_alle_zeichen : gesammelte Zeichenhäufigkeiten (im Gesamttext)
# sortiert5        : sortierte Zeichenhäufigkeiten (in der Auswahl)
# sortiert5a       : sortierte Zeichenhäufigkeiten (im Gesamttext)
# s                : lokal; Summe
# maximum          : lokal; größte Häufigkeit
# f                : lokal; Schleifenindex
# max_f            : lokal; Index dazu
# auswahl_types    : global; Anzahl der Types in der Auswahl
# alle_types       : global; Anzahl der Types im Gesamttext
# zs               : lokal; aktuelle Länge der Ausgabezeile
# maxzs            : lokal; maximale Länge der Ausgabezeile
# kopfzs           : lokal; Kopf der Ausgabezeile
# breite           : lokal; Breite des Labels bei der Ausgabe

sortiert5a = sorted(ges_alle_zeichen)
sortiert5  = sorted(alle_zeichen)

if character_distribution:

    breite = 34  
    maxzs  = 120
    kopfzs = "\n" + 17 * leer

    __ueberschrift("Ergebnisse (Verteilung der Zeichenhäufigkeiten im Gesamttext)","-")

    s       = 0
    maximum = 0
    max_f   = 0
    zs      = 0

    aus.write("<zeichen>:<code>:<anzahl>")
    aus.write(kopfzs)
    for f in sortiert5a:
        s += ges_alle_zeichen[f]
        if ges_alle_zeichen[f] > maximum:
            maximum = ges_alle_zeichen[f]; max_f = f
        zwi = str(f) + trenner + __chr_hex(f) + trenner + str(ges_alle_zeichen[f]) + 2 * leer
        zs += len(zwi)
        if zs >= maxzs:
            aus.write(kopfzs); zs = 0
        aus.write(zwi)
    aus.write("\n\n")
    aus.write("Modus der Zeichenverteilung:".ljust(breite) + "'" + str(max_f) + "' mit " + str(ges_alle_zeichen[max_f]) + " Vorkommen\n")
    aus.write("\n")

    __ueberschrift("Ergebnisse (Verteilung der Zeichenhäufigkeiten nach dem Filtern)","-")

    s       = 0
    maximum = 0
    max_f   = 0
    zs      = 0

    if len(sortiert5) > 0:
        aus.write("<zeichen>:<code>:<anzahl>")
        aus.write(kopfzs)
        for f in sortiert5:
            s += alle_zeichen[f]
            if alle_zeichen[f] > maximum:
                maximum = alle_zeichen[f]; max_f = f
            zwi = str(f) + trenner + __chr_hex(f) + trenner + str(alle_zeichen[f]) + 2 * leer
            zs += len(zwi)
            if zs >= maxzs:
                aus.write(kopfzs); zs = 0
            aus.write(zwi)
        aus.write("\n\n")
        aus.write("Modus der Zeichenverteilung:".ljust(breite) + "'" + str(max_f) + "' mit " + str(alle_zeichen[max_f]) + " Vorkommen\n")
        aus.write("\n")
    else:
        aus.write("Verteilung der Zeichenhäufigkeiten nach dem Filtern nicht verfügbar\n")


# ==============================================================
# (13) Pickle
# - Name der Pickle-Datei wird gewonnen
# - Pickle-Datei wird zum binären Schreiben göffnet
# - Objekt, das mit Pickle ausgelagert werden soll, wird erzeugt
# - Pickle-Datei wird geschrieben
# - Pickle-Datei wird geschlossen

pickle_name = __new_extension(out_name, "pkl")
pickle_file = open(pickle_name,"bw")
kopf = (verzeichnis, programm_name, programm_vers, programm_datum, programm_autor, autor_email, autor_institution, in_name)
programmdaten = (aufruf, in_name, separator, stop_name, go_name, sort_first, sort_second, out_name, word_template,
                p_lengths, p_rank, p_frequency)
pickle_daten = (kopf, programmdaten, sortiert, ges_alle_zeichen, ges_trennzeichen, ges_haeufigkeiten, ges_alle_laengen)
pickle.dump(pickle_daten, pickle_file)
pickle_file.close()

# ==============================================================
# (14) Dateien schließen
# Ein- und Ausgabedatei werden geschlossen

ein.close()
aus.close()
