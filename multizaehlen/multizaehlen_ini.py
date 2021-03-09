#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# multizaehlen_ini.py

# (C) Günter Partosch 2018-2021

# Stand: 2018-08-17
#        2020-07-27
#        2020-08-02 (Voreinstellung geändert)
#        2020-08-15 (Ausgabe-Strings)
#        2020-08-27 (Struktur für Programmversion und Programmdatum vereinheitlicht)
#        2020-08-27 (ini-Datei kann robust geladen werden)

# Abhängigkeiten:
# multizaehlen_ini.py
# + wird in multizaehlen.py geladen

# globale Parameter
# -------------------------------------------------------------------
# do not touch

menu_multizaehlen_ini_date  = "2021-03-06"  
menu_multizaehlen_ini_vers  = "1.1.12"
menu_multizaehlen_date      = "2020-08-27" # menu_multizaehlen.py
menu_multizaehlen_vers      = "1.2.10"     # menu_multizaehlen.py
multizaehlen_ini_date       = "2020-08-26" # multizaehlen_ini

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
language               = "de"

rndg                   = 3

# Ausgabe-Strings
# ===================================================================

# Programm-Parameter, global                                              # global program parameters
# -------------------------------------------------------------------
# can be changed
main_caption_text  = "Vergleichendes Auszählen von Texten"
prg_name_text      = "multizaehlen.py"
prg_author_text    = "Günter Partosch"
author_email_text  = "Guenter.Partosch@hrz.uni-giessen.de"
author_institution = "Justus-Liebig-Universität Gießen, Hochschulrechenzentrum"

# Argparse (x)                                                            # argparse
# -------------------------------------------------------------------
# can be changed
files_text     = "zu verarbeitende Dateien (*.plk)"                       # Specify input files [*.pkl]
files_anz_text = "Beschränkung der Dateien-Zahl (*.plk) mit Zeichenkette"
sort1_text     = "1. Sortierung [a+|a-|A+|A-]"                            # Specify 1st sorting (a+|a-|A+|A-)
sort2_text     = "2. Sortierung [L+|L-|F+|F-|D+|D-]"                      # Specify 2nd sorting (L+|L-|F+|F-)
out_text       = "Ausgabedatei"                                           # Specify name of the output file
template_text  = "Beschränkung auf bestimmte Wort-Muster (Muster)"        # limitation by specified word templates
lengths_text   = "Beschränkung auf bestimmte Wortlängen"                  # limitation by specified word lengths
rank_text      = "Beschränkung auf bestimmte Rangfolge"                   # limitation by specified ranks
freq_text      = "Beschränkung auf bestimmte Worthäufigkeiten"            # limitation by specified word frequencies
version_text   = "Version des Programms ausgeben"                         # Show version of the program and exit
autor_text     = "Autor des Programms ausgeben"                           # Show author of the program and exit
fd_text        = "Worthäufigkeiten-Verteilung berechnen"                  # Show distribution of word frequencies
ld_text        = "Wortlängen-Verteilung berechnen"                        # Show distribution of word lengths
sd_text        = "Trennzeichen-Verteilung berechnen"                      # Show distribution of separator characters
cd_text        = "Zeichen-Verteilung berechnen"                           # Show distribution of characters
language_text  = "Spracheinstellung"
argp_pos_par   = 'Positionsparameter'                                     # Positional parameters
argp_opt_par   = 'Optionale Parameter'                                    # Optional parameters
argp_default   = 'Voreinstellung'                                         # Default

# Kopf, allgemein                                                         # header, general
# -------------------------------------------------------------------     # max width: 43
# can be changed
head_content   = "Inhalt"                                                 # Contents
head_prg_name  = "Name des Programms"                                     # Name of the program
head_prg_vers  = "Version des Programms"                                  # Version of the program
head_prg_date  = "Bearbeitungsdatum"                                      # Date of last changes
prg_author     = "Autor des Programms"                                    # Author of the program
author_email   = "E-Mail-Adresse"                                         # Author's eMail address
author_inst    = "Institution"                                            # Author's institution
res_pre_ld     = "Ergebnisse (Längenverteilung vor dem Filtern)"          # Results (distribution of lengths before filtering)
res_pre_fd     = "Ergebnisse (Häufigkeitsverteilung vor dem Filtern)"     # Results (distribution of frequencies before filtering)
res_pre_cd     = "Ergebnisse (Zeichenverteilung vor dem Filtern)"         # Results (distribution of characters before filtering)
res_pre_sd     = "Ergebnisse (Trennzeichenverteilung vor dem Filtern)"    # Results (distribution of separators before filtering)
head_prg_para  = "Programm-Parameter"                                     # parameters of the program
head_result    = "Ergebnisse"                                             # Results
head_summary   = "Zusammenfassung"                                        # Summary

# Kopf, Programmparameter                                                 # header, program parameters
# -------------------------------------------------------------------     # max width: 57
# can be changed
sub_caption    = "Programm-Parameter"                                     # Program parameters
prg_call       = "Programm-Aufruf"                                        # Program call

# Kopf, Legende                                                           # header, table legend
# -------------------------------------------------------------------
# can be changed
caption_leg    = "Ergebnisse"                                             # Results
leg_rank       = "Rangfolge"                                              # Sequence of ranks (sequential number)
leg_str_len    = "Länge der Zeichenkette"                                 # Length of string
leg_string     = "Zeichenkette"                                           # String
leg_str_freq   = "Häufigkeit der Zeichenkette in allen Dateien"           # Frequency of thnis string in all input files
leg_acc_freq   = "akk. Häufigkeit der Zeichenkette"                       # Accumulated frequency of this string
leg_file_nr    = "Zahl der Dateien mit dieser Zeichenkette"               # Number of input files with this string
leg_in_file    = "Eingabedatei"                                           # Name of input file

# Ausgabe, Zusammenfassung                                                # output, summary
# -------------------------------------------------------------------     # max width: 42
# can be changed
result_summ    = "Zusammenfassung"                                        # Summary                       
res_token_pre  = "Zahl der Tokens (vor dem Filtern)"                      # Number of tokens (before filtering)
res_types_pre  = "Zahl der Types (vor dem Filtern)"                       # Number of types (before filtering)
res_ratio_pre  = "Verhältnis Types/Tokens (vor dem Filtern)"              # Ratio types/tokens (before filtering)
res_token_post = "Zahl der Tokens (nach dem Filtern)"                     # Number of tokens (after filtering)
res_types_post = "Zahl der Types (nach dem Filtern)"                      # Number of types (after filtering)
res_ratio_post = "Verhältnis Types/Tokens (nach dem Filtern)"             # Ratio types/tokens (after filtering)
types_pre_post = "Verhältnis Types (nach/vor Filtern)"                    # Ratio types (after/before filtering)
token_pre_post = "Verhältnis Tokens (nach/vor Filtern)"                   # Ratio tokens (after/before filtering                                  )

# Ausgabe, Längenverteilung                                               # output, distribution word lengths
# -------------------------------------------------------------------
# can be changed
caption_ld     = "Ergebnisse (Längenverteilung vor dem Filtern)"          # Results (distribution of lengths before filtering)
ld_hdr_nr      = "laufende Nummer"                                        # sequential number
ld_hdr_length  = "Länge"                                                  # Length
ld_hdr__word_nr= "Anzahl der Wörter mit dieser Länge über alle Dateien"   # Number of words with this length in all files
ld_hdr_files_nr= "Zahl der Dateien mit Wörter dieser Länge"               # Number of files with words with this length
ld_hdr_infile  = "Eingabedatei"                                           # Name of input file
ld_summary_sum = "Summen:"                                                # Sum:
ld_modus       = "Modus:"                                                 # Modus:
ld_at          = "bei:"                                                   # at:
ld_wa_short    = "gMW"                                                    # wa
ld_wa_long     = "(gMW = gewichteter Mittelwert)"                         # (wa = weighted average)
ld_min_length  = "kleinste Länge"                                         # Minimal length
ld_max_length  = "größte Länge"                                           # Maximal length

# Ausgabe, Häufigkeitsverteilung                                          # output, distribution of frequencies
# -------------------------------------------------------------------
# can be changed
caption_fd     = "Ergebnisse (Häufigkeitsverteilung vor dem Filtern)"     # Results (distribution of frequencies before filtering) 
fd_hdr_nr      = ld_hdr_nr
fd_hdr_freq    = "Häufigkeit"                                             # Frequency
fd_hdr_freq_nr = "Anzahl der Wörter mit dieser Häufigkeit über alle Dateien" # Number of words with this frequency in all files
fd_hdr_files_nr= "Zahl der Dateien mit Wörter dieser Häufigkeit"          # Number of files with words with this frequency
fd_hdr_infile  = ld_hdr_infile
fd_summary_sum = ld_summary_sum
fd_modus       = ld_modus
fd_at          = ld_at
fd_min_freq    = "kleinste Häufigkeit"                                    # Minimal frequency
fd_max_freq    = "größte Häufigkeit"                                      # Maximal frequency

# Ausgabe, Zeichenverteilung                                              # output, distribution of characters
# -------------------------------------------------------------------
# can be changed
caption_cd     = "Ergebnisse (Zeichenverteilung vor dem Filtern)"         # Results (distribution of characters before filtering)
cd_hdr_nr      = ld_hdr_nr
cd_hdr_char    = "Zeichen"                                                # Character
cd_hdr_hex     = "zugehöriger Hex-Code"                                   # Associated hex code
cd_hdr_char_nr = "Anzahl dieses Zeichens über alle Dateien"               # Number of thnis character in all files
cd_hdr_files_nr= "Zahl der Dateien mit diesem Zeichen"                    # Number of files with this character
cd_hdr_infile  = ld_hdr_infile
cd_summary_sum = ld_summary_sum
cd_modus       = ld_modus
cd_at          = ld_at

# Ausgabe, Trennzeichenverteilung                                        # output, distribution of separators
# -------------------------------------------------------------------
# can be changed
caption_sd     = "Ergebnisse (Trennzeichenverteilung vor dem Filtern)"   # Results (distribution of separators before filtering)
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
# do not touch
err_out        = "---Ausgabedatei {0} kann nicht geöffnet werden. Programmabbruch!"   # ---Output file {0} could not be opened; program exits!
err_pkl_open   = "---Datei {0} kann nicht geöffnet werden. Programmabbruch!"          # ---File {0} could not be opened; program exits!
err_type       = "---Datei {0} ist vom falschen Typ: Programmabbruch!"                # ---File {0} has not the correct type; program exits!
err_compatib   = "---Strukturen der vorherigen Ergebnisdateien sind nicht kompatibel. Programmabbruch!" # Structures of the former result files are not compatible; program exits!
err_no_files   = "---keine Dateien angegeben. Programmabbruch!"                       # ---No files specified; program exits!
warn_no_ini    = "---Warnung: zaehlen_ini.py nicht gefunden"                          # ---Warning: zaehlen_ini.py not found

