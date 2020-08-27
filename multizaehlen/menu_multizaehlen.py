#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# (C) Günter Partosch 2017-2018

# menu_multizaehlen.py

# 1.0.0: 2017-02-19: Anfang, aus menu_zaehlen.py entwickelt
# 1.1.0: 2017-02-19: erstmals funktionsfähig
# 1.2.0: 2017-07-18: Erweiterung und neues Konzept
# 1.2.8: 2020-08-19: Ausgabe-Strings in ini-Datei verlagert
# 1.2.9: 2020-08-26: ini-Dateien robust geladen
# 1.2.10: 2020-08-27: Konstrukt für Programm-Versionen und -Daten vereinheitlicht

menu_multizaehlen_date = "2020-08-27"
menu_multizaehlen_vers = "1.2.10"

# -----------------------------------------------------------------------
# Abhängigkeiten
# menu_multizaehlen.py
# + ruft multizaehlen.py auf
# + ruft menu_multizaehlen_ini.py 

# -----------------------------------------------------------------------
# Module importieren

import sys                                     # wird für path benötigt
import subprocess                              # Starten/Beobachten von Subprozessen
from tkinter import *                          # Tk
from tkinter.filedialog import askopenfilenames# Dateinamen erfragen in Tk
from tkinter.filedialog import askopenfilename # einen Dateinamen erfragen in Tk
from tkinter.messagebox import *               # Ausgabe in Message-Boxen
##from copy import deepcopy                      # "tiefes" Kopieren von Tuples und Listen
import re                                      # reguläre Ausdrücke


# -----------------------------------------------------------------------
# ini-Dateien laden

try:                                            # Konfiguration/Initialisierung von multizaehlen.py einlesen
    exec(open("multizaehlen_ini.py", encoding="utf-8", mode="r").read())
except FileNotFoundError:                       # falls Fehler: lokal Programm-Parameter und -Variablen initialisieren
    err_ini_text             = "--- Warnung: Initialisierungsdatei {0} kann nicht geladen werden; --> Voreinstellungen genommen"
    print(err_ini_text.format("menu_zaehlen_ini.py"))

    menu_multizaehlen_ini_date  = "2020-08-27"  
    menu_multizaehlen_date      = "2020-08-27" 
    menu_multizaehlen_vers      = "1.2.10"     
    multizaehlen_ini_date       = "2020-08-26" 

    in_name                = ""
    out_name               = "./mz_out.txt"   
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

    main_caption_text  = "Vergleichendes Auszählen von Texten"
    prg_name_text      = "multizaehlen.py"
    prg_author_text    = "Günter Partosch"
    author_email_text  = "Guenter.Partosch@hrz.uni-giessen.de"
    author_institution = "Justus-Liebig-Universität Gießen, Hochschulrechenzentrum"

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

    head_content   = "Inhalt"                                                 
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

    sub_caption    = "Programm-Parameter"                                     
    prg_call       = "Programm-Aufruf"                                        

    caption_leg    = "Ergebnisse"                                             
    leg_rank       = "Rangfolge"                                              
    leg_str_len    = "Länge der Zeichenkette"                                 
    leg_string     = "Zeichenkette"                                           
    leg_str_freq   = "Häufigkeit der Zeichenkette in allen Dateien"           
    leg_acc_freq   = "akk. Häufigkeit der Zeichenkette"                       
    leg_file_nr    = "Zahl der Dateien mit dieser Zeichenkette"               
    leg_in_file    = "Eingabedatei"                                           

    result_summ    = "Zusammenfassung"                                        
    res_token_pre  = "Zahl der Tokens (vor dem Filtern)"                      
    res_types_pre  = "Zahl der Types (vor dem Filtern)"                       
    res_ratio_pre  = "Verhältnis Types/Tokens (vor dem Filtern)"              
    res_token_post = "Zahl der Tokens (nach dem Filtern)"                     
    res_types_post = "Zahl der Types (nach dem Filtern)"                      
    res_ratio_post = "Verhältnis Types/Tokens (nach dem Filtern)"             
    types_pre_post = "Verhältnis Types (nach/vor Filtern)"                    
    token_pre_post = "Verhältnis Tokens (nach/vor Filtern)"                   

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

    err_out        = "---Ausgabedatei {0} kann nicht geöffnet werden. Programmabbruch!"   
    err_pkl_open   = "---Datei {0} kann nicht geöffnet werden. Programmabbruch!"          
    err_type       = "---Datei {0} ist vom falschen Typ: Programmabbruch!"                
    err_compatib   = "---Strukturen der vorherigen Ergebnisdateien sind nicht kompatibel. Programmabbruch!" 
    err_no_files   = "---keine Dateien angegeben. Programmabbruch!"                       
    warn_no_ini    = "---Warnung: zaehlen_ini.py nicht gefunden"                          

try:                                            # Konfiguration/Initialisierung von multizaehlen.py einlesen
    exec(open("menu_multizaehlen_ini.py", encoding="utf-8", mode="r").read())
except FileNotFoundError:                       # falls Fehler: lokal Programm-Parameter und -Variablen initialisieren
    err_ini_text             = "--- Warnung: Initialisierungsdatei {0} kann nicht geladen werden; --> Voreinstellungen genommen"
    print(err_ini_text.format("menu_multizaehlen_ini.py"))

    instverz         = '.'
    program_name     = "multizaehlen.py"
    program_name2    = "zaehlen.py"

    menu_multizaehlen_date       = "2020-08-27" 
    menu_multizaehlen_vers       = "1.2.10"     

    menu_multizaehlen_ini_date   = "2020-08-27" 
    menu_multizaehlen_ini_vers   = "1.1.11"     

    menue_zaehlen_date           = "2018-08-09" 

    menue_zaehlen_ini_date       = "2020-08-12" 

    multizaehlen_date            = "2020-08-26" 
    multizaehlen_vers            = "1.11.2"     

    multizaehlen_ini_date        = "2020-08-26" 

    zaehlen_date                 = "2020-08-25" 
    zaehlen_vers                 = "2.14.3"     

    zaehlen_ini_date             = "2020-08-25" 

    programmtitle                 = "Vergleich von Textauszählungen; Eingabemenü für das Programm "
                                                                            
    msg1                          = "Eingabefelder/Checkboxen"              
    msg2                          = "Schaltflächen"                         
    msg3                          = "Erläuterungen"                         
    msg4                          = "Version(en)"                           
    tuple_text                    = 'Tupel mit {0} Datei(en)'               
    error_text                    = "Fehler"                                
    execution_text                = "Bearbeitung"                           
    end_text                      = "Programm menu_zaehlen beendet"         
    call_text                     = "Aufruf"                                
    pickle_files                  = "Pickle-Dateien"                        
    all_files                     = "Alle Dateien"                          

    B0_text                       = 'Durchsuchen... [Eingabedatei(en)]'     
    B1_text                       = 'Zurücksetzen'                          
    B2_text                       = 'Löschen'                               
    B3_text                       = 'Start'                                 
    B4_text                       = 'Beenden'                               
    B5_text                       = 'Eingabefelder/Checkboxen'              
    B6_text                       = 'Schaltflächen'                         
    B7_text                       = 'Erläuterungen'                         
    B8_text                       = 'Version(en)'                           
                   
    tmp1 = "verarbeitet pkl-Dateien, die durch Aufrufe von"                 
    tmp2 = "erzeugt wurden, weiter"                                         
    tmp3 = "Es gibt folgende Eingabefelder/Checkboxen von"                  
    tmp4 = "(Voreinstellungen jeweils in eckigen Klammern)"                 
    tmp5 = "für Parameter"                                                  
    tmp6 = "Es gibt folgende Schaltflächen"                                 
    tmp7 = "ruft"                                                           

    #

    conf = [
    ("[E0] Eingabedatei(en)",  in_name,               "",   0),
    ("[E1] (-s1) " + sort1_text,     sort_first,            "-s1",2),
    ("[E2] (-s2) " + sort2_text,     sort_second,           "-s2",2),
    ("[E3] (-o) "  + out_text,       out_name,              "-o", 1),
    ("[E4] (-t) "  + template_text,  word_template,         "-t", 2),
    ("[E5] (-l) "  + lengths_text,   p_lengths,             "-l", 2),
    ("[E6] (-r) "  + rank_text,      p_rank,                "-r", 2),
    ("[E7] (-f) "  + freq_text,      p_frequency,           "-f", 2),
    ("[E8] (-fi) " + files_anz_text, p_files,               "-fi",2),
    ("[C0] (-fd) " + fd_text,        frequency_distribution,"-fd",4),
    ("[C1] (-ld) " + ld_text,        length_distribution,   "-ld",4),
    ("[C2] (-sd) " + sd_text,        separator_distribution,"-sd",4),
    ("[C3] (-cd) " + cd_text,        character_distribution,"-cd",4)
    ]

    button_conf =[
    ('[B0] ' + B0_text, "ask_in_file",          0, 2),
    ('[B1] ' + B1_text, "reset_entry_fields",  13, 0),
    ('[B2] ' + B2_text, "clear_entry_fields",  13, 1),
    ('[B3] ' + B3_text, "start",               14, 0),
    ('[B4] ' + B4_text, "mm.destroy",          14, 1),
    ('[B5] ' + B5_text, "hilfe1",              13, 2),
    ('[B6] ' + B6_text, "hilfe2",              13, 3),
    ('[B7] ' + B7_text, "hilfe3",              14, 2),
    ('[B8] ' + B8_text, "version",             14, 3)
    ]

    hilfe_text1 = programmtitle + program_name + ':\n\n'
    hilfe_text1 += "{3}\n(*) {0} {1} {2}".format(tmp1, program_name2, tmp2, program_name) + ".\n\n"
    hilfe_text1 += "{0} {1} {2}".format(tmp3, program_name, tmp4) + ":\n\n"
    for f in range(len(conf)):
        hilfe_text1 += "{0} [{1}]; {2} {3}".format(str(conf[f][0]), str(conf[f][1]), tmp5, conf[f][2]) + "\n"

    hilfe_text2 = tmp6 + ":\n\n"
    for f in range(len(button_conf)): 
        hilfe_text2 += "{0} {1} '{2}'".format(str(button_conf[f][0]), tmp7, str(button_conf[f][1])) + "\n"

    hilfe_text3 = """
    (*) zu [E0] und [E3]: erwartet werden korrekte Namen für Dateien
    (*) zu [E0]: mittels einer Schaltfläche ([B0]) können Dateien (plk-Dateien) ausgewählt werden
    (*) zu [E4]: Erwartet werden korrekte Muster (reguläre Ausdrücke).
    (*) zu [E4]: Muster für zu berücksichtigende Wörter;
        Voreinstellung bedeutet: alle Wörter aus mindestens einem beliebigen Zeichen.
        '^[aeiou]+en$' : nur Wörter, die mit einem kleinen Vokal beginnen und auf "en" enden
    (*) zu [E1] und [E2]: Angaben für Sortierungen; nur die aufgeführten Angaben sind möglich;
        "+" aufsteigend,
        "-" absteigend
    (*) zu [E1]: 1. Sortierung; mögliche Angaben:
        a+/a-: Groß- und Kleinbuchstaben sind eingereiht;
        A+/A-: Groß- und Kleinbuchstaben sind nicht eingereiht
    (*) zu [E2]: 2. Sortierung:
        L+/L-: Sortierung nach Wortlängen;
        F+/F-: Sortierung nach Worthäufigkeiten;
        D+/D-: Sortierung nach Dateizahl
    (*) zu [E5]-[E8]: Beschränkung der Ausgabe:
        + Wortlängen ([E5]),
        + Rangfolgen ([E6]),
        + Worthäufigkeiten ([E7]) und
        + Dateizahl ([E8])
        z.B. bedeutet '2, 100' bei [E7]: alle Wörter, die 2-mal bis 99-mal vorkommen

    (*) zu [B1]-[B4]: Schaltflächen zum Steuern des Programms
    (*) [B1]=setzt alle Eingabefelder auf Voreinstellungen zurück
        [B2]=löscht alle Eingabefelder
        [B3]=startet das Programm mit eingegebenen/ausgewählten Werten
        [B4]=beendet das Programm ohne Berechnung
        [B5]=Ausgabe eines Informationstextes: Eingabefelder/Checkboxen
        [B6]=Ausgabe eines Informationstextes: Schaltflächen
        [B7]=Ausgabe eines Informationstextes: Erläuterungen
        [B8]=Ausgabe eines Informationstextes: Version(en) der beteiligten Programme
    """

    version_text = """
    Aufrufkette
    =======
    menu_multizaehlen.py 
       ---ruft---> menu_multizaehlen_ini.py
       ---ruft---> multizaehlen.py
    multizaehlen.py
       ---ruft---> multizaehlen_ini.py
    zaehlen.py
       ---ruft---> zaehlen_ini.py

    Versionen der beteiligten Programme:
    ========================
    menu_multizaehlen.py [Oberfläche zum Aufruf von multizaehlen]
    """
    version_text += "   " + menu_multizaehlen_vers + ": " + menu_multizaehlen_date
    version_text += "\nmultizaehlen.py [vergleichende Darstellung mehrerer Aufrufe von zaehlen]\n"
    version_text += "   " + multizaehlen_vers + ": " + multizaehlen_date
    version_text += "\nzaehlen.py [Programm zum Auszählen von Texten]\n"
    version_text += "   " + zaehlen_vers + ": " + zaehlen_date
    version_text += """\n\nVersionen der beteiligten Konfigurationsdateien:
    ===============================
    menu_multizaehlen_ini.py [Konfiguration für menu_multizaehlen.py]\n"""
    version_text += "   " + menue_zaehlen_ini_date
    version_text += "\nmultizaehlen_ini.py [Konfiguration für multizaehlen.py]\n"
    version_text += "   " + multizaehlen_ini_date
    version_text += "\nzaehlen_ini.py [Konfiguration für zaehlen.py]\n"
    version_text += "   " + zaehlen_ini_date

# -----------------------------------------------------------------------
# Vereinbarungen

sl      = "/"                                  # Schrägstrich als Verzeichnistrennzeichen
##cd      = sys.path[0]                      # enthält akt. Verzeichnis
##cd      = cd.replace("\\", sl)             # normiert auf "/" als Trennstrich
datum   = "2018-08-04"                         # Datum der letzten Änderung
dir_sep = """[\/]"""                           # Trennzeichen für Verzeichnisnamen
ul      = "_"                                  # in create_filenames benutzt
p       = re.compile(dir_sep)

# Hilfsvariable
leer    = ""
name_in = []

# Sequenzen anlegen
L = []  # Labels
E = []  # Eingabefelder (Entry)
B = []  # Knöpfe (Button)
V = []  # Statusvariable für Checkboxen
C = []  # Checkboxen

# Sequenzen initialisieren
for f in range(len(conf)):
    L.append(None)
    E.append(None)
    V.append(None)
    C.append(None)

# Sequenz B (für Buttons) initialisieren
for f in range(len(button_conf)):
    B.append(None)
    
# =======================================================================
# einige Methoden

def create_filename(nummer, basis):
    """generiert aus nummer und basis einen Dateinamen"""
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
def hilfe1():
    """gibt einen Hilfetext aus."""
    showinfo(msg1, hilfe_text1)

# -----------------------------------------------------------------------
def hilfe2():
    """gibt einen Hilfetext aus."""
    showinfo(msg2, hilfe_text2)

# -----------------------------------------------------------------------
def hilfe3():
    """gibt einen Hilfetext aus."""
    showinfo(msg3, hilfe_text3)
    
# -----------------------------------------------------------------------
def init_entry_fields():
    """initialisiert Labels und Eingabefelder."""
    for f in range(len(conf)):
        L[f] = Label(mm, text=conf[f][0])
        L[f].grid(row = f)
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
    for f in range(len(conf)):
        if (conf[f][3] != 4):
            print(conf[f][0], ":", E[f].get())
        else:
            print(conf[f][0], ":", V[f].get())
    
# -----------------------------------------------------------------------
def clear_entry_fields():
    """löscht die Inhalte der Eingabefelder."""
    for f in range(len(conf)):
        if (conf[f][3] != 4):
            E[f].delete(0, END)
        else:
            V[f] = 0

# -----------------------------------------------------------------------
def ask_in_file():
    """erfragt die/den Namen der Eingabedatei(en) und trägt sie/ihn ein."""
    global name_in
    name_in = []
    name_in = askopenfilenames(filetypes = ((pickle_files, "*.pkl"),(all_files, "*.*")))
    E[0] = Entry(mm)
    E[0].insert(10, tuple_text.format(str(len(name_in))))
    E[0].grid(row=0, column=1)

# -----------------------------------------------------------------------
def reset_entry_fields():
    """setzt Eingabefelder auf Voreinstellungen zurück."""
    for f in range(len(conf)):
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
    """wertet die Eingabefelder aus und startet multizaehlen.py."""
    aufruf   = ["python", program_name]
    optionen = ""

    for f in range(len(conf)):
        typ     = conf[f][3]
        zwi_val = ""
        par     = conf[f][2]
        default = conf[f][1]
        if (typ == 2):
            zwi = E[f].get()
            if (zwi not in [leer, default]):
                aufruf.append(par); aufruf.append(zwi)
        elif (typ == 3):
            zwi = E[f].get()
            if (zwi not in ["0", leer]):
                aufruf.append(par)
        elif (typ == 1):
            zwi = E[f].get()
            if zwi != leer:
                aufruf.append(par); aufruf.append(zwi)
        elif (typ == 4):
            zwi = V[f].get()
            if (zwi == 1):
                aufruf.append(par)
        elif (typ == 0):
            zwi = E[f].get()
            if zwi != leer:
                for k in range(len(name_in)):
                    aufruf.append(name_in[k])
        else:
            pass

    showinfo(title=call_text, message = aufruf)
    x          = subprocess.Popen(aufruf, stderr=subprocess.PIPE, universal_newlines=True)
    fehlermeld = x.stderr.read()
    if (len(fehlermeld) > 0):
        showerror(title=error_text, message = fehlermeld, icon = ERROR)
    showinfo(title=execution_text, message = end_text)

# -----------------------------------------------------------------------
def init_buttons():
    """legt Buttons an und initialisiert sie."""
    for f in range(len(button_conf)):
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
    showinfo(msg4, version_text)

    
# =======================================================================
# eigentliches Programm

mm = Tk()
mm.title(programmtitle + program_name)
init_entry_fields()
init_buttons()

mainloop( )
