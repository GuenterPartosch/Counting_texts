#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# zaehlen-ini.py: Initialisierung, Vorbesetzungen
# Stand: 2018-08-17
#        2020-07-22

# Abhängigkeiten
# zaehlen_ini.py
# + wird von menue_zaehlen.py als Modul geladen
# + wird von zaehlen.py als Modul geladen

# Anpassungen für in_name und out:name

in_name          = "./ein.txt"    # ggf. anpassen     
out_name         = "./aus.txt"    # ggf. anpassen

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
zaehlen_ini_Datum= "2020-07-22"
programm_datum   = "2020-07-23"
programm_vers    = "2.13.1"
