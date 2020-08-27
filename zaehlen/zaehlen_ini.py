# zaehlen-ini.py: Initialisierung, Vorbesetzungen
# Stand: 2018-08-17
#        2020-08-02 (Voreinstellungen geändert)
#        2020-08-12 (Ausgabe-Strings hierher verlagert)
#        2020-08-20 (Ausgabe-Strings bearbeitet)
#        2020-08-25 (vereinheitlichte Konstruktion von Programm-Datum und Programm-Version)

# Abhängigkeiten
# zaehlen_ini.py
# + wird von menue_zaehlen.py geladen
# + wird von zaehlen.py geladen

zaehlen_ini_date       = "2020-08-25"
zaehlen_vers           = "2.14.3"                             # zaehlen.py:     Version
zaehlen_date           = "2020-08-25 "                        # zaehlen.py:     Datum der letzten Änderung

# Voreinstellungen                                            # defaults
# ---------------------------------------------- 
in_name                = "./in.txt"                           # -i
out_name               = "./out.txt"                          # -o
stop_name              = ""                                   # -S
go_name                = ""                                   # -G
separator              = """[\s.,;:!?<>()\[\]{}"'…—–“”„‘’`+»«‹–›0-9|/=_%*$]+"""
word_template          = """^.+$"""
p_lengths              = "1,100"
p_frequency            = "1,12000"
p_rank                 = "1,50000"
sort_first             = "a+"                                 # -s1
sort_second            = ""                                   # -s2
frequency_distribution = False                                # -fd
length_distribution    = False                                # -ld
separator_distribution = False                                # -sd
character_distribution = False                                # -cd
silent_mode            = False                                # -sm
language               = "de"                                 # -la

integer_breite         = 7                                    # Ausgabebreite für Integer
integer_breite_kl      = 3                                    # Ausgabebreite für kleine Integer
string_breite          = 3                                    # voreingestellte Ausgabebreite für Strings
string_breite_la       = 43                                   # Länge von Eingabeaufforderungen
real_breite            = 6                                    # Ausgabebreite für Reals
rndg                   = 2                                    # Zahl der Nachkommastellen für Reals/Floats

# Ausgabe-Strings                                             # output strings
# ====================================================
# allgemeine Angaben                                          # general ettings
# -----------------------------------------------------       #   max width: 21
# do not touch

program_author         = "Günter Partosch"
author_email           = "Guenter.Partosch@hrz.uni-giessen.de"
author_institution     = "Justus-Liebig-Universität Gießen, Hochschulrechenzentrum"

main_caption_text      = "Auszählen von Texten"               # Counting the words in text files
prg_name_text          = "Name des Programms"                 # Name of the program
prg_version_text       = "Version des Programms"              # Version of the program
prg_datum_text         = "Bearbeitungsdatum"                  # Date of last changes
prg_author_text        = "Autor des Programms"                # Author of the program
email                  = "E-Mail-Adresse"                     # eMail address
institution            = "Institution"                        # Institution

# argparse                                                    # argparse
# -----------------------------------------------------
in_text       = "Eingabedatei festlegen"                               # Specify input file
sep_text      = "Wort-Trennzeichen (Muster) spezifizieren"             # Specify separator characters
stop_text     = "Datei mit Stop-Wörter spezifizieren"                  # Specify file with stop words
go_text       = "Datei mit Go-Wörter spezifizieren"                    # Specify file with go words
sort1_text    = "1. Sortierung (a+|a-|A+|A-) spezifizieren"            # Specify 1st sorting (a+|a-|A+|A-)
sort2_text    = "2. Sortierung (L+|L-|F+|F-) spezifizieren"            # Specify 2nd sorting (L+|L-|F+|F-)
out_text      = "Ausgabedatei festlegen"                               # Specify name of the output file
template_text = "Beschränkung auf best. Wort-Muster (Muster)"          # Limitation by specified word templates
lengths_text  = "Beschränkung auf best. Wortlängen"                    # Limitation by specified word lengths
rank_text     = "Beschränkung auf best. Rangfolge"                     # Limitation by specified ranks
freq_text     = "Beschränkung auf best. Worthäufigkeiten"              # Limitation by specified word frequencies
version_text  = "Version des Programms ausgeben und Exit"              # Show version of the program and exit
autor_text    = "Autor des Programms ausgeben und Exit"                # Show author of the program and exit
fd_text       = "Worthäufigkeiten-Verteilung ausgeben"                 # Show distribution of word frequencies
ld_text       = "Wortlängen-Verteilung ausgeben"                       # Show distribution of word lengths
sd_text       = "Trennzeichen-Verteilung ausgeben"                     # Show distribution of separatot characters
cd_text       = "Zeichen-Verteilung ausgeben"                          # Show distribution of characters
sm_text       = "'Still'-Modus"                                        # Silent mode
language_text = "Spracheinstellung (noch nicht verfügbar)"             # Language (not available yet)

argp_pos_par  = 'Positionsparameter'                                   # Ppositional parameters
argp_opt_par  = 'Optionale Parameter'                                  # Optional parameters
argp_default  = 'Voreinstellung'                                       # Default


# Programmparameter                                                    # Parameters for the program
# -----------------------------------------------------                #   max width: 39
caption_parameter_text = "Programm-Parameter"                          # Parameter of the program
prg_call_text          = "Programm-Aufruf"                             # Program call
in_file_text           = "Eingabedatei"                                # Name for input file
sep_text               = "Wort-Trennzeichen (Muster)"                  # Template for word separators
stop_file_text         = "Datei mit Stop-Wörter"                       # File with stop words
go_file_text           = "Datei mit Go-Wörter"                         # File with go words
sort1_text             = "1. Sortierung (a+|a-|A+|A-)"                 # 1st sorting (a+|a-|A+|A-)
sort2_text             = "2. Sortierung (L+|L-|F+|F-)"                 # 2nd sorting (L+|L-|F+|F-)
out_file_text          = "Ausgabe-Datei"                               # Name for output file
limit_template_text    = "Beschränkung auf best. Wort-Muster"          # Limitation by specified word templates
limit_length_text      = "Beschränkung auf best. Wortlängen"           # Limitation by specified word lengths
limit_rangs_text       = "Beschränkung auf best. Rangfolge"            # Limitation by specified ranks
limit_frequency_text   = "Beschränkung auf best. Worthäufigkeiten"     # Limitation by specified word frequencies
act_freq_dist_text     = "Worthäufigkeiten-Verteilung aktiviert"       # Distribution of word frequencies activated
act_length__dist_text  = "Wortlängen-Verteilung aktiviert"             # Distribution of word lengths activated
act_sep_dist_text      = "Trennzeichen-Verteilung aktiviert"           # Distribution of word separators activateds
act_char_dist_text     = "Zeichen-Verteilung aktiviert"                # Distribution of characters activated

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
caption_res_words_text = "Ergebnisse (Wörter in der Auswahl)"          # Results (words in the selection)
res_rangs_text         = "Rangfolge"                                   # rank sequence
res_length_text        = "Länge der Zeichenkette"                      # length of the "word"
res_strings_text       = "Zeichenkette"                                # "word"
res_abs_freq_text      = "abs. Häufigkeit"                             # Absolute frequency
res_rel_freq_text      = "proz. Häufigkeit [%]"                        # relative frequency [%]
res_abs_acc_freq_text  = "akk. Häufigkeit"                             # Accumulated frequency
res_rel_acc_freq_text  = "proz. akk. Häufigkeit [%]"                   # Accumulated relative frequency [%]

# normale Ausgabe                                                      # Results, normal
# -----------------------------------------------------                #     max width: 33
caption_summary_text   = "Ergebnisse (Zusammenfassung der Auswahl)"    # Results (summary of selection)
summary_lines_text     = "Zeilen"                                      # Lines
summary_chars_tot_text = "Zeichen, insgesamt"                          # Characters, total
summary_chars_act_text = "Zeichen, berücksichtigt"                     # Characters, taken into account
summary_token_tot_text = "Wörter (Tokens), Gesamttext"                 # Words (tokens), total
summary_token_sel_text = "Wörter (Tokens), Auswahl"                    # Words (tokens) in the selection
summary_types_tot_text = "Wörter (Types), Gesamttext"                  # Words (types), total
summary_types_sel_text = "Wörter (Types), Auswahl"                     # Words (types) in the selection
summary_ratio_tot_text = "Verh. (Types/Tokens), Gesamttext"            # Ratio (types/tokens), total
summary_ratio_sel_text = "Verh. (Types/Tokens), Auswahl"               # Ratio (types/tokens) in the selection
corresponds            = "entspricht "                                 # corresponds

# normale Ausgabe, Abspann                                             # normal result, end
# -----------------------------------------------------
summary_sum            = "Summe"                                       # sum

# Wortlängen-Verteilung                                                                      # word length distribution
# -----------------------------------------------------
ld_caption_total       = "Ergebnisse (Verteilung der Wortlängen im Gesamttext)"              # Results (distribution of the word lengths in the whole text)
ld_caption_selected    = "Ergebnisse (Verteilung der Wortlängen nach dem Filtern)"           # Results (distribution of the word lengths after filtering)
ld_length_number       = "<länge>:<anzahl>"                                                  # <length>:<number>
ld_min_length          = "minimale Länge:"                                                   # Minimal length:
ld_max_length          = "maximale Länge:"                                                   # Maximal length:
ld_modus               = "Modus der Längenverteilung:"                                       # Modus of length distribution:
ld_mean                = "Durchschnittliche Länge:"                                          # Average of lengths:

# Frequenz-Verteilung                                                                        # frequency distribution
# -----------------------------------------------------
fd_caption_total       = "Ergebnisse (Verteilung der Worthäufigkeiten im Gesamttext)"        # Results (distribution of the word frequencies in the whole text)
fd_caption_selected    = "Ergebnisse (Verteilung der Worthäufigkeiten nach dem Filtern)"     # Results (distribution of the word frequencies after filtering)
fd_freq_number         = "<häufigkeit>:<anzahl>"                                             # <frequency>:<number>
fd_min_freq            = "minimale Häufigkeit:"                                              # Minimal frequency:
fd_freq_max            = "maximale Häufigkeit:"                                              # Maximal frequency:
fd_modus               = "Modus der Häufigkeitenverteilung:"                                 # Modus of frequency:

# Zeichen-Verteilung                                                                         # character distribution
# -----------------------------------------------------
cd_caption_total       = "Ergebnisse (Verteilung der Zeichenhäufigkeiten im Gesamttext)"     # Results (distribution of the word frequencies in the whole text)
cd_caption_selected    = "Ergebnisse (Verteilung der Zeichenhäufigkeiten nach dem Filtern)"  # Results (distribution of the word frequencies after filtering)
cd_char_code_number    = "<zeichen>:<code>:<anzahl>"                                         # <character>:<code>:<number>
cd_modus               = "Modus der Zeichenverteilung:"                                      # Modus of character distribution:

# Trennzeichen-Verteilung                                                                    # separator distribution
# -----------------------------------------------------
sd_caption_total       = "Ergebnisse (Verteilung der Trennzeichenhäufigkeiten im Gesamttext)"# Results (distribution of the word frequencies after filtering)
sd_sep_number          = "<trennzeichen>:<anzahl>"                                           # <separator>:<number>
sd_modus               = "Modus der Trennzeichenverteilung:"                                 # Modus of separator distribution

# Fehlermeldungen + Warnungen                                                                            # error messages and warnings
# -----------------------------------------------------
err_in                 = "---Eingabedatei {0} kann nicht geöffnet werden. Programmabbruch"               # ---input file {0} could not ber opened. program exit
err_out                = "---Ausgabedatei {0} kann nicht geöffnet werden. Programmabbruch"               # ---output file {0} could not ber opened. program exit
warn_GoStop            = "---Warnung: Go-Datei und Stop-Datei gleichzeitig angegeben; ignoriert"         # ---warning: stop file and go file simultaneously specifoed; ignored
warn_Stop              = "---Warnung: Stop-Datei {0} kann nicht geöffnet werden. Ignoriert."             # ---warning: file with stop words {0} could not be opened; ignored
warn_Go                = "---Warnung: Go-Datei {0} kann nicht geöffnet werden. Ignoriert."               # ---warning: file with go words {0} could not be opened; ignored
warn_ini               = "---Warnung: Datei zaehlen_ini.py nicht gefunden; Voreinstellungen genommen"    # ---warning: file zaehlen_ini.py not found; defaults taken
warn_Aa                = '---Warnung: nur "", "A+", "A-", "a+", "a-" zulässig; Voreinstellung genommen'  # ---warning: only "", "A+", "A-", "a+", "a-" permitted; defaults taken
warn_LF                = '---Warnung: nur "", "L+", "L-", "F+", "F-" zulässig;  Voreinstellung genommen' # ---warning: only "", "L+", "L-", "F+", "F-" permitted; defaults taken
warn_cd_filter         = "---Verteilung der Zeichenhäufigkeiten nach dem Filtern nicht verfügbar"        # ---distribution opf characters after filtering not available
warn_fd                = "---Verteilung der Worthäufigkeiten im Gesamttext nicht verfügbar"              # ---distribution of word frequencies in the whole text filtering not available
warn_fd_filter         = "---Verteilung der Worthäufigkeiten nach dem Filtern nicht verfügbar"           # ---distribution of word frequencies after filtering not available
warn_ld_filter         = "---Verteilung der Wortlängen nach dem Filtern nicht verfügbar"                 # ---distribution opf word lengths after filtering not available
