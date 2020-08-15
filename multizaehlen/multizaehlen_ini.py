#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# multizaehlen_ini.py
# Stand: 2018-08-17
#        2020-07-27
#        2020-08-02 (Voreinstellung geändert)
#        2020-08-15 (Ausgabe-Strings)

# (C) Günter Partosch 2018-2010

# Abhängigkeiten:
# multizaehlen_ini.py
# + wird in multizaehlen.py als Modul geladen

mz_ini_datum           = "2020-08-15"

in_name                = ""
out_name               = "./mz_out.txt"   # muss ggf. angepasst werden
word_template          = """^.+$"""
p_lengths              = "1,100"
p_files                = "1,20"
p_frequency            = "1,20000"
p_rank                 = "1,60000"
sort_first             = "a+"
sort_second            = ""
frequency_distribution = False
length_distribution    = False
separator_distribution = False
character_distribution = False
rndg                   = 3

# Ausgabe-Strings
# ===================================================================

# Programm-Paramdeter, global
# -------------------------------------------------------------------
main_caption_text  = "Vergleichendes Auszählen von Texten"
prg_name_text      = "multizaehlen.py"
prg_vers_text      = "1.11.0"
prg_date_text      = "2020-08-15"
prg_author_text    = "Günter Partosch"
author_email_text  = "Guenter.Partosch@hrz.uni-giessen.de"
author_institution = "Justus-Liebig-Universität Gießen, Hochschulrechenzentrum"

# Argparse (x)
# -------------------------------------------------------------------
files_text     = "zu verarbeitende Dateien (*.plk)"
files_anz_text = "Beschränkung der Dateien-Zahl (*.plk) mit Zeichenkette"
sort1_text     = "1. Sortierung [a+|a-|A+|A-]"
sort2_text     = "2. Sortierung [L+|L-|F+|F-|D+|D-]"
out_text       = "Ausgabedatei"
template_text  = "Beschränkung auf bestimmte Wort-Muster (Muster)"
lengths_text   = "Beschränkung auf bestimmte Wortlängen"
rank_text      = "Beschränkung auf bestimmte Rangfolge"
freq_text      = "Beschränkung auf bestimmte Worthäufigkeiten"
version_text   = "Version des Programms ausgeben"
autor_text     = "Autor des Programms ausgeben"
fd_text        = "Worthäufigkeiten-Verteilung berechnen"
ld_text        = "Wortlängen-Verteilung berechnen"
sd_text        = "Trennzeichen-Verteilung berechnen"
cd_text        = "Zeichen-Verteilung berechnen"

argp_pos_par   = 'Positionsparameter'
argp_opt_par   = 'Optionale Parameter'
argp_default   = 'Voreinstellung'

# Kopf, allgemein
# -------------------------------------------------------------------
head_content   = "Inhalt"                          # breite: 43
head_prg_name  = "Name des Programms"
head_prg_vers  = "Version des Programms"
head_prg_date  = "Bearbeitungsdatum"
prg_author     = "Autor des Programms"
author_email   = "E-Mail-Adresse"
author_inst    = "Institution" 
res_pre_ld     = "Ergebnisse (Längenverteilung vor dem Filtern)"
res_pre_fd     = "Ergebnisse (Häufigkeitsverteilung vor dem Filtern)"
res_pre_cd     = "Ergebnisse (Zeichenverteilung vor dem Filtern)"
res_pre_sd     = "Ergebnisse (Trennzeichenverteilung vor dem Filtern)"
head_prg_para  = "Programm-Parameter"
head_result    = "Ergebnisse"
head_summary   = "Zusammenfassung"

# Kopf, Programmparameter
# -------------------------------------------------------------------
sub_caption    = "Programm-Parameter"     # breite: 57
prg_call       = "Programm-Aufruf"

# Kopf, Legende
# -------------------------------------------------------------------
caption_leg    = "Ergebnisse"
leg_rank       = "Rangfolge"
leg_str_len    = "Länge der Zeichenkette"
leg_string     = "Zeichenkette"
leg_str_freq   = "Häufigkeit der Zeichenkette in allen Dateien"
leg_acc_freq   = "akk. Häufigkeit der Zeichenkette"
leg_file_nr    = "Zahl der Dateien mit dieser Zeichenkette"
leg_in_file    = "Eingabedatei"

# Ausgabe, Zusammenfassung
# -------------------------------------------------------------------
result_summ    = "Zusammenfassung"                                  # bfreite: 42
res_token_pre  = "Zahl der Tokens (vor dem Filtern)"
res_types_pre  = "Zahl der Types (vor dem Filtern)"
res_ratio_pre  = "Verhältnis Types/Tokens (vor dem Filtern)"
res_token_post = "Zahl der Tokens (nach dem Filtern)"
res_types_post = "Zahl der Types (nach dem Filtern)"
res_ratio_post = "Verhältnis Types/Tokens (nach dem Filtern)"
types_pre_post = "Verhältnis Types (nach/vor Filtern)"
token_pre_post = "Verhältnis Tokens (nach/vor Filtern)"

# Ausgabe, Längenverteilung
# -------------------------------------------------------------------
caption_ld     = "Ergebnisse (Längenverteilung vor dem Filtern)"
ld_hdr_nr      = "laufende Nummer"
ld_hdr_length  = "Länge"
ld_hdr__word_nr= "Anzahl der Wörter mit dieser Länge über alle Dateien"
ld_hdr_files_nr= "Zahl der Dateien mit Wörter dieser Länge"
ld_hdr_infile  = "Eingabedatei"
ld_summary_sum = "Summen:"
ld_modus       = "Modus:"
ld_at          = "bei:"
ld_wa_short    = "gMW"
ld_wa_long     = "(gMW = gewichteter Mittelwert)"
ld_min_length  = "kleinste Länge"
ld_max_length  = "größte Länge"

# Ausgabe, Häufigkeitsverteilung
# -------------------------------------------------------------------
caption_fd     = "Ergebnisse (Häufigkeitsverteilung vor dem Filtern)"
fd_hdr_nr      = ld_hdr_nr
fd_hdr_freq    = "Häufigkeit"
fd_hdr_freq_nr = "Anzahl der Wörter mit dieser Häufigkeit über alle Dateien"
fd_hdr_files_nr= "Zahl der Dateien mit Wörter dieser Häufigkeit"
fd_hdr_infile  = ld_hdr_infile
fd_summary_sum = ld_summary_sum
fd_modus       = ld_modus
fd_at          = ld_at
fd_min_freq    = "kleinste Häufigkeit"
fd_max_freq    = "größte Häufigkeit"

# Ausgabe, Zeichenverteilung
# -------------------------------------------------------------------
caption_cd     = "Ergebnisse (Zeichenverteilung vor dem Filtern)"
cd_hdr_nr      = ld_hdr_nr
cd_hdr_char    = "Zeichen"
cd_hdr_hex     = "zugehöriger Hex-Code"
cd_hdr_char_nr = "Anzahl dieses Zeichens über alle Dateien"
cd_hdr_files_nr= "Zahl der Dateien mit diesem Zeichen"
cd_hdr_infile  = ld_hdr_infile
cd_summary_sum = ld_summary_sum
cd_modus       = ld_modus
cd_at          = ld_at

# Ausgabe, Trennzeichenverteilung
# -------------------------------------------------------------------
caption_sd     = "Ergebnisse (Trennzeichenverteilung vor dem Filtern)"
sd_hdr_nr      = ld_hdr_nr
sd_hdr_char    = cd_hdr_char
sd_hdr_hex     = cd_hdr_hex
sd_hdr_char_nr = cd_hdr_char_nr
sd_hdr_files_nr= cd_hdr_files_nr
sd_hdr_infile  = ld_hdr_infile
sd_summary_sum = ld_summary_sum
sd_modus       = ld_modus
sd_at          = ld_at

# Fehlermeldungen
# -------------------------------------------------------------------
err_out        = "---Ausgabedatei {0} kann nicht geöffnet werden. Programmabbruch"
err_pkl_open   = "---Datei {0} kann nicht geöffnet werden. Programmabbruch!"
err_type       = "---Datei {0} ist vom falschen Typ: Programmabbruch!"
err_compatib   = "---Strukturen der vorherigen Ergebnisdateien sind nicht kompatibel. Programmabbruch!"
err_no_files   = "---keine Dateien angegeben. Programmabbruch!"
warn_no_ini    = "---Warnung: zaehlen_ini.py nicht gefunden"
