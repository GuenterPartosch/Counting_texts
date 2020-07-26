#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# multizaehlen_ini.py
# Stand: 2018-08-17
#        2020-07-26

# Abhängigkeiten:
# multizaehlen_ini.py
# + wird in multizaehlen.py als Modul geladen

files_text    = "zu verarbeitende Dateien (*.plk)"
files_anz_text= "Beschränkung der Dateien-Zahl (*.plk) mit Zeichenkette"
sort1_text    = "1. Sortierung [a+|a-|A+|A-]"
sort2_text    = "2. Sortierung [L+|L-|F+|F-|D+|D-]"
out_text      = "Ausgabedatei"
template_text = "Beschränkung auf bestimmte Wort-Muster (Muster)"
lengths_text  = "Beschränkung auf bestimmte Wortlängen"
rank_text     = "Beschränkung auf bestimmte Rangfolge"
freq_text     = "Beschränkung auf bestimmte Worthäufigkeiten"
version_text  = "Version des Programms ausgeben"
autor_text    = "Autor des Programms ausgeben"
fd_text       = "Worthäufigkeiten-Verteilung berechnen"
ld_text       = "Wortlängen-Verteilung berechnen"
sd_text       = "Trennzeichen-Verteilung berechnen"
cd_text       = "Zeichen-Verteilung berechnen"

in_name       = ""
out_name      = "./aus.txt"   # muss ggf. angepasst werden
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
