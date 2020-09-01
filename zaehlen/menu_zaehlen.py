#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# menu_zaehlen.py

# (C) Günter Partosch 2018-2020

# Stand: 2018-08-20
# Stand: 2020-07-22
# Stand: 2020-08-07
# Stand: 2020-08-08 (Ausgabe-Strings parametrisiert)
# Stand: 2020-08-09 (Überprüfung der Eingabewerte)
# Stand: 2020-08-16 (Ausgabe-Strings überarbeitet)
# Stand: 2020-08-23 (ini-Dateien entkoppelt)
# Stand: 2020-09-24 (ini-Dateien robust geladen)
# Stand: 2020-08-24 (argparse; Vorarbeiten für die Parameter -sm, -la)
# Stand: 2020-08-24 (silent_mode per Parameter -sm verfügbar)
# Stand: 2020-08-25 (silent mode im Menü)
# Stand: 2020-08-25 (vereinheitlichte Konstruktion von Programm-Datum und Programm-Version)
# Stand: 2020-08-30 (Sprachunterstützung für Englisch)

# Vorhaben:
# + Fehlerbehandlung bei unzulässigen Eingaben (x)
# + unterschiedliche ini-Dateien für verschiedene Sprachen (?)
# + Parameter für andere Sprachen: -la (x)
# + generell: andere ini-Dateien erlauben
# + Laden der ini-Datei robuster gestalten (x)
# + strings ggf. umschreiben mit Platzhalter (x)
# + verbose/silent-Modus (x)
# + Unterschied zwischen Abbrechen/Beenden
# + tkinter listbox
# + einheitliches Konzept für Programnamen und -versionen (x)
# + wenn mit -sm aufgerufen ==> eintragen in Menü


# =======================================================================
##m_z_datum = "2020-07-22"
menu_zaehlen_date = "2018-08-30"             # Datum der letzten Änderung

# -----------------------------------------------------------------------
# Abhängigkeiten
# menu_zaehlen.py
# + lädt menu_zaehlen_ini.py als Modul
# + ruft zaehlen.py auf

# =======================================================================
# Importe

import argparse                                # Parser für Aufruf-Parameter 
import sys                                     # wird für path verwendet
import subprocess                              # Starten/Beobachten von Subprozessen
from tkinter import *                          # Tk
from tkinter.filedialog import askopenfilenames# Dateinamen erfragen in Tk
from tkinter.filedialog import askopenfilename # einen Dateinamen erfragen in Tk
from tkinter.messagebox import *               # Ausgabe in Message-Boxen
import re                                      # reguläre Ausdrücke

# -----------------------------------------------------------------------
try:                                           # Initialisierungsdatei des Programms zaehlen.py
    exec(open("zaehlen_ini.py", encoding="utf-8", mode="r").read())
except FileNotFoundError:
    err_ini_text           = "--- Warnung: Initialisierungsdatei {0} kann nicht geladen werden; --> Voreinstellungen genommen"
    print(err_ini_text.format("zaehlen_ini.py"))

    zaehlen_ini_date       = "2020-08-30"
    zaehlen_vers           = "2.15.1"
    zaehlen_date           = "2020-08-30"

    in_name                = "./in.txt"                           
    out_name               = "./out.txt"                          
    stop_name              = ""                                   
    go_name                = ""                                   
    separator              = """[\s.,;:!?<>()\[\]{}"'…—–“”„‘’`+»«‹–›0-9|/=_%*$]+"""
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
    silent_mode            = False                                
    language               = "de"                                 

    integer_breite         = 7                                    
    integer_breite_kl      = 3                                    
    string_breite          = 3                                    
    string_breite_la       = 43                                   
    real_breite            = 6                                    
    rndg                   = 2                                    

    program_author         = "Günter Partosch"
    author_email           = "Guenter.Partosch@hrz.uni-giessen.de"
    author_institution     = "Justus-Liebig-Universität Gießen, Hochschulrechenzentrum"

    main_caption_text      = "Auszählen von Texten"               
    prg_name_text          = "Name des Programms"                 
    prg_version_text       = "Version des Programms"              
    prg_datum_text         = "Bearbeitungsdatum"                  
    prg_author_text        = "Autor des Programms"                
    email                  = "E-Mail-Adresse"                     
    institution            = "Institution"                        

    in_text       = "Eingabedatei festlegen"                               
    sep_text      = "Wort-Trennzeichen (Muster) spezifizieren"             
    stop_text     = "Datei mit Stop-Wörter spezifizieren"                  
    go_text       = "Datei mit Go-Wörter spezifizieren"                    
    sort1_text    = "1. Sortierung (a+|a-|A+|A-) spezifizieren"            
    sort2_text    = "2. Sortierung (L+|L-|F+|F-) spezifizieren"            
    out_text      = "Ausgabedatei festlegen"                               
    template_text = "Beschränkung auf best. Wort-Muster (Muster)"          
    lengths_text  = "Beschränkung auf best. Wortlängen"                    
    rank_text     = "Beschränkung auf best. Rangfolge"                     
    freq_text     = "Beschränkung auf best. Worthäufigkeiten"              
    version_text  = "Version des Programms ausgeben und Exit"              
    autor_text    = "Autor des Programms ausgeben und Exit"                
    fd_text       = "Worthäufigkeiten-Verteilung ausgeben"                 
    ld_text       = "Wortlängen-Verteilung ausgeben"                       
    sd_text       = "Trennzeichen-Verteilung ausgeben"                     
    cd_text       = "Zeichen-Verteilung ausgeben"                          
    sm_text       = "'Still'-Modus"                                        
    language_text = "Spracheinstellung (noch nicht verfügbar)"             

    argp_pos_par  = 'Positionsparameter'                                   
    argp_opt_par  = 'Optionale Parameter'                                  
    argp_default  = 'Voreinstellung'                                       

    caption_parameter_text = "Programm-Parameter"                          
    prg_call_text          = "Programm-Aufruf"                             
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

    text_prompt            = ": "                                          
    interac_text_prompt    = ": "
    interac_in_text        = "Eingabedatei festlegen"                      
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
    interac_fd_text        = "Worthäufigkeiten-Verteilung ausgeben"        
    interac_ld_text        = "Wortlängen-Verteilung ausgeben"              
    interac_sd_text        = "Trennzeichen-Verteilung ausgeben"            
    interac_cd_text        = "Zeichen-Verteilung ausgeben"                 

    caption_interac_text   = "Programm {0} zum Zählen von Wörtern in einer Datei" 
    subcap_interac_text    = "voreingestellte bzw. übergebene bzw. neue Werte"    
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

    caption_res_words_text = "Ergebnisse (Wörter in der Auswahl)"          
    res_rangs_text         = "Rangfolge"                                   
    res_length_text        = "Länge der Zeichenkette"                      
    res_strings_text       = "Zeichenkette"                                
    res_abs_freq_text      = "abs. Häufigkeit"                             
    res_rel_freq_text      = "proz. Häufigkeit [%]"                        
    res_abs_acc_freq_text  = "akk. Häufigkeit"                             
    res_rel_acc_freq_text  = "proz. akk. Häufigkeit [%]"                   

    caption_summary_text   = "Ergebnisse (Zusammenfassung der Auswahl)"    
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

    summary_sum            = "Summe"                                       

    ld_caption_total       = "Ergebnisse (Verteilung der Wortlängen im Gesamttext)"              
    ld_caption_selected    = "Ergebnisse (Verteilung der Wortlängen nach dem Filtern)"           
    ld_length_number       = "<länge>:<anzahl>"                                                  
    ld_min_length          = "minimale Länge            : "                                       
    ld_max_length          = "maximale Länge            : "                                       
    ld_modus               = "Modus der Längenverteilung: '{0}' mit {1} Vorkommen"
    ld_mean                = "Durchschnittliche Länge   : "                                       

    fd_caption_total       = "Ergebnisse (Verteilung der Worthäufigkeiten im Gesamttext)"        
    fd_caption_selected    = "Ergebnisse (Verteilung der Worthäufigkeiten nach dem Filtern)"     
    fd_freq_number         = "<häufigkeit>:<anzahl>"                                             
    fd_min_freq            = "minimale Häufigkeit            : "                                              
    fd_freq_max            = "maximale Häufigkeit            : "                                              
    fd_modus               = "Modus der Häufigkeitsverteilung: '{0}' mit {1} Vorkommen"          

    cd_caption_total       = "Ergebnisse (Verteilung der Zeichenhäufigkeiten im Gesamttext)"     
    cd_caption_selected    = "Ergebnisse (Verteilung der Zeichenhäufigkeiten nach dem Filtern)"  
    cd_char_code_number    = "<zeichen>:<code>:<anzahl>"                                         
    cd_modus               = "Modus der Zeichen-Verteilung: '{0}' mit {1} Vorkommen"             

    sd_caption_total       = "Ergebnisse (Verteilung der Trennzeichenhäufigkeiten im Gesamttext)"
    sd_sep_number          = "<trennzeichen>:<anzahl>"                                           
    sd_modus               = "Modus der Trennzeichen-Verteilung: '{0}' mit {1} Vorkommen"        

    err_in                 = "---Eingabedatei {0} kann nicht geöffnet werden. Programmabbruch"               
    err_out                = "---Ausgabedatei {0} kann nicht geöffnet werden. Programmabbruch"               
    warn_GoStop            = "---Warnung: Go-Datei und Stop-Datei gleichzeitig angegeben; ignoriert"         
    warn_Stop              = "---Warnung: Stop-Datei {0} kann nicht geöffnet werden. Ignoriert."             
    warn_Go                = "---Warnung: Go-Datei {0} kann nicht geöffnet werden. Ignoriert."               
    warn_ini               = "---Warnung: Datei zaehlen_ini.py nicht gefunden; Voreinstellungen genommen"    
    warn_Aa                = '---Warnung: nur "", "A+", "A-", "a+", "a-" zulässig; Voreinstellung genommen'  
    warn_LF                = '---Warnung: nur "", "L+", "L-", "F+", "F-" zulässig;  Voreinstellung genommen' 
    warn_cd_filter         = "---Verteilung der Zeichenhäufigkeiten nach dem Filtern nicht verfügbar"        
    warn_fd                = "---Verteilung der Worthäufigkeiten im Gesamttext nicht verfügbar"              
    warn_fd_filter         = "---Verteilung der Worthäufigkeiten nach dem Filtern nicht verfügbar"           
    warn_ld_filter         = "---Verteilung der Wortlängen nach dem Filtern nicht verfügbar"                 

# -----------------------------------------------------------------------
try:                                           # Initialisierungsdatei des Programms menu_zaehlen.py
    exec(open("menu_zaehlen_ini.py", encoding="utf-8", mode="r").read())
except FileNotFoundError:
    err_ini_text             = "--- Warnung: Initialisierungsdatei {0} kann nicht geladen werden; --> Voreinstellungen genommen"
    print(err_ini_text.format("menu_zaehlen_ini.py"))

    instverz                 = '.'                                  
    remote_program_name      = "zaehlen.py"
    program_name             = "menu_zaehlen.py"                    

    menu_zaehlen_ini_date    = "2020-08-30"                         

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

    msg1                     = "Eingabefelder/Checkboxen"                         
    msg2                     = "Schaltflächen"                                    
    msg3                     = "Erläuterungen"                                    
    msg4                     = "Version(en)"                                      
    tuple_text               = 'Tupel mit {0} Datei(en)'                          
    error_text               = "Fehler"                                           
    execution_text           = "Bearbeitung"                                      
    end_text                 = "Programm menu_zaehlen.py beendet"                 
    call_text                = "Aufruf"                                           

    programmtitle            = "Auszählen eines Textes; Eingabemenü für das Programm "

    E0_text                  = "Eingabedatei(en)"                                 
    E1_text                  = "Wort-Trennzeichen [Muster]"                       
    E2_text                  = "Datei mit Stop-Wörter"                            
    E3_text                  = "Datei mit Go-Wörter"                              
    E4_text                  = "1. (alph.) Sortierung [a+|a-|A+|A-]"              
    E5_text                  = "2. Sortierung [L+|L-|F+|F-]"                      
    E6_text                  = "Ausgabedatei(en)"                                 
    E7_text                  = "Beschränkung auf bestimmte Wörter [Muster]"       
    E8_text                  = "Beschränkung auf bestimmte Wortlängen"            
    E9_text                  = "Beschränkung auf bestimmte Rangfolge"             
    E10_text                 = "Beschränkung auf best. Worthäufigkeiten"          

    C0_text                  = "Worthäufigkeiten-Verteilung berechnen"            
    C1_text                  = "Wortlängen-Verteilung berechnen"                  
    C2_text                  = "Trennzeichen-Verteilung berechnen"                
    C3_text                  = "Zeichen-Verteilung berechnen"                     
    C4_text                  = "'Stille' Verarbeitung"                            

    B0_text                  = 'Durchsuchen... [Eingabedatei(en)]'                
    B1_text                  = 'Durchsuchen... [Stop-Datei]'                      
    B2_text                  = 'Durchsuchen... [Go-Datei]'                        
    B4_text                  = 'Zurücksetzen'                                     
    B5_text                  = 'Löschen'                                          
    B6_text                  = 'Start'                                            
    B7_text                  = 'Beenden'                                          
    B8_text                  = 'Eingabefelder/Checkboxen'                         
    B9_text                  = 'Schaltflächen'                                    
    B10_text                 = 'Erläuterungen'                                    
    B11_text                 = 'Version(en)'                                      

    fields_boxes_text        = "Es stehen folgende Eingabefelder/Checkboxen zur Verfügung (Voreinstellung in runden Klammern):"
                                                                                  
    buttons_text             = "Es gibt folgende Schaltflächen:"                  
    for_parameter            = "für Parameter"                                    
    calls_text               = "ruft"                                             

    err_ini_text             = "--- Warnung: Initialisierungsdatei {0} kann nicht geladen werden; --> Voreinstellungen genommen"
    err_value_text           = "--- Fehler '{1}' bei '{0}'; --> Voreinstellung genommen"
    err1_file_text           = "--- Datei '{1}' bei '{0}' kann nicht geöffnet werden; --> Voreinstellung genommen"
    err2_file_text           = "--- Datei '{1}' bei '{0}' kann nicht geöffnet werden; --> korrigieren + Neustart"

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

    help_text1 = programmtitle + remote_program_name + ':\n\n'
    help_text1 += fields_boxes_text + "\n\n"
    for f in range(len(conf)):
        help_text1 += str(conf[f][0]) + " (" + str(conf[f][1]) + "); {0} ".format(for_parameter) + conf[f][2] + "\n"

    help_text2 = buttons_text + "\n\n"
    for f in range(len(button_conf)):
        help_text2 += str(button_conf[f][0]) + "; {0} '".format(calls_text) + str(button_conf[f][1]) + "'\n"

    help_text3 = comments_text

    version_msg_text = version_help_text.format(zaehlen_vers, zaehlen_date, menu_zaehlen_date, menu_zaehlen_ini_date, zaehlen_ini_date)


# =======================================================================
# argparse

parser = argparse.ArgumentParser(description = programmtitle + " [" + program_name + "; " +
                                     "Version: " + menu_zaehlen_date + "]")
parser._positionals.title = argp_pos_par
parser._optionals.title   = argp_opt_par
parser.add_argument("-a", "--author",
                    help = autor_text,
                    action = 'version',
                    version = program_author + " (" + author_email + ", " + author_institution + ")") 
parser.add_argument("-la", "--language",
                    help = language_text + "; {0}: %(default)s".format(argp_default),
                    choices = ["de", "en"],
                    dest = "language",
                    default = language) 
parser.add_argument("-sm", "--silent_mode",
                    help = sm_text + "; {0}: %(default)s".format(argp_default),
                    action = "store_true",
                    default = silent_mode)

args                   = parser.parse_args()   # Aufruf-Parameter
silent_mode            = args.silent_mode
language               = args.language


# =======================================================================
# Sprachmodule

if language == "de":
    pass
elif language == "en":
    try:                                           # Initialisierungsdatei des Programms menu_zaehlen.py
        exec(open("zaehlen_ini_en.py", encoding="utf-8", mode="r").read())
    except FileNotFoundError:
        err_ini_text             = "--- Warnung: Initialisierungsdatei {0} kann nicht geladen werden; --> Voreinstellungen genommen"
        print(err_ini_text.format("zaehlen_ini_en.py"))

    try:                                           # Initialisierungsdatei des Programms menu_zaehlen.py
        exec(open("menu_zaehlen_ini_en.py", encoding="utf-8", mode="r").read())
    except FileNotFoundError:
        err_ini_text             = "--- Warnung: Initialisierungsdatei {0} kann nicht geladen werden; --> Voreinstellungen genommen"
        print(err_ini_text.format("menu_zaehlen_ini_en.py"))
else:
    pass

# =======================================================================
# Initialisierungen

##cd      = sys.path[0]                          # enthält akt. Verzeichnis
##cd      = cd.replace("\\", sl)                 # normiert auf "/" als Trennstrich
sl          = "/"                              # Schrägstrich als Verzeichnistrennzeichen
dir_sep     = """[\/]"""                       # Trennzeichen für Verzeichnisnamen
ul          = "_"                              # in create_filenames benutzt
p           = re.compile(dir_sep)              # regulärer Ausdruck zum Auftrennen von Verzeichnisnamen
no_call     = False                            # Flag: der Aufruf soll nicht durchgeführt werden
set_in_file = False                            # Flag: Name der Eingabedatei Eingabedatei wurde per Auswahl festgelegt

# Hilfsvariable
leer        = ""
name_in     = []

# Sequenzen anlegen
L           = []                               # Labels
E           = []                               # Eingabefelder (Entry)
B           = []                               # Knöpfe (Button)
V           = []                               # Statusvariable für Checkboxen
C           = []                               # Checkboxen

# Sequenzen initialisieren
for f in range(len(conf)):                     # Schleife über alle Labels, Eingabefelder, ass. Variablen und Checkboxen 
    L.append(None)
    E.append(None)
    V.append(None)
    C.append(None)

# Sequenz B (für Buttons) initialisieren
for f in range(len(button_conf)):              # Schleife über alle Schaltflächen
    B.append(None)

    
# =======================================================================
# einige Methoden

# -----------------------------------------------------------------------
def create_filename(nummer, basis):
    """generiert aus nummer und basis einen Dateinamen."""
    l = p.split(basis)
    if (len(l) == 1):
        aus = str(nummer) + ul + basis
    else:
        aus = l[0]
        l[len(l)-1] = str(nummer) + ul + l[len(l)-1]
        for f in range(1,len(l)):
            aus = aus + sl + l[f]
    return aus

# -----------------------------------------------------------------------
def check(parameter, value, type):
    """checks compatibility of parameter and value."""

    global no_call, set_in_file
    
    result = True
    if parameter in ["-s1"]:                                            # Parameter -s1
        if value in ["a+", "a-", "A+", "A-"]:
            pass                                                        # -- alles OK
        else:
            showerror(title=error_text, message = err_value_text.format(parameter, value), icon = ERROR)
            result = False
    elif parameter in ["-s2"]:                                          # Parameter -s2
        if value in ["L+", "L-", "F+", "F-"]:
            pass                                                        # -- alles OK
        else:
            showerror(title=error_text, message = err_value_text.format(parameter, value), icon = ERROR)
            result = False
    elif parameter in ["-l", "-r", "-f"]:                               # Parameter -l, -r, -f
        n, m = eval("(" + str(value) + ")")
        if isinstance(n, int) and isinstance(m, int) and (n <= m):
            pass                                                        # -- alles OK
        else:
            showerror(title=error_text, message = err_value_text.format(parameter, value), icon = ERROR)
            result = False
    elif parameter in ["-G", "-S"]:                                     # Parameter -S, -G
        try:
            tmp = open(value, encoding="utf-8", mode="r")               # -- Versuch, Datei zu öffnen
            tmp.close()
        except FileNotFoundError:                                       # -- nicht OK
            showerror(title=error_text, message = err1_file_text.format(parameter, value), icon = ERROR)
            no_call = True                                              # -- kein Aufruf später
            result  = False
    elif parameter in ["-o"]:                                           # Parameter -o
        try:
            tmp = open(value, encoding="utf-8", mode="w")               # -- Versuch, Datei zu öffnen
            tmp.close()
        except FileNotFoundError:                                       # -- nicht OK
            showerror(title=error_text, message = err1_file_text.format(parameter, value), icon = ERROR)
            no_call = True                                              # -- kein Aufruf später
            result  = False
    elif parameter in ["-i"]:                                           # Parameter -i
        if set_in_file:
            pass
        else:
            try:
                tmp = open(value, encoding="utf-8", mode="r")           # -- Versuch, Datei zu öffnen
                tmp.close()
            except FileNotFoundError:                                   # -- nicht OK
                showerror(title=error_text, message = err2_file_text.format(parameter, value), icon = ERROR)
                no_call = True                                          # -- kein Aufruf später
                result  = False
    return result

# -----------------------------------------------------------------------
def help1():
    """gibt einen Hilfetext aus."""
    showinfo(msg1, help_text1)

# -----------------------------------------------------------------------
def help2():
    """gibt einen Hilfetext aus."""
    showinfo(msg2, help_text2)

# -----------------------------------------------------------------------
def help3():
    """gibt einen Hilfetext aus."""
    showinfo(msg3, help_text3)
    
# -----------------------------------------------------------------------
def init_entry_fields():
    """initialisiert Labels und Eingabefelder."""
    for f in range(len(conf)): # Schleife über alle Eingabefelder, LabelVariablen und Checkboxens, 
        L[f] = Label(mm, text=conf[f][0])
        L[f].grid(row=f)
        if conf[f][3] != 4:
            E[f] = Entry(mm)
            E[f].insert(10, conf[f][1])
            E[f].grid(row=f, column=1, sticky=W, pady=5)
        else:
            V[f] = IntVar()
            C[f] = Checkbutton(mm, text="", variable=V[f])
            C[f].grid(row=f, column=1, sticky=W, pady=0)

# -----------------------------------------------------------------------
def show_entry_fields():
    """zeigt die Werte der Eingabefelder an."""
    for f in range(len(conf)): # Schleife über alle Eingabefelder
        if (conf[f][3] != 4):
            print(conf[f][0], ":", E[f].get())
        else:
            print(conf[f][0], ":", V[f].get())
    
# -----------------------------------------------------------------------
def clear_entry_fields():
    """löscht die Inhalte der Eingabefelder."""
    for f in range(len(conf)): # Schleife über alle Eingabefelder und Variablen
        if (conf[f][3] != 4):
            E[f].delete(0, END)
        else:
            V[f] = 0

# -----------------------------------------------------------------------
def ask_in_file():
    """erfragt die/den Namen der Eingabedatei(en) und trägt sie/ihn in Eingabefeld ein."""
    
    global name_in, set_in_file
    
    name_in = []
    name_in = askopenfilenames()
    E[0]    = Entry(mm)
    E[0].insert(10, tuple_text.format(str(len(name_in))))
    set_in_file = True
    E[0].grid(row=0, column=1)

# -----------------------------------------------------------------------
def ask_go_file():
    """erfragt den Namen der Go-Datei und trägt ihn in Eingabefeld ein."""
    name = askopenfilename()
    E[3] = Entry(mm)
    E[3].insert(10, name)
    E[3].grid(row=3, column=1)

# -----------------------------------------------------------------------
def ask_stop_file():
    """erfragt Namen der Stop-Datei und trägt ihn in Eingabefeld ein."""
    name = askopenfilename()
    E[2] = Entry(mm)
    E[2].insert(10, name)
    E[2].grid(row=2, column=1)

# -----------------------------------------------------------------------
def ask_out_file():
    """erfragt Namen der Ausgabedatei und trägt ihn in Eingabefeld ein."""
    name = askopenfilename()
    name = name.replace(cd,".")
    E[6] = Entry(mm)
    E[6].insert(10, name)
    E[6].grid(row=2, column=1)
    
# -----------------------------------------------------------------------
def reset_entry_fields():
    """setzt Eingabefelder auf Voreinstellungen zurück."""
    for f in range(len(conf)):                                   # Schleife über alle Eingabefelder
        if conf[f][3] != 4:
            E[f] = Entry(mm)
            E[f].insert(10, conf[f][1])
            E[f].grid(row=f, column=1)
        else:
            V[f] = IntVar()
            C[f] = Checkbutton(mm, text="", variable=V[f])
            C[f].grid(row=f, column=1, sticky=W, pady=0)
    
# -----------------------------------------------------------------------
def start():
    """wertet die Eingabefelder aus und startet zaehlen.py."""

# conf : Sequenz von 4-elementigen Listen:
# (Label, assoziierte Variable, assoziierter Aufruf-Parameter, Parameter-Typ)
#   + Label: Text, der das Feld kennzeichnet
#   + assoziierte Variable: Vorbesetzung des Feldes (aus zaehlen_ini.py)
#   + assoziierter Aufruf-Parameter: Aufruf-Parameter, den zaehlen.py erwartet
#   + Parameter-Typ: Hinweis, wie Eingaben weiter bearbeitet werden
#     1: Parameter erwartet einen Wert; spezielle Behandlung bei leerer Eingabe
#     2: Parameter erwartet einen Wert; wird normal weiter verarbeitet
#     3: Parameter erwartet keinen Wert
#     4: wie 3; zusätzlich wird eine Checkbox abgefragt

##    aufruf   = ["python", instverz + sl + remote_program_name]
    aufruf      = ["python", remote_program_name]
    optionen    = ""
    silent_mode = args.silent_mode

    for f in range(len(conf)):                                  # Schleife über alle Eingabefelder/Checkboxen
        typ     = conf[f][3]
        zwi_val = ""
        par     = conf[f][2]
        default = conf[f][1]
        if (typ == 2):                                          # (2) Parameter erwartet einen Wert; wird normal weiter verarbeitet; -s, -S, -G, -s1, -s2, -l, -r, -f
            zwi = E[f].get()
            if (zwi not in [leer, default]):
                if check(par, zwi, typ):
                    aufruf.append(par); aufruf.append(zwi)
        elif (typ == 3):                                        # (3) Parameter erwartet keinen Wert
            zwi = E[f].get()
            if (zwi not in ["0", leer]):
                aufruf.append(par)
        elif (typ == 1):                                        # (1) Parameter erwartet einen Wert; spezielle Behandlung bei leerer Eingabe; -i, -o
            zwi = E[f].get()
            if zwi != leer:
                if check(par, zwi, typ):
                    aufruf.append(par); aufruf.append(zwi)
        elif (typ == 4):                                        # (4) wie 3; zusätzlich wird eine Checkbox abgefragt; -fd, -ld, -sd, -cd
            zwi = V[f].get()
            if (zwi == 1):
                if par in ["-sm", "--silent_mode"]:
                    silent_mode = True
                else:
                    aufruf.append(par)
        else:
            pass

    if language == "de":                                        # Sprachparameter für Aufruf
        pass
    elif language == "en":
        aufruf.append("-la");
        aufruf.append(language)
    else:
        pass

    if (len(name_in) == 0):                                     # kein Name für Eingabedatei
        if not no_call:
            if not silent_mode:
                showinfo(title=call_text, message = aufruf)
            x = subprocess.Popen(aufruf, stderr=subprocess.PIPE, universal_newlines=True)
            errormess = x.stderr.read()
            if (len(errormess) > 0):
                showerror(title=error_text, message=errormess, icon=ERROR)

    for f in range(len(name_in)):                               # Schleife über alle Eingabedateien
        aufruf_i = aufruf[:]

        for g in range(len(aufruf_i)):                          # -- Schleife über alle Parameter
            if (aufruf_i[g] == "-i"):
                g_i = g                                         # -- Position von -i merken
            if (aufruf_i[g] == "-o"):
                g_o = g                                         # -- Position von -o merken
        aufruf_i[g_i + 1] = name_in[f]
        aufruf_i[g_o + 1] = create_filename(f, aufruf[g_o + 1]) # -- Name für Ausgabedatei(en) generieren
        if not silent_mode:
            showinfo(title=call_text, message = aufruf_i)
        x = subprocess.Popen(aufruf_i, stderr=subprocess.PIPE, universal_newlines=True)
        errormess = x.stderr.read()
        if (len(errormess) > 0):
            showerror(title=error_text, message=errormess, icon=ERROR)
    showinfo(title=execution_text, message = end_text)

# -----------------------------------------------------------------------
def init_buttons():
    """legt Buttons an und initialisiert sie."""
    for f in range(len(button_conf)):                           # Schleife über alle Schaltflächen
        zwi0      = button_conf[f][0]
        zwi1      = button_conf[f][1]
        zwi2      = str(button_conf[f][2])
        zwi3      = str(button_conf[f][3])
        b_string1 = "Button(mm, text = '" + zwi0 + "', command = " + zwi1 + ")\n"
        b_string2 = "B[" + str(f) + "].grid(row = " + zwi2 + ", column = " + zwi3 + ", sticky=W, pady=0)\n"
        B[f]      = eval(b_string1)
        eval(b_string2)

# -----------------------------------------------------------------------
def version():
    """gibt Versionsdaten aus."""
    showinfo(msg4, version_msg_text)


# =======================================================================
mm = Tk()
mm.title(programmtitle + remote_program_name)

init_entry_fields()
init_buttons()
mainloop( )

