#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# (C) Günter Partosch 2017-2018

# menu_multizaehlen.py
# Stand: 2018-08-19

# 1.0.0: 2017-02-19: Anfang, aus menu_zaehlen.py entwickelt
# 1.1.0: 2017-02-19: erstmals funktionsfähig
# 1.2.0: 2017-07-18: Erweiterung und neues Konzept
# 1.2.8: 2020-08-15: Ausgabe-Strings in ini-Datei verlagert

m_mz_datum   = "2020-08-15"
m_mz_version = "1.2.8"

# -----------------------------------------------------------------------
# Abhängigkeiten
# menu_multizaehlen.py
# + lädt menu_multizaehlen_ini.py als Modul
# + ruft multizaehlen.py auf

# -----------------------------------------------------------------------
# Module importieren

from menu_multizaehlen_ini import *            # Initialisierungsdatei des Programms menu_multizaehlen.py
import sys                                     # wird für path benötigt
import subprocess                              # Starten/Beobachten von Subprozessen
from tkinter import *                          # Tk
from tkinter.filedialog import askopenfilenames# Dateinamen erfragen in Tk
from tkinter.filedialog import askopenfilename # einen Dateinamen erfragen in Tk
from tkinter.messagebox import *               # Ausgabe in Message-Boxen
##from copy import deepcopy                      # "tiefes" Kopieren von Tuples und Listen
import re                                      # reguläre Ausdrücke

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
    
# -----------------------------------------------------------------------
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

def hilfe1():
    """gibt einen Hilfetext aus."""
    showinfo(msg1, hilfe_text1)

def hilfe2():
    """gibt einen Hilfetext aus."""
    showinfo(msg2, hilfe_text2)

def hilfe3():
    """gibt einen Hilfetext aus."""
    showinfo(msg3, hilfe_text3)
    
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

def show_entry_fields():
    """zeigt die Werte der Eingabefelder an."""
    for f in range(len(conf)):
        if (conf[f][3] != 4):
            print(conf[f][0], ":", E[f].get())
        else:
            print(conf[f][0], ":", V[f].get())
    
def clear_entry_fields():
    """löscht die Inhalte der Eingabefelder."""
    for f in range(len(conf)):
        if (conf[f][3] != 4):
            E[f].delete(0, END)
        else:
            V[f] = 0

def ask_in_file():
    """erfragt die/den Namen der Eingabedatei(en) und trägt sie/ihn ein."""
    global name_in
    name_in = []
    name_in = askopenfilenames(filetypes = ((pickle_files, "*.pkl"),(all_files, "*.*")))
    E[0] = Entry(mm)
    E[0].insert(10, tuple_text.format(str(len(name_in))))
    E[0].grid(row=0, column=1)

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
    
def start():
    """wertet die Eingabefelder aus und startet zaehlen.py."""
    aufruf   = ["python", programmname]
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

def version():
    """gibt Versionsdaten aus."""
    showinfo(msg4, version_text)
    
# -----------------------------------------------------------------------
# eigentliches Programm

mm = Tk()
mm.title(programmtitle + programmname)
init_entry_fields()
init_buttons()

mainloop( )
