#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# zaehlen-ini_en.py


# (C) Günter Partosch 2016-2020
# Initialisierung, Vorbesetzungen

# Stand: 2020-08-27 (erste Version)

# Abhängigkeiten
# + wird ggf. von menu_zaehlen.py geladen
# + wird ggf. von zaehlen.py geladen

zaehlen_ini_en_date    = "2020-08-28"

# Ausgabe-Strings                                             # output strings
# ====================================================
# allgemeine Angaben                                          # general ettings
# -----------------------------------------------------       #   max width: 21
# do not touch

main_caption_text      = "Counting the words in text files"
prg_name_text          = "Name of the program"
prg_version_text       = "Version of program"
prg_datum_text         = "Date of last changes"
prg_author_text        = "Author of the program"
email                  = "eMail address"
institution            = "Institution"

# argparse                                                    # argparse
# -----------------------------------------------------
in_text       = "Specify input file"
sep_text      = "Specify separator characters"
stop_text     = "Specify file with stop words"
go_text       = "Specify file with go words"
sort1_text    = "Specify 1st sorting (a+|a-|A+|A-)"
sort2_text    = "Specify 2nd sorting (L+|L-|F+|F-)"
out_text      = "Specify name of the output file"
template_text = "Limitation by specified word templates"
lengths_text  = "Limitation by specified word lengths"
rank_text     = "Limitation by specified ranks"
freq_text     = "Limitation by specified word frequencies"
version_text  = "Show version of the program and exit"
autor_text    = "Show author of the program and exit"
fd_text       = "Show distribution of word frequencies"
ld_text       = "Show distribution of word lengths"
sd_text       = "Show distribution of separatot characters"
cd_text       = "Show distribution of characters"
sm_text       = "Silent mode"
language_text = "Language (not available yet)"

argp_pos_par  = "Ppositional parameters"
argp_opt_par  = "Optional parameters"
argp_default  = "Default"


# Programmparameter                                                    # Parameters for the program
# -----------------------------------------------------                #   max width: 39
caption_parameter_text = "Parameter of the program"
prg_call_text          = "Program call"
in_file_text           = "Name for input file"
sep_text               = "Template for word separators"
stop_file_text         = "File with stop words"
go_file_text           = "File with go words"
sort1_text             = "1st sorting (a+|a-|A+|A-)"
sort2_text             = "2nd sorting (L+|L-|F+|F-)"
out_file_text          = "Name for output file"
limit_template_text    = "Limitated by specified word templates"
limit_length_text      = "Limitated by specified word lengths"
limit_rangs_text       = "Limitated by specified ranks"
limit_frequency_text   = "Limitated by specified word frequencies"
act_freq_dist_text     = "Distribution of word frequencies activ."
act_length__dist_text  = "Distribution of word lengths activated"
act_sep_dist_text      = "Distribution of word separators activ."
act_char_dist_text     = "Distribution of characters activated"

# interaktive Eingabe                                                  # interactive input
# -----------------------------------------------------
text_prompt            = ": "                                          # text prompt
interac_text_prompt    = ": "
interac_in_text        = "Eingabedatei festlegen"                      # Specify input file
interac_sep_text       = "Wort-Trennzeichen (Muster) spezifizieren"    # Specify separator characters (template)
interac_stop_text      = "Datei mit Stop-Wörter spezifizieren"         # Specify file with stop words
interac_go_text        = "Datei mit Go-Wörter spezifizieren"           # Specify file with go words
interac_sort1_text     = "1. Sortierung (a+|a-|A+|A-) spezifizieren"   # Specify 1st sorting (a+|a-|A+|A-)
interac_sort2_text     = "2. Sortierung (L+|L-|F+|F-) spezifizieren"   # Specify 2nd sorting (L+|L-|F+|F-)
interac_out_text       = "Ausgabedatei(en) festlegen"                  # Specify output file
interac_template_text  = "Beschränkung auf best. Wort-Muster (Muster)" # Limitation by specified word templates
interac_lengths_text   = "Beschränkung auf best. Wortlängen"           # Limitation by specified word lengths
interac_rank_text      = "Beschränkung auf best. Rangfolge"            # Limitation by specified ranks
interac_freq_text      = "Beschränkung auf best. Worthäufigkeiten"     # Limitation by specified word frequencies
interac_version_text   = "Version des Programms ausgeben und Exit"     # Show version of the program and exit
interac_autor_text     = "Autor des Programms ausgeben und Exit"       # Show author of the program and exit
interac_fd_text        = "Worthäufigkeiten-Verteilung ausgeben"        # Show distribution of word frequencies
interac_ld_text        = "Wortlängen-Verteilung ausgeben"              # Show word length distribution
interac_sd_text        = "Trennzeichen-Verteilung ausgeben"            # Show separator distribution
interac_cd_text        = "Zeichen-Verteilung ausgeben"                 # Show character distribution

caption_interac_text   = "Programm {0} zum Zählen von Wörtern in einer Datei" # Program {0} for word couting in a text file
subcap_interac_text    = "voreingestellte bzw. übergebene bzw. neue Werte"    # Default values a/o transferred values
interac_task           = "Aufgabe"                                     # Task
interac_pre            = "bisheriger Wert"                             # Old value
interac_post           = "neuer Wert"                                  # New value
interac_legend_text    = """Werte neu setzen:
    <return> bisherigen Wert übernehmen
    OK       weitere Eingabe beenden und Programm starten
    sonst    neuer Wert
    <strg D> Programm-Abbruch bzw.
    <strg C> Programm-Abbruch
    """                                                                # Renew values:
# renew values:
# <return> take old values
# OK       finish further input andf start program
# else     new value
# <ctrl D> terminate program
# <ctrl C> terminate program

# Tabellenlegende                                                      # legend for table header
# -----------------------------------------------------
caption_res_words_text = "Results (words in the selection)"
res_rangs_text         = "rank sequence"
res_length_text        = "length of the 'word'"
res_strings_text       = "'word'"
res_abs_freq_text      = "Absolute frequency"
res_rel_freq_text      = "relative frequency [%]"
res_abs_acc_freq_text  = "Accumulated frequency"
res_rel_acc_freq_text  = "Accumulated relative frequency [%]"

# normale Ausgabe                                                      # Results, normal
# -----------------------------------------------------                #     max width: 33
caption_summary_text   = "Results (summary of selection)"
summary_lines_text     = "Lines"
summary_chars_tot_text = "Characters, total"
summary_chars_act_text = "Characters, taken into account"
summary_token_tot_text = "Words (tokens), total"
summary_token_sel_text = "Words (tokens) in the selection"
summary_types_tot_text = "Words (types), total"
summary_types_sel_text = "Words (types) in the selection"
summary_ratio_tot_text = "Ratio (types/tokens), total"
summary_ratio_sel_text = "Ratio (types/tokens), selection"
corresponds            = "corresponds"

# normale Ausgabe, Abspann                                             # normal result, end
# -----------------------------------------------------
summary_sum            = "sum"

# Wortlängen-Verteilung                                                                      # word length distribution
# -----------------------------------------------------
ld_caption_total       = "Results (distribution of the word lengths in the whole text)"
ld_caption_selected    = "Results (distribution of the word lengths after filtering)"
ld_length_number       = "<length>:<number>"
ld_min_length          = "Minimal length               : "
ld_max_length          = "Maximal length               : "
ld_modus               = "Modus of length dcistribution: '{0}' with {1} cases"
ld_mean                = "Average of lengths           : "

# Frequenz-Verteilung                                                                        # frequency distribution
# -----------------------------------------------------
fd_caption_total       = "Results (distribution of the word frequencies in the whole text)"
fd_caption_selected    = "Results (distribution of the word frequencies after filtering)"
fd_freq_number         = "<frequency>:<number>"
fd_min_freq            = "Minimal frequency              : "
fd_freq_max            = "Maximal frequency              : "
fd_modus               = "Modus of frequency distribution: '{0}' with {1} cases"

# Zeichen-Verteilung                                                                         # character distribution
# -----------------------------------------------------
cd_caption_total       = "Results (distribution of the character distribution in the whole text)"
cd_caption_selected    = "Results (distribution of the character distribution after filtering)"
cd_char_code_number    = "<character>:<code>:<number>"
cd_modus               = "Modus of character distribution: '{0}' with {1} cases"

# Trennzeichen-Verteilung                                                                    # separator distribution
# -----------------------------------------------------
sd_caption_total       = "Results (distribution of the separator after filtering)"
sd_sep_number          = "<separator>:<number>"
sd_modus               = "Modus of separator distribution: '{0}' with {1} cases"

# Fehlermeldungen + Warnungen                                                                            # error messages and warnings
# -----------------------------------------------------
err_in                 = "---input file {0} could not ber opened. program exit"
err_out                = "---output file {0} could not ber opened. program exit"
warn_GoStop            = "---warning: stop file and go file simultaneously specifoed; ignored"
warn_Stop              = "---warning: file with stop words {0} could not be opened; ignored"
warn_Go                = "---warning: file with go words {0} could not be opened; ignored"
warn_ini               = "---warning: file zaehlen_ini.py not found; defaults taken"
warn_Aa                = '---warning: only "", "A+", "A-", "a+", "a-" permitted; defaults taken'
warn_LF                = '---warning: only "", "L+", "L-", "F+", "F-" permitted; defaults taken'
warn_cd_filter         = "---distribution opf characters after filtering not available"
warn_fd                = "---distribution of word frequencies in the whole text filtering not available"
warn_fd_filter         = "---distribution of word frequencies after filtering not available"
warn_ld_filter         = "---distribution opf word lengths after filtering not available"
