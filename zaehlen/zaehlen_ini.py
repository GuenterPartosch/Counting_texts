# zaehlen-ini.py: Initialisierung, Vorbesetzungen
# Stand: 2018-08-17
#        2020-08-02 (Voreinstellungen geändert)
#        2020-08-12 (Ausgabe-Strings hierher verlagert) 

# Abhängigkeiten
# zaehlen_ini.py
# + wird von menue_zaehlen.py als Modul geladen
# + wird von zaehlen.py als Modul geladen

# ----------------------------------------------
# Voreinstellungen

in_name                = "./in.txt"
out_name               = "./out.txt"
stop_name              = ""
go_name                = ""
separator              = """[\s.,;:!?<>()\[\]{}"'…—–“”„‘’`+»«‹–›0-9|/=_%*$&autor_institution]+"""
word_template          = """^.+$"""
p_lengths              = "1,100"
p_frequency            = "1,12000"
p_rank                 = "1,50000"
sort_first             = "a+"
sort_second            = ""
frequency_distribution = False
length_distribution    = False
separator_distribution = False
character_distribution = False

integer_breite         = 7  # Ausgabebreite für Integer
integer_breite_kl      = 3  # Ausgabebreite für kleine Integer
string_breite          = 3  # voreingestellte Ausgabebreite für Strings
string_breite_la       = 43 # Länge von Eingabeaufforderungen
real_breite            = 6  # Ausgabebreite für Reals
rndg                   = 2  # Zahl der Nachkommastellen für Reals/Floats

# Ausgabe-Strings
# ====================================================
# allgemeine Angaben
# -----------------------------------------------------
main_caption_text      = "Auszählen von Texten"
prg_name_text          = "Name des Programms"            # Länge: 21
prg_version_text       = "Version des Programms"
prg_datum_text         = "Bearbeitungsdatum"
prg_author_text        = "Autor des Programms"
email                  = "E-Mail-Adresse"
institution            = "Institution"

# argparse
# -----------------------------------------------------
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

argp_pos_par  = 'Positionsparameter'
argp_opt_par  = 'Optionale Parameter'
argp_default  = 'Voreinstellung'


# Programmparameter
# -----------------------------------------------------
caption_parameter_text = "Programm-Parameter"
prg_call_text          = "Programm-Aufruf"                           # Länge: 39
in_file_text           = "Eingabedatei"
sep_text               = "Wort-Trennzeichen (Muster)"
stop_file_text         = "Datei mit Stop-Wörter"
go_file_text           = "Datei mit Go-Wörter"
sort1_text             = "1. Sortierung (a+|a-|A+|A-)"
sort2_text             = "2. Sortierung (L+|L-|F+|F-)"
out_file_text          = "Ausgabe-Datei"
limit_template_text    = "Beschränkung auf best. Wort-Muster"
limit_length_text      = "Beschränkung auf best. Wortlängen"
limit_rangs_text       = "Beschränkung auf best. Rangfolge"
limit_frequency_text   = "Beschränkung auf best. Worthäufigkeiten"
act_freq_dist_text     = "Worthäufigkeiten-Verteilung aktiviert"
act_length__dist_text  = "Wortlängen-Verteilung aktiviert"
act_sep_dist_text      = "Trennzeichen-Verteilung aktiviert"
act_char_dist_text     = "Zeichen-Verteilung aktiviert"

# interaktive Eingabe
# -----------------------------------------------------
interac_in_text        = "Eingabedatei(en) festlegen"
interac_sep_text       = "Wort-Trennzeichen (Muster) spezifizieren"
interac_stop_text      = "Datei mit Stop-Wörter spezifizieren"
interac_go_text        = "Datei mit Go-Wörter spezifizieren"
interac_sort1_text     = "1. Sortierung (a+|a-|A+|A-) spezifizieren"
interac_sort2_text     = "2. Sortierung (L+|L-|F+|F-) spezifizieren"
interac_out_text       = "Ausgabedatei(en) festlegen"
interac_template_text  = "Beschränkung auf best. Wort-Muster (Muster)"
interac_lengths_text   = "Beschränkung auf best. Wortlängen"
interac_rank_text      = "Beschränkung auf best. Rangfolge"
interac_freq_text      = "Beschränkung auf best. Worthäufigkeiten"
interac_version_text   = "Version des Programms ausgeben und Exit"
interac_autor_text     = "Autor des Programms ausgeben und Exit"
interac_text_prompt    = ": "
interac_fd_text        = "Worthäufigkeiten-Verteilung ausgeben"
interac_ld_text        = "Wortlängen-Verteilung ausgeben"
interac_sd_text        = "Trennzeichen-Verteilung ausgeben"
interac_cd_text        = "Zeichen-Verteilung ausgeben"

caption_interac_text   = "Programm {0} zum Zählen von Wörtern in einer Datei"
subcap_interac_text    = "Voreingestellte bzw. übergebene bzw. neue Werte"
interac_task           = "Aufgabe"
interac_pre            = "bisheriger Wert"
interac_post           = "neuer Wert"
interac_legend_text    = """Werte neu setzen:
    <return> bisherigen Wert übernehmen
    OK       weitere Eingabe beenden und Programm starten
    sonst    neuer Wert
    <strg D> Programm-Abbruch bzw.
    <strg C> Programm-Abbruch
    """

# Tabellenlegende
# -----------------------------------------------------
caption_res_words_text = "Ergebnisse (Wörter in der Auswahl)"
res_rangs_text         = "(1) Rangfolge"
res_length_text        = "(2) Länge der Zeichenkette"
res_strings_text       = "(3) Zeichenkette"
res_abs_freq_text      = "(4) abs. Häufigkeit"
res_rel_freq_text      = "(5) proz. Häufigkeit [%]"
res_abs_acc_freq_text  = "(6) akk. Häufigkeit"
res_rel_acc_freq_text  = "(7) proz. akk. Häufigkeit [%]"

# normale Ausgabe
# -----------------------------------------------------
caption_summary_text   = "Ergebnisse (Zusammenfassung der Auswahl)" # breite: 33
summary_lines_text     = "Zeilen"
summary_chars_tot_text = "Zeichen, insgesamt"
summary_chars_act_text = "Zeichen, berücksichtigt"
summary_token_tot_text = "Wörter (Tokens), Gesamttext"
summary_token_sel_text = "Wörter (Tokens), Auswahl"
summary_types_tot_text = "Wörter (Types), Gesamttext"
summary_types_sel_text = "Wörter (Types), Auswahl"
summary_ratio_tot_text = "Verh. (Types/Tokens), Gesamttext"
summary_ratio_sel_text = "Verh. (Types/Tokens), Auswahl"
corresponds            = "entspricht "

# normale Ausgabe, Abspann
# -----------------------------------------------------
summary_sum = "Summe"

# Wortlängen-Verteilung
# -----------------------------------------------------
ld_caption_total       = "Ergebnisse (Verteilung der Wortlängen im Gesamttext)"
ld_caption_selected    = "Ergebnisse (Verteilung der Wortlängen nach dem Filtern)"
ld_length_number       = "<länge>:<anzahl>"
ld_min_length          = "minimale Länge:"
ld_max_length          = "maximale Länge:"
ld_modus               = "Modus der Längenverteilung:"
ld_mean                = "Durchschnittliche Länge:"

# Frequenz-Verteilung
# -----------------------------------------------------
fd_caption_total       = "Ergebnisse (Verteilung der Worthäufigkeiten im Gesamttext)"
fd_caption_selected    = "Ergebnisse (Verteilung der Worthäufigkeiten nach dem Filtern)"
fd_freq_number         = "<häufigkeit>:<anzahl>"
fd_min_freq            = "minimale Häufigkeit:"
fd_freq_max            = "maximale Häufigkeit:"
fd_modus               = "Modus der Häufigkeitenverteilung:"


# Zeichen-Verteilung
# -----------------------------------------------------
cd_caption_total       = "Ergebnisse (Verteilung der Zeichenhäufigkeiten im Gesamttext)"
cd_caption_selected    = "Ergebnisse (Verteilung der Zeichenhäufigkeiten nach dem Filtern)"
cd_char_code_number    = "<zeichen>:<code>:<anzahl>"
cd_modus               = "Modus der Zeichenverteilung:"

# Trennzeichen-Verteilung
# -----------------------------------------------------
sd_caption_total       = "Ergebnisse (Verteilung der Trennzeichenhäufigkeiten im Gesamttext)"
sd_sep_number          = "<trennzeichen>:<anzahl>"
sd_modus               = "Modus der Trennzeichenverteilung:"

# Fehlermeldungen + Warnungen
# -----------------------------------------------------
err_in                 = "---Eingabedatei {0} kann nicht geöffnet werden. Programmabbruch"
err_out                = "---Ausgabedatei {0} kann nicht geöffnet werden. Programmabbruch"
warn_GoStop            = "---Warnung: Go-Datei und Stop-Datei gleichzeitig angegeben; ignoriert"
warn_Stop              = "---Warnung: Stop-Datei {0} kann nicht geöffnet werden. Ignoriert."
warn_Go                = "---Warnung: Go-Datei {0} kann nicht geöffnet werden. Ignoriert."
warn_ini               = "---Warnung: zaehlen_ini.py nicht gefunden; Voreinstellungen genommen"
warn_Aa                = '---Warnung: nur "", "A+", "A-", "a+", "a-" zulässig; Voreinstellung genommen'
warn_LF                = '---Warnung; nur "", "L+", "L-", "F+", "F-" zulässig;  Voreinstellung genommen'
warn_cd_filter         = "---Verteilung der Zeichenhäufigkeiten nach dem Filtern nicht verfügbar"
warn_fd                = "---Verteilung der Worthäufigkeiten im Gesamttext nicht verfügbar"
warn_fd_filter         = "---Verteilung der Worthäufigkeiten nach dem Filtern nicht verfügbar"
warn_ld_filter         = "---Verteilung der Wortlängen nach dem Filtern nicht verfügbar"
