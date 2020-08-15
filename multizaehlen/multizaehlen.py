#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# multizaehlen.py

# (C) Günter Partosch 2017-2020

# Programm zum Auswerten der Auszählungen von Textdateien
# =======================================================
# Pickle-Daten werden ausgewertet und zusammengefasst

# noch
# + auch sonst Variablen aufführen

# History:
# 1.0.0: 2017-02-17: Anfang
# 1.1.0: 2017-02-17: erstmals funktionsfähig
# 1.2.0: 2017-02-18: Filterung (-r, -l, -t, -f) aktiviert
# 1.3.0: 2017-02-18: Sortierung funktioniert
# 1.4.0: 2017-02-18: Fehlerabprüfung beim Öffnen von Dateien
# 1.5.0: 2017-02-19: Filterung nach Zahl der Dateien
# 1.6.0: 2017-02-19: ini-Datei per import
# 1.7.0: 2017-02-19: -fd / -ld
# 1.8.0: 2017-07-10: -sd / -cd angefangen
# 1.9.0: 2017-07-17: neues Konzept für -d, -ld, -cd, -sd
# 1.10.0: 2017-07-19: Berechnung von Modus und Summen für -d, -ld, -cd, -sd

# 1.10.9: 2020-08-02: Voreinstellungen geändert
# 1.11.0: 2020-08-15: Ausgabe-Strings

# --------------------------------------------------------------
# Fehlermeldungen

# ---Ausgabedatei <out_name> kann nicht geöffnet werden. Programmabbruch!
# ---Datei <datei> kann nicht geöffnet werden. Programmabbruch!
# ---Datei <datei> ist vom falschen Typ: Programmabbruch!
# ---Strukturen der vorherigen Ergebnisdateien sind nicht kompatibel. Programmabbruch!

# --------------------------------------------------------------
# Programmabfolge

# (1) Programm-Parameter: global
# (2) Module laden:
# (3) eigene Methoden:
# (4) Strukturen vorbesetzen und initialisieren:
# (5) Variablen vorbesetzen:
# (6) Programm-Parameter:
#     (6-1) Programm-Parameter: Datum und Uhrzeit
#     (6-2) Programm-Parameter: Aufruf
#     (6-3) Definition und Beschreibung der Aufrufparameter:
#     (6-4) Programm-Parameter: reguläre Ausdrücke
#     (6-5) Programm-Parameter: Filterung
# (7) Ausgabedatei öffnen:
# (8) Daten wiedergewinnen:
#     (8-1) prüfen, ob die gewonnenen Daten kompatibel sind: ggf. Abbruch
# (9) Strukturen vereinigen zu einer neuen Struktur:
# (10) 1. Sortierung:
# (11) daraus Aufbau einer Liste mit Zeichenkette, Anzahl und Länge (für den Gesamttext):
# (12) 2. Sortierung:
# (13) Ausgabe
#      (13-1) Ausgabe vorbereiten:
#      (13-2) Ausgabe, Kopf, allgemein:
#      (13-3) Ausgabe, Kopf, Ausgabe Programm-Parameter:
#      (13-4) Ausgabe, Legende:
#      (13-5) Ausgabe, Kopfzeile:
#      (13-6) Ausgabe, eigentliche Ausgabe:
#      (13-7) Ausgabe, Zusammenfassung
#      (13-8) Ausgabe, ld ausgeben (Längen-Verteilung):
#      (13-9) Ausgabe, fd ausgeben (Häufigkeitsverteilung):
#      (13-10) Ausgabe, cd ausgeben (Zeichen-Verteilung):
#      (13-11) Ausgabe, sd ausgeben (Trennzeichen-Verteilung):
# (14) Ausgabe schließen

    
# ==============================================================
# (1) Programm-Parameter: global

# in ini-Datei verschoben

##prg_name_text     = "multizaehlen.py"
##prg_vers_text     = "1.10.9"
##prg_date_text    = "2020-08-02"
##prg_author_text    = "Günter Partosch"
##author_email_text  = "Guenter.Partosch@hrz.uni-giessen.de"
##author_institution = "Justus-Liebig-Universität Gießen, Hochschulrechenzentrum"


# ==============================================================
# (2) Module laden:

import pickle                   # Pickle ermöglichen
import sys                      # Aufruf-Parameter, System-Zugriffe
from operator import itemgetter # Sortieren nach Items
import argparse                 # Defintion und Verarbeitung von Aufrufparameter
import re                       # reguläre Ausdrücke
from time import *              # Datum, Uhrzeit
import math                     # math. Funktionen


# ==============================================================
# (3) eigene Methoden:

# -----------------------------------------------------
def __ueberschrift(text,z="-"):
    """dient zum Ausgeben von Überschriften bei der Ausgabe."""
    aus.write("\n" + str(text) + "\n")
    aus.write(z*len(text) + "\n\n")

# -----------------------------------------------------
def __chr_hex(c):
    """dient zur Ausgabe eines Zeichens im Hex-Code."""
    return str(hex(ord(c)))

# -----------------------------------------------------
def __chr_out(c):
    """dient zur Ausgabe eines beliebigen Zeichens."""
    # www: lokale Hilfsvariable
    if (c == "\n"):
        www = r"\n"
    elif (c == "\r"):
        www = r"\r"
    elif (c == "\f"):
        www = r"\f"
    elif (c == "\v"):
        www = r"\v"
    elif (c == "\t"):
        www = r"\t"
    elif (c == leer):
        www = "leer"
    else:
        www = c
    return www


# ==============================================================
# (4) Strukturen vorbesetzen und initialisieren:

P                  = [] # Filehandles aller pkl-Dateien
P_load             = [] # alle Daten aller pkl-Dateien
P_kopf             = [] # Kopfdaten aus allen pkl-Dateien
P_programmdaten    = [] # Programmdaten aller pkl-Dateien
P_sortiert         = [] # Ergebnisdaten (aus sortiert) aus allen pkl-Dateien
P_ges_alle_zeichen = [] # Ergebnisdaten (aus ges_alle_zeichen) aus allen pkl-Dateien
P_ges_trennzeichen = [] # Ergebnisdaten (aus ges_trennzeichen) aus allen pkl-Dateien
P_ges_haeufigkeiten= [] # Ergebnisdaten (aus ges_haeufigkeiten) aus allen pkl-Dateien
P_ges_alle_laengen = [] # Ergebnisdaten (aus ges_alle_laengen) aus allen pkl-Dateien

neu                = {} # Directory zum Sammeln der Ergebnisdaten (sortiert)
neu3               = [] # nach Sortierung und Umstrukturierung

akk_anz            = 0  # akk. Anzahl (über alle Dateien)
akk_anz_vor        = 0  # akk. Anzahl (über alle Dateien; vor Filterung) [=akk_anz]
akk_anz_nach       = 0  # ; nach Filterung
anz_dat            = [] # Anzahl für die verschiedenen Dateien
fd_vor             = {} # Directory für Häufigkeitsverteilung vor Filterung 
fd_nach            = {} # Directory für Häufigkeitsverteilung nach Filterung
ld_vor             = {} # Directory für Längenverteilung vor Filterung
ld_nach            = {} # Directory für Längenverteilung nach Filterung
cd_vor             = {} # Directory für Zeichenverteilung vor Filterung
cd_nach            = {} # Directory für Zeichenverteilung nach Filterung
sd_vor             = {} # Directory für Trennzeichenverteilung vor Filterung


# ==============================================================
# (5) Variablen vorbesetzen:

# + Import von multizaehlen_ini.py
# + falls nicht erfolgreich: lokale Spezifikationen

# Texte für Programmparameter: autor_text, cd_text, fd_text, files_anz_text, files_text, freq_text, ld_text, lengths_text,
#                              out_text, rank_text, sd_text, sort1_text, sort2_text, template_text, version_text
# Pogrammparameter: character_distribution, frequency_distribution, in_name, length_distribution, out_name, p_files, p_frequency,
#                   p_lengths, p_rank, separator_distribution, sort_first, sort_second, word_template
# Hilfsvariable: leer, trenner
# Kurznamen für math. Funktionen: floor, lg

try:
    # Konfiguration/Initialisierung von multizaehlen.py einlesen
    from multizaehlen_ini import * 
except ImportError:
    # falls Fehler: lokal Programm-Parameter und -Variablen initialisieren
    sys.stderr.write(warn_no_ini)

    files_text    = "zu verarbeitende Dateien (*.plk)"
    files_anz_text= "Beschränkung der Zahl von Dateien (*.plk) mit Zeichenkette"
    sort1_text    = "1. Sortierung [a+|a-|A+|A-]"
    sort2_text    = "2. Sortierung [L+|L-|F+|F-|D+|D-]"
    out_text      = "Ausgabedatei"
    template_text = "Beschränkung auf best. Wort-Muster (Muster)"
    lengths_text  = "Beschränkung auf best. Wortlängen"
    rank_text     = "Beschränkung auf best. Rangfolge"
    freq_text     = "Beschränkung auf best. Worthäufigkeiten"
    version_text  = "Version des Programms ausgeben"
    autor_text    = "Autor des Programms ausgeben"
    fd_text       = "Worthäufigkeiten-Verteilung berechnen"
    ld_text       = "Wortlängen-Verteilung berechnen"
    sd_text       = "Trennzeichen-Verteilung berechnen"
    cd_text       = "Zeichen-Verteilung berechnen"

    in_name       = ""
    out_name      = "./out.txt"
    word_template = """^.+$"""
    p_lengths     = "1,100"
    p_files       = "1,20"
    p_frequency   = "1,20000"
    p_rank        = "1,60000"
    
    sort_first    = "a+"
    sort_second   = ""
    frequency_distribution = False
    length_distribution    = False
    separator_distribution = False
    character_distribution = False
    rndg          = 3

lg      = math.log10 # Logarithmus zur Basis 10
floor   = math.floor # Abrunden zur nächsten Integer
leer    = " "
trenner = ":"


# ==============================================================
# (6) Programm-Parameter:
# + Datum und Uhrzeit
# + Aufruf
# + Aufrufparameter
# + Programm-Parameter: reguläre Ausdrücke
# + Programm-Parameter: Filterung

# --------------------------------------------------------------
# (6-1) Programm-Parameter: Datum und Uhrzeit

# lt      : Hilfsvariable
# jahr    : Hilfsvariable: wird bei der Ausgabe verwendet
# monat   : Hilfsvariable: wird bei der Ausgabe verwendet
# tag     : Hilfsvariable: wird bei der Ausgabe verwendet
# stunde  : Hilfsvariable: wird bei der Ausgabe verwendet
# minute  : Hilfsvariable: wird bei der Ausgabe verwendet
# uhrzeit : Hilfsvariable: wird bei der Ausgabe verwendet

lt             = localtime()
jahr,monat,tag = lt[0:3]
stunde,minute  = lt[3:5]
datum          = "%04i-%02i-%02i" % (jahr,monat,tag)
uhrzeit        = "%02i:%02i" % (stunde,minute)

# --------------------------------------------------------------
# (6-2) Programm-Parameter: Aufruf

aufruf = ""
for f in range(len(sys.argv)):
    aufruf += sys.argv[f] + leer

# --------------------------------------------------------------
# (6-3) Definition und Beschreibung der Aufrufparameter:

# Aufruf:
# multizaehlen.py [-h] [-a] [-v] [-f P_FREQUENCY] [-fd] [-fi P_FILES]
#                 [-l P_LENGTHS] [-ld] [-o OUT_NAME] [-r P_RANK]
#                 [-s1 {a+,a-,A+,A-}] [-s2 {L+,L-,F+,F-,D+,D-}]
#                 [-t WORD_TEMPLATE]
#                 files [files ...]
# Schlüsselwort-Parameter: -a/--author, -v/--version, -f/--frequencies, -fd/frequency_distribution, -l/--lengths,
#                          -ld/--length_distribution, -o/--output, -r/--ranking, -s/--sort1, -s2/--sort2,
#                          -t/--template -fi/--files
# andere Parameter: <files>

parser = argparse.ArgumentParser(description = main_caption_text + " [" + prg_name_text + "; " +
                                 "Version: " + prg_vers_text + " (" + prg_date_text + ")]")
parser._positionals.title = argp_pos_par
parser._optionals.title   = argp_opt_par

parser.add_argument('files', nargs ='+',
                    help = files_text)
parser.add_argument("-a", "--author",
                    help    = autor_text,
                    action  = 'version',
                    version = prg_author_text + " (" + author_email_text + ")") 
parser.add_argument("-cd", "--character_distribution",
                    help    = cd_text + "; {0}: %(default)s".format(argp_default),
                    action  = "store_true",
                    default = character_distribution) 
parser.add_argument("-f", "--frequencies",
                    help    = freq_text + "; {0}: %(default)s".format(argp_default),
                    dest    = "p_frequency",
                    default = p_frequency) 
parser.add_argument("-fd", "--frequency_distribution",
                    help    = fd_text + "; {0}: %(default)s".format(argp_default),
                    action  = "store_true",
                    default = frequency_distribution) 
parser.add_argument("-fi", "--files",
                    help    = files_anz_text + "; {0}: %(default)s".format(argp_default),
                    dest    = "p_files",
                    default = p_files) 
parser.add_argument("-l", "--lengths",
                    help    = lengths_text + "; {0}: %(default)s".format(argp_default),
                    dest    = "p_lengths",
                    default = p_lengths) 
parser.add_argument("-ld", "--length_distribution",
                    help    = ld_text + "; {0}: %(default)s".format(argp_default),
                    action  = "store_true",
                    default = length_distribution) 
parser.add_argument("-o", "--output",
                    help    = out_text + "; {0}: %(default)s".format(argp_default),
                    type    = argparse.FileType(mode = 'w', encoding = "utf-8"),
                    dest    = "out_name",
##                    default = sys.stdout) 
                    default = out_name) 
parser.add_argument("-r", "--ranking",
                    help    = rank_text + "; {0}: %(default)s".format(argp_default),
                    dest    = "p_rank",
                    default = p_rank) 
parser.add_argument("-s1", "--sort1",
                    help    = sort1_text + "; {0}: %(default)s".format(argp_default),
                    choices = ["a+", "a-", "A+", "A-"],
                    dest    = "sort_first",
                    default = sort_first) 
parser.add_argument("-s2", "--sort2",
                    help    = sort2_text + "; {0}: %(default)s".format(argp_default),
                    choices = ["L+", "L-", "F+", "F-", "D+", "D-"],
                    dest    = "sort_second",
                    default = sort_second) 
parser.add_argument("-sd", "--separator_distribution",
                    help    = sd_text + "; {0}: %(default)s".format(argp_default),
                    action  = "store_true",
                    default = separator_distribution) 
parser.add_argument("-t", "--template",
                    help    = template_text + "; {0}: %(default)s".format(argp_default),
                    dest    = "word_template",
                    default = word_template) 
parser.add_argument("-v", "--version",
                    help    = version_text,
                    action  = 'version',
                    version = '%(prog)s '+ prg_vers_text + " (" + prg_date_text + ")") 

args  =  parser.parse_args()

# --------------------------------------------------------------
# Zuweisung an lokale Variablen
alle                   = args.files
aus                    = args.out_name
out_name               = args.out_name.name
word_template          = args.word_template
p_lengths              = args.p_lengths
p_frequency            = args.p_frequency
p_rank                 = args.p_rank
sort_first             = args.sort_first
sort_second            = args.sort_second
frequency_distribution = args.frequency_distribution
length_distribution    = args.length_distribution
character_distribution = args.character_distribution
separator_distribution = args.separator_distribution
p_files                = args.p_files

len_alle               = len(alle)
if (len_alle == 0):
    sys.stderr.write(err_no_files)
    exit()

# --------------------------------------------------------------
# (6-4) Programm-Parameter: reguläre Ausdrücke
#
# word_template : aus Aufruf: Wortausgabemuster
# p2            : compilierter regulärer Ausdruck: wird beim Filtern verwendet

p2 = re.compile(word_template) # für Ausgabe-Muster

# --------------------------------------------------------------
# (6-5) Programm-Parameter: Filterung
# Anzahl der Dateien, Wortlängen, Häufigkeiten und Rangfolge
#
# p_lengths    : aus Aufruf: Wortlängen
# p_frequency  : aus Aufruf: Worthäufigkeiten
# p_rank       : aus Aufruf: Rangfolge
# p_files      : aus Aufruf: Anzahl der Dateien
# re_lengths   : p_lengths ausgewertet: wird beim Filtern verwendet
# re_frequency : p_frequency ausgewertet: wird beim Filtern verwendet
# re_rank      : p_rank ausgewertet: wird beim Filtern verwendet
# re_files     : p_files ausgewertet: wird beim Filtern verwendet

re_lengths    = eval("range(" + str(p_lengths) + ")")   # range-Ausdruck für Wortlängen
re_frequency  = eval("range(" + str(p_frequency) + ")") # range-Ausdruck für Wortfrequenzen
re_rank       = eval("range(" + str(p_rank) + ")")      # range-Ausdruck für Rangfolge
re_files      = eval("range(" + str(p_files) + ")")     # range-Ausdruck für Anzahl der Dateien


# ==============================================================
# (7) Ausgabedatei öffnen:

# out_name : Ausgabedatei
# aus      : Filehandle

try:
    aus = open(out_name, encoding='utf-8', mode='w+')  # Ausgabedatei
except IOError:                                        # wenn Ausgabedatei nicht geöffnet werden kann
    sys.stderr.write(err_out.format(out_name))
    exit()


# ==============================================================
# (8) Daten wiedergewinnen:

# loads = (kopf, programmdaten, sortiert, ges_alle_zeichen, ges_trennzeichen)
#
# sortiert
# [(zkette, anzahl, länge), ...]
#
# kopf = (verzeichnis, prg_name_text, prg_vers_text, prg_date_text, prg_author_text, author_email_text, author_institution, in_name)
#
# programmdaten = (aufruf, in_name, separator, stop_name, go_name, sort_first, sort_second, out_name, word_template,
#                  p_lengths, p_rank, p_frequency
#
# f                  : Hilfsvariable: Schleifenvariable
# len_alle           : Anzahl der pkl-Dateien
# P[i]               : File-Handels aller pkl-Dateien
# P_load[i]          : alle Daten aller pkl-Dateien
# P_kopf[i]          : Kopfdaten aus aller pkl-Dateien
# P_programmdaten[i] : Programmdaten aller pkl-Dateien
# P_sortiert[i]      : Ergebnisdaten aller pkl-Dateien

# --------------------------------------------------------------
# Schleife: alle angeforderten pkl-Dateien öffnen
# ggf. Programmabbruch
for f in range(len_alle):
    try:
        file = open(alle[f], "br")
    except IOError:                # falls eine pkl-Datei nicht geöffnet werden kann
        sys.stderr.write(err_pkl_open.format(alle[f]))
        exit()
   
    if not (".pkl" in alle[f]):    # ggf. Programmabbruch, wenn falscher Typ        
        sys.stderr.write(err_type.format(alle[f]))
        exit()

# --------------------------------------------------------------
    # Daten der pkl-Dateien wiedergewinnen
    P.append(file)                                # Filehandles aller pkl-Dateien werden in der Liste P abgelegt
    loads = pickle.load(P[f])                     # die Daten aller pkl-Dateien werden in der Liste loads abgelegt
    P_load.append(loads)                          # loads wird in der Liste P_load abgelegt
    kopf, programmdaten, sortiert, ges_alle_zeichen, ges_trennzeichen, ges_haeufigkeiten, ges_alle_laengen = loads
    P_kopf.append(kopf)                           # kopf wird in der Liste P_kopf abgelegt
    P_programmdaten.append(programmdaten)         # programmdaten wird in der Liste P_programmdaten abgelegt
    P_sortiert.append(sortiert)                   # sortiert wird in der Liste P_sortiert abgelegt
    P_ges_alle_zeichen.append(ges_alle_zeichen)   # ges_alle_zeichen wird in der Liste P_ges_alle_zeichen abgelegt
    P_ges_trennzeichen.append(ges_trennzeichen)   # ges_trennzeichen wird in der Liste P_ges_trennzeichen abgelegt
    P_ges_haeufigkeiten.append(ges_haeufigkeiten) # ges_haeufigkeiten wird in der Liste P_ges_haeufigkeiten abgelegt
    P_ges_alle_laengen.append(ges_alle_laengen)   # ges_alle_laengen wird in der Liste P_ges_alle_laengen abgelegt

# --------------------------------------------------------------
# (8-1) prüfen, ob die gewonnenen Daten kompatibel sind:
#       ggf. Abbruch
# 
# P_kopf          : zu überprüfende Kopfdaten aus allen pkl-Dateien
# P_programmdaten : zu überprüfende Programmdaten aus allen pkl-Dateien
# aus 1.ff pkl-Datei (Kopf-Daten)   : x_prg_date_text, x_prg_name_text, x_prg_vers_text
# aus 1.ff pkl-Datei (Programmdaten): x_go_name, x_separator, x_stop_name
# f               : Schleifenvariable
# len_alle        : Anzahl der pkl-Dateien
# kompatibel      : True, wenn die betreffenden Daten der einzelnen pkl-Dateien kompatibel sind

kompatibel       = True

# --------------------------------------------------------------
# Programmkopf
x_prg_name_text  = P_kopf[0][1]
x_prg_vers_text  = P_kopf[0][2]
x_prg_date_text = P_kopf[0][3]

# --------------------------------------------------------------
# wichtige Programmdaten
x_separator      = P_programmdaten[0][2]
x_stop_name      = P_programmdaten[0][3]
x_go_name        = P_programmdaten[0][4]

# --------------------------------------------------------------
# Schleife über alle Köpfe und Programmdaten
for f in range(1, len_alle):
    if (P_kopf[f][1] != x_prg_name_text): kompatibel = False
    if (P_kopf[f][2] != x_prg_vers_text): kompatibel = False
    if (P_kopf[f][3] != x_prg_date_text): kompatibel = False

    if (P_programmdaten[f][2] != x_separator): kompatibel = False
    if (P_programmdaten[f][3] != x_stop_name): kompatibel = False
    if (P_programmdaten[f][4] != x_go_name): kompatibel = False

if not kompatibel:
    sys.stderr.write(err_compatib)
    exit()


# ==============================================================
# (9) Strukturen vereinigen zu einer neuen Struktur:

# P_sortiert : Ergebnisstruktur eines zaehlen-Aufrufs
# neu        : neue Struktur: enthält für jedes Wort die Daten aus allen pkl-Dateien
#              laenge - akk. Zahl über alle Dateien - Anzahl der Dateien - Anzahl in Dat1 - Anzahl in Dat2 - ...
# ergebnis   : Hilfsstruktur: ein Eintrag in neu
# len_alle   : Anzahl der pkl-Dateien
# f          : Schleifenvariable: über alle pkl-Dateien  
# g          : Schleifenvariable: über alle Wörter einer pkl-Datei
# l3         : Hilfsvariable
# zkette     : Hilfsvariable
# anzahl     : Hilfsvariable
# laenge     : Hilfsvariable
# alle       : Liste mit allen Namen
# ll         : jeweils Anzahl der Wörter in einer pkl-Datei

l3 = len_alle + 3

for f in range(len_alle):
    ll   = len(P_sortiert[f])
    for g in range(ll):
        zkette, anzahl, laenge = P_sortiert[f][g]
        if not(zkette in neu):
            ergebnis        = [0 for x in range(l3)]
            ergebnis[0]     = laenge
            ergebnis[f + 3] = anzahl
            ergebnis[1]     = anzahl
            ergebnis[2]     = 1
            neu[zkette]     = ergebnis
        else:
            neu[zkette][f+3] = anzahl
            neu[zkette][1]  += anzahl
            neu[zkette][2]  += 1


# ==============================================================
# (10) 1. Sortierung:

# neu        : gesammelte Einträge
# neu2       : sortierte Wörter
# sort_first : global; Kriterium für 1. Sortierung; verschiedene Varianten:
#              a+ : alphabetisch, Groß/Klein-Schreibung einsortiert; aufsteigend
#              a- : alphabetisch, Groß/Klein-Schreibung einsortiert; absteigend
#              A+ : alphabetisch, Groß/Klein-Schreibung nicht einsortiert; aufsteigend
#              A- : alphabetisch, Groß/Klein-Schreibung nicht einsortiert; absteigend
#              andere Angaben: wie a+

if (sort_first == "a+"):
    neu2 = sorted(neu, key=str.lower, reverse=False)
elif (sort_first == "a-"):
    neu2 = sorted(neu, key=str.lower, reverse=True)
elif (sort_first == "A+"):
    neu2 = sorted(neu, reverse=False)
elif (sort_first == "A-"):
    neu2 = sorted(neu, reverse=True)
else:
    neu2 = sorted(neu, key=str.lower, reverse=False)


# ==============================================================
# (11) daraus Aufbau einer Liste mit Zeichenkette, Anzahl und Länge (für den Gesamttext):

# neu2      : sortierte Liste
# neu3      : neu aufgebaute Liste
#             Index 0: Zeichenkette (ein Wort)
#             Index 1: Länge dieser Zeichenkette
#             Index 2: Anzahl der Zeichenkette in den n Dateien
#             Index 3: in wieviel Dateien
#             Index 4ff : Anzahl der Zeichenkette in den einzelnen Dateien
# maxlaenge : Hilfsvariable: max. Länge aller Zeichenketten
# maxzahl   : Hilfsvariable: max. Anzahl aller Zeichenketten
# z         : Hilfsvariable: Schleifenvariable
# ww        : Hilfsvariable
# zwi       : Hilfsvariable

maxlaenge = 0
maxzahl   = 0

for z in range(len(neu2)):
    ww   = neu2[z]
    zwi  = [ww]
    zwi += neu[ww]
    if len(zwi[0]) > maxlaenge:
        maxlaenge = len(zwi[0])
    if zwi[2] > maxzahl:
        maxzahl = zwi[2]
    neu3 += [tuple(zwi)]


# ==============================================================
# (12) 2. Sortierung:

# neu3        : sortierte Liste mit Zeichenkette, Anzahl und Länge; ggf. neu sortiert
# sort_second : global; Kriterium für 2. Sortierung, verschiedene Varianten:
#               L+ : sortiert nach Länge; aufsteigend
#               L- : sortiert nach Länge; absteigend
#               F+ : sortiert nach Worthäufigkeit; aufsteigend
#               F- : sortiert nach Worthäufigkeit; absteigend
#               L+ : sortiert nach Anzahl der Dateien; aufsteigend
#               L- : sortiert nach Anzahl der Dateien; absteigend
#               andere Angaben: ignoriert (==> keine 2. Sortierung)

if (sort_second == "L+"):
    neu3 = sorted(neu3, key=itemgetter(1), reverse=False)
elif (sort_second == "L-"):
    neu3 = sorted(neu3, key=itemgetter(1), reverse=True)
elif (sort_second == "F+"):
    neu3 = sorted(neu3, key=itemgetter(2), reverse=False)
elif (sort_second == "F-"):
    neu3 = sorted(neu3, key=itemgetter(2), reverse=True)
elif (sort_second == "D+"):
    neu3 = sorted(neu3, key=itemgetter(3), reverse=False)
elif (sort_second == "D-"):
    neu3 = sorted(neu3, key=itemgetter(3), reverse=True)
else:
    pass


# ==============================================================
# (13) Ausgabe
#
# --------------------------------------------------------------
# (13-1) Ausgabe vorbereiten:

# vorbereitet werden: die Breiten i1, i2, z3, i4, i5, i6, i7

i1 = floor(lg(len(neu3))) + 1 # Breite der Kolumne 1 (laufende Nummer); adaptierbar <-- len(neu3)
i2 = 2                        # Breite der Kolumne 2 (Zeichenkettenlänge)
z3 = maxlaenge                # Breite der Kolumne 3 (Zeichenkette); adaptierbar <-- maxlaenge
i4 = floor(lg(maxzahl)) + 2   # Breite der Kolumne 4 (Summenzahl über alle Dateien); adaptierbar
i5 = i4                       # Breite der Kolumne 5 (akk. Summenzahl über alle Dateien); adaptierbar
i6 = 2                        # Breite der Kolumne 6 (Zahl der Dateien); adaptierbar
i7 = i4                       # Breite der Kolumne 7 (Anzahl); adaptierbar <-- maxzahl

##ps1 = "{0:" + str(i1) + "} "
##ps2 = "{0:" + str(i2) + "} "
##ps3 = "{0:" + str(z3) + "} "
##ps4 = "{0:" + str(i4 + 1) + "} "
##ps5 = "{0:" + str(i5) + "} "
##ps6 = "{0:" + str(i6) + "} "
##ps7 = "{0:" + str(i7) + "} "

# --------------------------------------------------------------
# (13-2) Ausgabe, Kopf, allgemein:

# b                : Breite des Labels
# ausgegeben werden: author_email_text, author_institution, prg_author_text, prg_date_text, prg_name_text, prg_vers_text

__ueberschrift(main_caption_text,"=")
b = 43

aus.write(head_prg_name.ljust(b) + trenner + leer + prg_name_text + "\n")
aus.write(head_prg_vers.ljust(b) + trenner + leer + prg_vers_text + "\n")
aus.write(head_prg_date.ljust(b) + trenner + leer + prg_date_text + "\n")
aus.write(prg_author.ljust(b)    + trenner + leer + prg_author_text + "\n")
aus.write(author_email.ljust(b)  + trenner + leer + author_email_text + "\n")
aus.write(author_inst.ljust(b)   + trenner + leer + author_institution + "\n\n")

__ueberschrift(head_content,"-")

aus.write("+ {0}".format(head_prg_para) + "\n")
aus.write("+ {0}".format(head_result) + "\n")
aus.write("+ {0}".format(head_summary) + "\n")
if length_distribution:    aus.write("+ {0}".format(res_pre_ld) + "\n")
if frequency_distribution: aus.write("+ {0}".format(res_pre_fd) + "\n")
if character_distribution: aus.write("+ {0}".format(res_pre_cd) + "\n")
if separator_distribution: aus.write("+ {0}".format(res_pre_sd) + "\n")
aus.write("\n")

# --------------------------------------------------------------
# (13-3) Ausgabe, Kopf, Ausgabe Programm-Parameter:

# b                : Breite des Labels
# aufruf           : katueller Aufruf mit Parametern
# Labels           : fd_text, files_anz_text, freq_text, ld_text, lengths_text, out_text, rank_text, sort1_text, sort2_text,
#                    template_text
# ausgegeben werden: frequency_distribution, length_distribution, out_name, p_files, p_frequency, p_lengths, p_rank, sort_first,
#                    sort_second, word_template

__ueberschrift(sub_caption,"-")
b = 57

aus.write(prg_call.ljust(b)          + trenner + leer + aufruf + "\n")
aus.write(sort1_text.ljust(b)        + trenner + leer + sort_first + "\n")
aus.write(sort2_text.ljust(b)        + trenner + leer + sort_second + "\n")
aus.write(out_text.ljust(b)          + trenner + leer + out_name + "\n")
aus.write(template_text.ljust(b)     + trenner + leer + word_template + "\n")
aus.write(lengths_text.ljust(b)      + trenner + leer + "[" + p_lengths + ")\n")
aus.write(rank_text.ljust(b)         + trenner + leer + "[" + p_rank + ")\n")
aus.write(freq_text.ljust(b)         + trenner + leer + "[" + p_frequency + ")\n")
aus.write(files_anz_text.ljust(b)    + trenner + leer + "[" + p_files + ")\n")
aus.write(fd_text.ljust(b)           + trenner + leer + str(frequency_distribution) + "\n")
aus.write(ld_text.ljust(b)           + trenner + leer + str(length_distribution) + "\n")
aus.write(sd_text.ljust(b)           + trenner + leer + str(separator_distribution) + "\n")
aus.write(cd_text.ljust(b)           + trenner + leer + str(character_distribution) + "\n")
aus.write("\n")

# --------------------------------------------------------------
# (13-4) Ausgabe, Legende:
#
# datum    : global: Datum
# uhrzeit  : global: Uhrzeit
# i        : lokale Schleifenvariable
# len_alle : Anzahl der pkl-Dateien
# alle     : Liste mit den Namen der pkl-Dateien
# p_kopf   : Liste mit Kopfdaten: hier Namen der ursprünglichen Dateien 

__ueberschrift(caption_leg,"-")

aus.write("(" + datum + ", " + uhrzeit + ")\n\n")

aus.write("(1) {0}".format(leg_rank) + "\n")
aus.write("(2) {0}".format(leg_str_len) + "\n")
aus.write("(3) {0}".format(leg_string) + "\n")
aus.write("(4) {0}".format(leg_str_freq) + "\n")
aus.write("(5) {0}".format(leg_acc_freq) + "\n")
aus.write("(6) {0}".format(leg_file_nr) + "\n")
for i in range(len_alle):
    aus.write("({0}) {1} {2} ({3} -->\n    {4})".format(str(i + 7), leg_in_file, str(i), alle[i], P_kopf[i][7]) + "\n")
aus.write("\n")

# --------------------------------------------------------------
# (13-5) Ausgabe, Kopfzeile:

# benutzt werden: i1, i2, z3, i4, i5, i6, i7
# len_alle      : Anzahl der pkl-Dateien

aus.write("(1)".rjust(i1))
aus.write("(2)".rjust(i2))
aus.write("(3)".ljust(z3 + 2))
aus.write("(4)".rjust(i4 + 1))
aus.write("(5)".rjust(i5 + 1))
aus.write("(6)".rjust(i6))
for i in range(len_alle):
    aus.write(("(" + str(i + 7) + ")").rjust(i7 + 1))
aus.write("\n")

aus.write("-" * (i1 + i2 + z3 + 2 + i4 + 1 + i5 + 1 + i6 + len_alle *(i7 + 1) + 2))
aus.write("\n")

# --------------------------------------------------------------
# (13-6) Ausgabe, eigentliche Ausgabe:

# len_alle     : Anzahl der plk-Dateien
# dat_anz      : Anzahl der Datei mit dieser Zeiechenkette
# nr           : laufende Nummer für Ausgabezeile (vor dem Filtern)
# nr_nach      : laufende Nummer für Ausgabezeile (nach dem Filtern)
# z            : Hilfsvariable: Schleifenvariable über neu3 / alle Wörter
# i            : Hilfsvariable
# neu3         : nach Sortierung und Umstrukturierung
# zkette       : Hilfsvariable: ein Wort
# laenge       : Hilfsvariable: zugehörige Länge
# anz          : Hilfsvariable: zugehörige Anzahl
# dat_anz      : Hilfsvariable: zugehörige Zahl der Dateien
# akk_anz      : Hilfsvariable: akk. Anzahl
# fd_vor       : Directory: Sammeln der Häufigkeiten vor dem Filtern
# ld_vor       : Directory: Sammeln der Längen vor dem Filtern
# fd_nach      : Directory: Sammeln der Häufigkeiten beim Filtern
# ld_nach      : Directory: Sammeln der Längen beim Filtern
# beding       : Hilfsvariable: steuert das Filtern
# p2           : Bedingung für Filtern: zulässiges Ausgabemuster
# re_frequency : Bedingung für Filtern: zulässige Frequenz
# re_lengths   : Bedingung für Filtern: zulässige Länge
# re_rank      : Bedingung für Filtern: zulässiger Rang
# re_files     : Bedingung für Filtern: zulässige Anzahl von Dateien

# --------------------------------------------------------------
# Vorbesetzen
for i in range(len_alle):
    anz_dat += [0]
    
nr      = 0
nr_nach = 0

# --------------------------------------------------------------
# Schleife (über alle Elemente in neu3)
for z in range(len(neu3)):
    nr       = z + 1
    zkette   = neu3[z][0]
    laenge   = neu3[z][1]
    anz      = neu3[z][2]
    dat_anz  = neu3[z][3]
    akk_anz += anz

# --------------------------------------------------------------
    # Bedingungen überprüfen (Filterung)
    # + p2          : zulässiges Ausgabemuster
    # + re_frequency: zulässige Häufigkeit
    # + re_lengths  : zulässige Länge
    # + re_rank     : zulässiger Rang
    # + re_files    : zulässige Dateizahl
    
    #Bedingung für Filterung
    beding = p2.match(zkette) and (anz in re_frequency) and (laenge in re_lengths) and (nr in re_rank) and (dat_anz in re_files)

# --------------------------------------------------------------
    # Ausgabe: eine Zeile mit Filterung
    if beding:
        nr_nach += 1
        akk_anz_nach += anz

        # eine Ausgabezeile schreiben
        aus.write(str(nr).rjust(i1) + leer)
        aus.write(str(laenge).rjust(i2) + leer)
        aus.write(str(zkette).ljust(z3) + 2 * leer)
        aus.write(str(anz).rjust(i4) + leer)
        aus.write(str(akk_anz_nach).rjust(i5) + leer)
        aus.write(str(dat_anz).rjust(i6) + leer)
        for i in range(len_alle):
            ri          = neu3[z][i + 4]
            anz_dat[i] += ri
            if (ri > 0):
                aus.write(str(ri).rjust(i7) + leer)
            else:
                aus.write(("-" * i7) + leer)
        aus.write("\n")

# --------------------------------------------------------------
# Abspann
aus.write("-" * (i1 + i2 + z3 + 2 + i4 + 1 + i5 + 1 + i6 + len_alle *(i7 + 1) + 2))
aus.write("\n")

aus.write((leer).rjust(i1) + leer)
aus.write((leer).rjust(i2) + leer)
aus.write((leer).ljust(z3) + 2 * leer)
aus.write(str(akk_anz_nach).rjust(i4) + leer)
aus.write(str(akk_anz_nach).rjust(i5) + leer)
aus.write((leer).rjust(i6) + leer)
for i in range(len_alle):
    aus.write(str(anz_dat[i]).rjust(i7) + leer)
aus.write("\n")

# --------------------------------------------------------------
# (13-7) Ausgabe, Zusammenfassung

# breite       : Breite des Ausageb-Labels
# akk_anz_vor  : akk. Anzahl der Tokens vor dem Filtern (= akk_anz)
# akk_anz_nach : akk. Anzahl nach dem Filtern
# nr           : Zahl der Types vor dem Filtern
# nr_nach      : Zahl der Types nach dem Filtern

__ueberschrift(result_summ,"-")

breite      = 42
akk_anz_vor = akk_anz

aus.write(res_token_pre.ljust(breite) + trenner + str(akk_anz_vor).rjust(i4 + 1) + "\n")
aus.write(res_types_pre.ljust(breite) + trenner + str(nr).rjust(i4 + 1) + "\n")
aus.write(res_ratio_pre.ljust(breite) + trenner + str(round(nr / akk_anz_vor, rndg)).rjust(i4 + 1) + "\n\n")

aus.write(res_token_post.ljust(breite) + trenner + str(akk_anz_nach).rjust(i4 + 1) + "\n")
aus.write(res_types_post.ljust(breite) + trenner + str(nr_nach).rjust(i4 + 1) + "\n")
aus.write(res_ratio_post.ljust(breite) + trenner +
          str(round(nr_nach / akk_anz_nach, rndg)).rjust(i4 + 1) + "\n\n")

aus.write(types_pre_post.ljust(breite) + trenner + str(round(nr_nach / nr, rndg)).rjust(i4 + 1) + "\n")
aus.write(token_pre_post.ljust(breite) + trenner + str(round(akk_anz_nach / akk_anz_vor, rndg)).rjust(i4 + 1)
          + "\n\n")

# --------------------------------------------------------------
# (13-8) Ausgabe, ld ausgeben (Längen-Verteilung):
#
# length_distribution : global: Schalter für ld
# P_ges_alle_laengen  : Ergebnisdaten (aus ges_alle_laengen) aus allen pkl-Dateien
# neu_gal             : Zusammenfassung aus P_ges_alle_laengen
# neu2_gal            : sortiert aus neu_gal
# neu3_gal            : neustrukturiert aus neu_gal / neu2_gal
# len_alle            : Anzahl der Dateien
# l3                  : lokale Hilfsvariable
# f                   : Schleifenvariable über alle Dateien
# g                   : Schleifenvariable über alle Items einer Datei
# pp                  : lokale Hilfsvariable
# laenge              : Hilfsgröße
# anzahl              : Hilfsgröße
# ergebnis            : lokale Hilfsstruktur
# z                   : Schleifenvariable neu2_gal ---> neu3_gal
# ww                  : lokale Hilfsvariable
# zwi                 : lokale Hilfsstruktur
# zwi2                : lokale Hilfsgröße
# zwi3                : lokale Hilfsgröße
# breite              : lokale Hilfsstruktur: Label-Breite
# nr                  : lokale Hilfsstruktur: laufende Nummer bei Ausgabe
# gessumme            : lokale Hilfsgröße: Summe über alle Zeilen 
# datsumme            : lokale Hilfsstruktur: Summe über alle Zeilen (über alle Dateien)
# gesmodus            : lokale Hilfsgröße: Berechnung des Modus für Gesamtzahlen
# datmodus            : lokale Hilfsstruktur: Berechnung des Modus für alle Dateien
# summe               : lokale Hilfsgröße
# maxlaenge           : lokale Hilfsgröße
# leer                : globale Hilfsgröße
# trenner             : globale Hilfsgröße
# gew_summe           : lokale Hilfsgröße

# P_ges_alle_laengen[i] --> (Neustrukturierung) --> neu_gal --> (Sortierung) --> neu2_gal --> (Neustrukturierung) --> neu3_gal

if length_distribution:
    __ueberschrift(caption_ld,"-")

# --------------------------------------------------------------
    # Vereinarungen
    neu_gal   = {} # Zusammenfassung aus P_ges_alle_laengen
    neu3_gal  = [] # neustrukturiert aus neu_gal --> neu2_gal

# --------------------------------------------------------------
    # Hilfsvariablen
    breite    = 20
    summe     = 0
    maxlaenge = 0
    nr        = 0
    gessumme  = 0
    datsumme  = [0 for x in range(len_alle)]
    gesmodus  = (0, 0)
    datmodus  = [(0, 0) for x in range(len_alle)] # (länge, anzahl)
    gesgsumme = 0 # für gewichteten Mittelwert
    datgsumme = [0 for x in range(len_alle)]

# --------------------------------------------------------------
    # Neustrukturierung
    l3 = len_alle + 2
    for f in range(len_alle):
        pp = P_ges_alle_laengen[f]
        for g in pp:
            laenge = g
            anzahl = pp[g]
            if laenge > maxlaenge:
                maxlaenge = laenge
        
            if not(laenge in neu_gal):
                ergebnis        = [0 for x in range(l3)]
                ergebnis[0]     = anzahl
                ergebnis[f + 2] = anzahl
                ergebnis[1]     = 1
                neu_gal[laenge] = ergebnis
            else:
                neu_gal[laenge][f+2] = anzahl
                neu_gal[laenge][0]  += anzahl
                neu_gal[laenge][1]  += 1

            if summe < neu_gal[laenge][0]:
                summe = neu_gal[laenge][0]

# --------------------------------------------------------------
    # Sortierung
    neu2_gal = sorted(neu_gal)            

# --------------------------------------------------------------
    # Neustrukturierung
    for z in range(len(neu2_gal)):
        ww        = neu2_gal[z]
        zwi       = [ww]
        zwi      += neu_gal[ww]
        neu3_gal += [tuple(zwi)]

# --------------------------------------------------------------
    # Hilfsvariablen für die Ausgabe
    i1 = floor(lg(len(neu3_gal))) + 2# Breite der Kolumne 1 (laufende Nummer); adaptierbar <-- len(neu3_gal)
    i2 = floor(lg(maxlaenge)) + 2    # Breite der Kolumne 2 (Länge)
    i3 = floor(lg(summe)) + 3        # Breite der Kolumne 3 (Summenzahl über alle Dateien); adaptierbar
    i4 = floor(lg(len_alle)) + 3     # Breite der Kolumne 5 (Zahl der Dateien); adaptierbar
    i5 = i3                          # Breite der Kolumne 6 (Anzahl); adaptierbar <-- summe

# --------------------------------------------------------------
    # Legende und Kopf
    aus.write("(1) {0}".format(ld_hdr_nr) + "\n")
    aus.write("(2) {0}".format(ld_hdr_length) + "\n")
    aus.write("(3) {0}".format(ld_hdr__word_nr) + "\n")
    aus.write("(4) {0}".format(ld_hdr_files_nr) + "\n")
    for f in range(len_alle):
        aus.write("({0}) {1} {2} ({3} --> \n    {4})".format(str(i + 5), ld_hdr_infile, str(f), alle[f], P_kopf[f][7])  + "\n")
    aus.write("\n")

    aus.write("(1)".rjust(i1))
    aus.write("(2)".rjust(i2))
    aus.write("(3)".rjust(i3))
    aus.write("(4)".rjust(i4))
    for f in range(len_alle):
        aus.write(("(" + str(f + 5) + ")").rjust(i5))
    aus.write("\n")

    aus.write("-" * (i1 + i2 + i3 + i4 + len_alle *(i5))+ "\n")

# --------------------------------------------------------------
    # Ausgabeschleife
    for z in range(len(neu3_gal)):               # jeweils eine Zeile
        nr += 1
        aus.write(str(nr).rjust(i1))             # 1. Item
        aus.write(str(neu3_gal[z][0]).rjust(i2)) # 2. Item
        aus.write(str(neu3_gal[z][1]).rjust(i3)) # 3. Item
        gesgsumme += neu3_gal[z][0] * neu3_gal[z][1]
        if neu3_gal[z][1] > gesmodus[1]:
            gesmodus = (neu3_gal[z][0], neu3_gal[z][1])
        gessumme += neu3_gal[z][1]
        
        aus.write(str(neu3_gal[z][2]).rjust(i4)) # 4. Item
        
        for f in range(len_alle):
            zwi2          = neu3_gal[z][f + 3]
            datsumme[f]  += zwi2
            datgsumme[f] += neu3_gal[z][0] * neu3_gal[z][f + 3]
            if zwi2 > datmodus[f][1]:
                datmodus[f] = (neu3_gal[z][0], zwi2)
            if zwi2 > 0:
                aus.write(str(zwi2).rjust(i5))   # 5ff. Item
            else:
                aus.write("----".rjust(i5))      # 5ff. Item
        aus.write("\n")

# --------------------------------------------------------------
    # Abspann
    aus.write("-" * (i1 + i2 + i3 + i4 + len_alle *(i5))+ "\n")
    aus.write(ld_summary_sum.ljust(i1+i2))
    aus.write(str(gessumme).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(str(datsumme[f]).rjust(i5))
    aus.write("\n")

    aus.write(ld_modus.ljust(i1+i2))
    aus.write(str(gesmodus[1]).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(str(datmodus[f][1]).rjust(i5))
    aus.write("\n")

    aus.write(ld_at.ljust(i1+i2))
    aus.write(str(gesmodus[0]).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(str(datmodus[f][0]).rjust(i5))
    aus.write("\n")

    aus.write(ld_wa_short.ljust(i1+i2))
    aus.write(str(round(gesgsumme / gessumme, 1)).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(str(round(datgsumme[f] / datsumme[f], 1)).rjust(i5))
    aus.write("\n\n")
    aus.write(ld_wa_long + "\n\n")

    aus.write(ld_min_length.ljust(breite) + trenner + str(min(neu3_gal)[0]).rjust(i5) + "\n")
    aus.write(ld_max_length.ljust(breite) + trenner + str(max(neu3_gal)[0]).rjust(i5) + "\n\n")

# --------------------------------------------------------------
# (13-9) Ausgabe, fd ausgeben (Häufigkeitsverteilung):
#
# frequency_distribution: global; Schalter für fd
# P_alle_haeufigkeiten  : Ergebnisdaten (aus ges_haeufigkeiten) aus allen pkl-Dateien
# neu_gh                : Zusammenfassung aus P_alle_haeufigkeiten
# neu2_gh               : sortiert aus neu_gh
# neu3_gh               : neustrukturiert aus neu_gh / neu2_gh
# len_alle              : Anzahl der Dateien
# l3                    : lokale HilfsvariableAnzahl der Wörter mit dieser Länge über alle Dateien
# f                     : Schleifenvariable über alle Dateien
# g                     : Schleifenvariable über alle Items einer Datei
# pp                    : lokale Hilfsvariable
# haeufig               :
# anzahl                :
# ergebnis              : lokale Hilfsstruktur
# z                     : Schleifenvariable neu2_gh ---> neu3_gh
# ww                    : lokale Hilfsvariable
# zwi                   : lokale Hilfsstruktur
# zwi2                  : lokale Hilfsgröße
# zwi3                  : lokale Hilfsgröße
# breite                : lokale Hilfsstruktur: Label-Breite
# nr                    : lokale Hilfsstruktur: laufende Nummer bei Ausgabe
# gessumme              : lokale Hilfsgröße: Summe über alle Zeilen 
# datsumme              : lokale Hilfsstruktur: Summe über alle Zeilen (über alle Dateien)
# gesmodus              : lokale Hilfsgröße: Berechnung des Modus für Gesamtzahlen
# datmodus              : lokale Hilfsstruktur: Berechnung des Modus für alle Dateien
# summe                 : lokale Hilfsgröße
# maxfreq               : lokale Hilfsgröße
# leer                  : globale Hilfsgröße
# trenner               : globale Hilfsgröße

# P_ges_haeufigkeiten[i] --> (Neustrukturierung) --> neu_gh --> (Sortierung) --> neu2_gh --> (Neustrukturierung) --> neu3_gh

if frequency_distribution:
    __ueberschrift(caption_fd,"-")

# --------------------------------------------------------------
    # Vereinbarungen
    neu_gh  = {} # Zusammenfassung aus P_ges_haeufigkeiten
    neu3_gh = [] # 

# --------------------------------------------------------------
    # Hilfsvariablen
    breite    = 20
    summe     = 0
    maxfreq   = 0
    nr        = 0
    gessumme  = 0
    datsumme  = [0 for x in range(len_alle)]
    gesmodus  = (0, 0)
    datmodus  = [(0, 0) for x in range(len_alle)] # (länge, anzahl)

# --------------------------------------------------------------
    # Neustrukturierung
    l3 = len_alle + 2
    for f in range(len_alle):
        pp = P_ges_haeufigkeiten[f]
        for g in pp:
            haeufig = g
            anzahl  = pp[g]
            if haeufig > maxfreq:
                maxfreq = haeufig
        
            if not(haeufig in neu_gh):
                ergebnis        = [0 for x in range(l3)]
                ergebnis[0]     = anzahl
                ergebnis[f + 2] = anzahl 
                ergebnis[1]     = 1
                neu_gh[haeufig] = ergebnis
            else:
                neu_gh[haeufig][f+2] = anzahl
                neu_gh[haeufig][0]  += anzahl
                neu_gh[haeufig][1]  += 1

            if summe < neu_gh[haeufig][0]:
                summe = neu_gh[haeufig][0]

# --------------------------------------------------------------
    #Sortierung
    neu2_gh = sorted(neu_gh)            

# --------------------------------------------------------------
    # Neustrukturierung
    for z in range(len(neu2_gh)):
        ww        = neu2_gh[z]
        zwi       = [ww]
        zwi      += neu_gh[ww]
        neu3_gh  += [tuple(zwi)]

# --------------------------------------------------------------
    # Hilfsvariablen für die Ausgabe
    i1 = floor(lg(len(neu3_gh))) + 2 # Breite der Kolumne 1 (laufende Nummer); adaptierbar <-- len(neu3_gal)
    i2 = floor(lg(maxfreq)) + 2      # Breite der Kolumne 2 (Häufigkeit)
    i3 = floor(lg(summe)) + 2        # Breite der Kolumne 3 (Summenzahl über alle Dateien); adaptierbar
    i4 = floor(lg(len_alle)) + 3     # Breite der Kolumne 5 (Zahl der Dateien); adaptierbar
    i5 = i3                          # Breite der Kolumne 6 (Anzahl); adaptierbar <-- summe

# --------------------------------------------------------------
    # Legende und Kopf
    aus.write("(1) {0}".format(ld_hdr_nr) + "\n")
    aus.write("(2) {0}".format(fd_hdr_freq) + "\n")
    aus.write("(3) {0}".format(fd_hdr_freq_nr) + "\n")
    aus.write("(4) {0}".format(fd_hdr_files_nr) + "\n")
    for f in range(len_alle):
        aus.write("({0}) {1} {2} ({3} --> \n    {4})".format(str(i + 5), fd_hdr_infile, str(f), alle[f], P_kopf[f][7]) + "\n")
    aus.write("\n")

    aus.write("(1)".rjust(i1))
    aus.write("(2)".rjust(i2))
    aus.write("(3)".rjust(i3))
    aus.write("(4)".rjust(i4))
    for f in range(len_alle):
        aus.write(("(" + str(f + 5) + ")").rjust(i5))
    aus.write("\n")

    aus.write("-" * (i1 + i2 + i3 + i4 + len_alle *(i5))+ "\n")

# --------------------------------------------------------------
    # Ausgabeschleife
    for z in range(len(neu3_gh)):              # jeweils eine Zeile
        nr += 1
        aus.write(str(nr).rjust(i1))           # 1. Item
        aus.write(str(neu3_gh[z][0]).rjust(i2))# 2. Item
        aus.write(str(neu3_gh[z][1]).rjust(i3))# 3. Item
        zwi3 = neu3_gh[z][1]
        if zwi3 > gesmodus[1]:
            gesmodus = (neu3_gh[z][0], zwi3)
        gessumme += zwi3
        
        aus.write(str(neu3_gh[z][2]).rjust(i4))# 4. Item
        
        for f in range(len_alle):
            zwi2 = neu3_gh[z][f + 3]
            if zwi2 > datmodus[f][1]:
                datmodus[f] = (neu3_gh[z][0], zwi2)
            datsumme[f] += zwi2
            if zwi2 > 0:
                aus.write(str(zwi2).rjust(i5)) # 5ff. Item
            else:
                aus.write("----".rjust(i5))    # 5ff. Item
        aus.write("\n")

# --------------------------------------------------------------
    # Abspann
    aus.write("-" * (i1 + i2 + i3 + i4 + len_alle *(i5))+ "\n")
    aus.write(fd_summary_sum.ljust(i1+i2))
    aus.write(str(gessumme).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(str(datsumme[f]).rjust(i5))
    aus.write("\n")

    aus.write(fd_modus.ljust(i1+i2))
    aus.write(str(gesmodus[1]).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(str(datmodus[f][1]).rjust(i5))
    aus.write("\n")

    aus.write(fd_at.ljust(i1+i2))
    aus.write(str(gesmodus[0]).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(str(datmodus[f][0]).rjust(i5))
    aus.write("\n\n")

    aus.write(fd_min_freq.ljust(breite) + trenner + str(min(neu3_gh)[0]).rjust(i2) + "\n")
    aus.write(fd_max_freq.ljust(breite) + trenner + str(max(neu3_gh)[0]).rjust(i2) + "\n\n")

# --------------------------------------------------------------
# (13-10) Ausgabe, cd ausgeben (Zeichen-Verteilung):
#
# character_distribution: global; Schalter für cd
# P_ges_alle_zeichen    : Ergebnisdaten (aus ges_alle_zeichen) aus allen pkl-Dateien
# neu_gaz               : Zusammenfassung aus P_ges_alle_zeichen
# neu2_gaz              : sortiert aus neu_gaz
# neu3_gaz              : neustrukturiert aus neu_gaz / neu2_gaz
# len_alle              : Anzahl der Dateien
# l3                    : lokale Hilfsvariable
# f                     : Schleifenvariable über alle Dateien
# g                     : Schleifenvariable über alle Items einer Datei
# pp                    : lokale Hilfsvariable
# zeichen               :
# anzahl                :
# ergebnis              : lokale Hilfsstruktur
# z                     : Schleifenvariable neu2_gaz ---> neu3_gaz
# ww                    : lokale Hilfsvariable
# zwi                   : lokale Hilfsstruktur
# zwi2                  : lokale Hilfsgröße
# zwi3                  : lokale Hilfsgröße
# breite                : lokale Hilfsstruktur: Label-Breite
# nr                    : lokale Hilfsstruktur: laufende Nummer bei Ausgabe
# gessumme              : lokale Hilfsgröße: Summe über alle Zeilen 
# datsumme              : lokale Hilfsstruktur: Summe über alle Zeilen (über alle Dateien)
# gesmodus              : lokale Hilfsgröße: Berechnung des Modus für Gesamtzahlen
# datmodus              : lokale Hilfsstruktur: Berechnung des Modus für alle Dateien
# summe                 : lokale Hilfsgröße
# maxzahl               : lokale Hilfsgröße
# leer                  : globale Hilfsgröße
# trenner               : globale Hilfsgröße

# P_ges_alle_zeichen[i] --> (Neustrukturierung) --> neu_gaz --> (Sortierung) --> neu2_gaz --> (Neustrukturierung) --> neu3_gaz

if character_distribution:
    __ueberschrift(caption_cd,"-")

# --------------------------------------------------------------
    # Vereinbarungen
    neu_gaz  = {} # Zusammenfassung aus P_ges_alle_zeichen
    neu3_gaz = [] # neustrukturiert aus neu_gaz / neu2_gaz

# --------------------------------------------------------------
    # Hilfsvariablen
    breite   = 25
    summe    = 0
    maxzahl  = 0
    nr       = 0
    gessumme = 0
    datsumme = [0 for x in range(len_alle)]
    gesmodus = (0, 0)
    datmodus = [(0, 0) for x in range(len_alle)] # (länge, anzahl)

# --------------------------------------------------------------
    # Neustrukturierung
    l3 = len_alle + 2
    for f in range(len_alle):
        pp = P_ges_alle_zeichen[f]
        for g in pp:
            zeichen = g
            anzahl  = pp[g]
            if maxzahl < anzahl:
                amaxzahl = anzahl
        
            if not(zeichen in neu_gaz):
                ergebnis        = [0 for x in range(l3)]
                ergebnis[0]     = anzahl
                ergebnis[f + 2] = anzahl 
                ergebnis[1]     = 1
                neu_gaz[zeichen]= ergebnis
            else:
                neu_gaz[zeichen][f+2] = anzahl
                neu_gaz[zeichen][0]  += anzahl
                neu_gaz[zeichen][1]  += 1

            if summe < neu_gaz[zeichen][0]:
                summe = neu_gaz[zeichen][0]

# --------------------------------------------------------------
    #Sortierung
    neu2_gaz = sorted(neu_gaz)            

# --------------------------------------------------------------
    # Neustrukturierung
    for z in range(len(neu2_gaz)):
        ww        = neu2_gaz[z]
        zwi       = [ww]
        zwi      += neu_gaz[ww]
        neu3_gaz += [tuple(zwi)]

# --------------------------------------------------------------
    # Hilfsvariablen für die Ausgabe
    i1 = floor(lg(len(neu3_gaz))) + 2 # Breite der Kolumne 1 (laufende Nummer); adaptierbar <-- len(neu3_gaz)
    i2 = 3                            # Breite der Kolumne 2 (Zeichen)
    i2a = 7                           # zugehöriger Hex-Code
    i3 = floor(lg(summe)) + 3         # Breite der Kolumne 3 (Summenzahl über alle Dateien); adaptierbar
    i4 = floor(lg(len_alle)) + 3      # Breite der Kolumne 5 (Zahl der Dateien); adaptierbar
    i5 = i3                           # Breite der Kolumne 6 (Anzahl); adaptierbar <-- summe

# --------------------------------------------------------------
    # Legende und Kopf
    aus.write("(1) {0}".format(cd_hdr_nr) + "\n")
    aus.write("(2) {0}".format(cd_hdr_char) + "\n")
    aus.write("(3) {0}".format(cd_hdr_hex) + "\n")
    aus.write("(4) {0}".format(cd_hdr_char_nr) + "\n")
    aus.write("(5) {0}".format(cd_hdr_files_nr) + "\n")
    for f in range(len_alle):
        aus.write("({0}) {1} {2} ({3}  --> \n    {4})".format(str(f + 6), cd_hdr_infile, str(f), alle[f], P_kopf[f][7]) + "\n")
    aus.write("\n")

    aus.write("(1)".rjust(i1))
    aus.write("(2)".rjust(i2))
    aus.write("(3)".rjust(i2a))
    aus.write("(4)".rjust(i3))
    aus.write("(5)".rjust(i4))
    for f in range(len_alle):
        aus.write(("(" + str(f + 6) + ")").rjust(i5))
    aus.write("\n")

    aus.write("-" * (i1 + i2 + i2a + i3 + i4 + len_alle *(i5))+ "\n")

# --------------------------------------------------------------
    # Ausgabeschleife
    for z in range(len(neu3_gaz)):                     # jeweils eine Zeile
        nr += 1
        aus.write(str(nr).rjust(i1))                   # 1. Item
        aus.write(str(neu3_gaz[z][0]).rjust(i2))       # 2. Item
        aus.write(__chr_hex(neu3_gaz[z][0]).rjust(i2a))# 3. Item
        aus.write(str(neu3_gaz[z][1]).rjust(i3))       # 4. Item
        zwi3 = neu3_gaz[z][1]
        if zwi3 > gesmodus[1]:
            gesmodus = (neu3_gaz[z][0], zwi3)
        gessumme += zwi3
        
        aus.write(str(neu3_gaz[z][2]).rjust(i4))       # 5. Item
        
        for f in range(len_alle):
            zwi2 = neu3_gaz[z][f + 3]
            if zwi2 > datmodus[f][1]:
                datmodus[f] = (neu3_gaz[z][0], zwi2)
            datsumme[f] += zwi2
            if zwi2 > 0:
                aus.write(str(zwi2).rjust(i5))         # 6ff. Item
            else:
                aus.write("----".rjust(i5))            # 6ff. Item
        aus.write("\n")

# --------------------------------------------------------------
    # Abspann
    aus.write("-" * (i1 + i2 + i2a + i3 + i4 + len_alle *(i5))+ "\n")
    aus.write(cd_summary_sum.ljust(i1+i2+i2a))
    aus.write(str(gessumme).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(str(datsumme[f]).rjust(i5))
    aus.write("\n")

    aus.write(cd_modus.ljust(i1+i2+i2a))
    aus.write(str(gesmodus[1]).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(str(datmodus[f][1]).rjust(i5))
    aus.write("\n")

    aus.write(cd_at.ljust(i1+i2+i2a))
    aus.write(__chr_out(gesmodus[0]).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(__chr_out(datmodus[f][0]).rjust(i5))
    aus.write("\n\n")

# --------------------------------------------------------------
# (13-11) Ausgabe, sd ausgeben (Trennzeichen-Verteilung):
#
# separator_distribution: global; Schalter für sd
# P_ges_trennzeichen    : Ergebnisdaten (aus ges_trennzeichen) aus allen pkl-Dateien
# neu_gt                : Zusammenfassung aus P_ges_trennzeichen
# neu2_gt               : sortiert aus neu_gh
# neu3_gt               : neustrukturiert aus neu_gt / neu2_gt
# len_alle              : Anzahl der Dateien
# l3                    : lokale Hilfsvariable
# f                     : Schleifenvariable über alle Dateien
# g                     : Schleifenvariable über alle Items einer Datei
# pp                    : lokale Hilfsvariable
# zeichen               :
# anzahl                :
# ergebnis              : lokale Hilfsstruktur
# z                     : Schleifenvariable neu2_gt ---> neu3_gt
# ww                    : lokale Hilfsvariable
# zwi                   : lokale Hilfsstruktur
# zwi2                  : lokale Hilfsgröße
# zwi3                  : lokale Hilfsgröße
# breite                : lokale Hilfsstruktur: Label-Breite
# nr                    : lokale Hilfsstruktur: laufende Nummer bei Ausgabe
# gessumme              : lokale Hilfsgröße: Summe über alle Zeilen 
# datsumme              : lokale Hilfsstruktur: Summe über alle Zeilen (über alle Dateien)
# gesmodus              : lokale Hilfsgröße: Berechnung des Modus für Gesamtzahlen
# datmodus              : lokale Hilfsstruktur: Berechnung des Modus für alle Dateien
# summe                 : lokale Hilfsgröße
# maxzahl               : lokale Hilfsgröße
# leer                  : globale Hilfsgröße
# trenner               : globale Hilfsgröße

# P_ges_alle_zeichen[i] --> (Neustrukturierung) --> neu_gt --> (Sortierung) --> neu2_gt --> (Neustrukturierung) --> neu3_gt

if separator_distribution:
    __ueberschrift(caption_sd,"-")

# --------------------------------------------------------------
    # Vereinbarungen
    neu_gt  = {} # Zusammenfassung aus P_ges_trennzeichen
    neu3_gt = [] # neustrukturiert aus neu_gt / neu2_gt

# --------------------------------------------------------------
    # Hilfsvariablen
    breite   = 25
    summe    = 0
    maxzahl  = 0
    nr       = 0
    gessumme = 0
    datsumme = [0 for x in range(len_alle)]
    gesmodus = (0, 0)
    datmodus = [(0, 0) for x in range(len_alle)] # (länge, anzahl)

# --------------------------------------------------------------
    # Neustrukturierung
    l3 = len_alle + 2
    for f in range(len_alle):
        pp = P_ges_trennzeichen[f]
        for g in pp:
            zeichen = g
            anzahl  = pp[g]
        
            if not(zeichen in neu_gt):
                ergebnis        = [0 for x in range(l3)]
                ergebnis[0]     = anzahl
                ergebnis[f + 2] = anzahl 
                ergebnis[1]     = 1
                neu_gt[zeichen] = ergebnis
            else:
                neu_gt[zeichen][f+2] = anzahl
                neu_gt[zeichen][0]  += anzahl
                neu_gt[zeichen][1]  += 1

            if summe < neu_gt[zeichen][0]:
                summe = neu_gt[zeichen][0]

# --------------------------------------------------------------
    #Sortierung
    neu2_gt = sorted(neu_gt)            

# --------------------------------------------------------------
    # Neustrukturierung
    for z in range(len(neu2_gt)):
        ww        = neu2_gt[z]
        zwi       = [ww]
        zwi      += neu_gt[ww]
        neu3_gt  += [tuple(zwi)]

# --------------------------------------------------------------
    # Hilfsvariablen für die Ausgabe
    i1  = floor(lg(len(neu3_gt))) + 2 # Breite der Kolumne 1 (laufende Nummer); adaptierbar <-- len(neu3_gt)
    i2  = 5                           # Breite der Kolumne 2 (Zeichen)
    i2a = 7                           # zugehöriger Hex-Code
    i3  = floor(lg(summe)) + 3        # Breite der Kolumne 3 (Summenzahl über alle Dateien); adaptierbar
    i4  = floor(lg(len_alle)) + 3     # Breite der Kolumne 5 (Zahl der Dateien); adaptierbar
    i5  = i3                          # Breite der Kolumne 6 (Anzahl); adaptierbar <-- summe

# --------------------------------------------------------------
    # Legende und Kopf
    aus.write("(1) {0}".format(sd_hdr_nr) + "\n")
    aus.write("(2) {0}".format(sd_hdr_char) + "\n")
    aus.write("(3) {0}".format(sd_hdr_hex) + "\n")
    aus.write("(4) {0}".format(sd_hdr_char_nr) + "\n")
    aus.write("(5) {0}".format(sd_hdr_files_nr) + "\n")
    for f in range(len_alle):
        aus.write("({0}) {1} {2} ({3} --> \n    {4})".format(str(f + 6), sd_hdr_infile, str(f), alle[f], P_kopf[f][7]) + "\n")
    aus.write("\n")

    aus.write("(1)".rjust(i1))
    aus.write("(2)".rjust(i2))
    aus.write("(3)".rjust(i2a))
    aus.write("(4)".rjust(i3))
    aus.write("(5)".rjust(i4))
    for f in range(len_alle):
        aus.write(("(" + str(f + 6) + ")").rjust(i5))
    aus.write("\n")

    aus.write("-" * (i1 + i2 + i2a + i3 + i4 + len_alle *(i5))+ "\n")

# --------------------------------------------------------------
    # Ausgabeschleife
    for z in range(len(neu3_gt)):                     # jeweils eine Zeile
        nr += 1
        aus.write(str(nr).rjust(i1))                  # 1. Item
        aus.write(__chr_out(neu3_gt[z][0]).rjust(i2)) # 2. Item
        aus.write(__chr_hex(neu3_gt[z][0]).rjust(i2a))# 3. Item
        aus.write(str(neu3_gt[z][1]).rjust(i3))       # 4. Item
        zwi3 = neu3_gt[z][1]
        if zwi3 > gesmodus[1]:
            gesmodus = (neu3_gt[z][0], zwi3)
        gessumme += zwi3
        
        aus.write(str(neu3_gt[z][2]).rjust(i4))       # 5. Item
        
        for f in range(len_alle):
            zwi2 = neu3_gt[z][f + 3]
            if zwi2 > datmodus[f][1]:
                datmodus[f] = (neu3_gt[z][0], zwi2)
            datsumme[f] += zwi2
            if zwi2 > 0:
                aus.write(str(zwi2).rjust(i5))        # 6ff. Item
            else:
                aus.write("----".rjust(i5))           # 6ff. Item
        aus.write("\n")

# --------------------------------------------------------------
    # Abspann
    aus.write("-" * (i1 + i2 + i2a + i3 + i4 + len_alle *(i5))+ "\n")
    aus.write(sd_summary_sum.ljust(i1+i2+i2a))
    aus.write(str(gessumme).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(str(datsumme[f]).rjust(i5))
    aus.write("\n")

    aus.write(sd_modus.ljust(i1+i2+i2a))
    aus.write(str(gesmodus[1]).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(str(datmodus[f][1]).rjust(i5))
    aus.write("\n")

    aus.write(sd_at.ljust(i1+i2+i2a))
    aus.write(__chr_out(gesmodus[0]).rjust(i3))
    aus.write(leer.rjust(i4))
    for f in range(len_alle):
        aus.write(__chr_out(datmodus[f][0]).rjust(i5))
    aus.write("\n\n")


# ==============================================================
# (14) Ausgabe schließen

aus.close()









