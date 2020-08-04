#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# (C) Günter Partosch 2018-2020

# menu_zaehlen.py
# Stand: 2018-08-20
# Stand: 2020-07-22
# Stand: 2020-08-04


# =======================================================================
##m_z_datum = "2020-07-22"
menue_zaehlen_Datum = "2018-08-04"             # Datum der letzten Änderung

# -----------------------------------------------------------------------
# Abhängigkeiten
# menu_zaehlen.py
# + lädt menu_zaehlen_ini.py als Modul
# + ruft zaehlen.py auf

# -----------------------------------------------------------------------
from menu_zaehlen_ini import *                 # Initialisierungsdatei des Programms menu_zaehlen.py
import sys                                     # wird für path verwendet
import subprocess                              # Starten/Beobachten von Subprozessen
from tkinter import *                          # Tk
from tkinter.filedialog import askopenfilenames# Dateinamen erfragen in Tk
from tkinter.filedialog import askopenfilename # einen Dateinamen erfragen in Tk
from tkinter.messagebox import *               # Ausgabe in Message-Boxen
import re                                      # reguläre Ausdrücke

# -----------------------------------------------------------------------
sl      = "/"                                  # Schrägstrich als Verzeichnistrennzeichen
##cd      = sys.path[0]                          # enthält akt. Verzeichnis
##cd      = cd.replace("\\", sl)                 # normiert auf "/" als Trennstrich
dir_sep = """[\/]"""                           # Trennzeichen für Verzeichnisnamen
ul      = "_"                                  # in create_filenames benutzt
p       = re.compile(dir_sep)                  # regulärer Ausdruck zum Auftrennen von Verzeichnisnamen

# Hilfsvariable
leer    = ""
name_in = []

# Sequenzen anlegen
L = []                                         # Labels
E = []                                         # Eingabefelder (Entry)
B = []                                         # Knöpfe (Button)
V = []                                         # Statusvariable für Checkboxen
C = []                                         # Checkboxen

# Sequenzen initialisieren
for f in range(len(conf)): # Schleife über alle Labels, Eingabefelder, ass. Variablen und Checkboxen 
    L.append(None)
    E.append(None)
    V.append(None)
    C.append(None)

# Sequenz B (für Buttons) initialisieren
for f in range(len(button_conf)): # Schleife über alle Schaltflächen
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
def hilfe1():
    """gibt einen Hilfetext aus."""
    showinfo("Hilfe 1", hilfe_text1)

# -----------------------------------------------------------------------
def hilfe2():
    """gibt einen Hilfetext aus."""
    showinfo("Hilfe 2", hilfe_text2)

# -----------------------------------------------------------------------
def hilfe3():
    """gibt einen Hilfetext aus."""
    showinfo("Hilfe 3 ", hilfe_text3)
    
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
    global name_in
    name_in = []
    name_in = askopenfilenames()
    E[0] = Entry(mm)
    E[0].insert(10, 'Tupel mit ' + str(len(name_in)) + ' Datei(en)')
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
    for f in range(len(conf)): # Schleife über alle Eingabefelder
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
##    aufruf   = ["python", instverz + sl + programmname]
    aufruf   = ["python", programmname]
    optionen = ""

    for f in range(len(conf)):           # Schleife über alle Eingabefelder/Checkboxen
        typ     = conf[f][3]
        zwi_val = ""
        par     = conf[f][2]
        default = conf[f][1]
        if (typ == 2):                   # (2) Parameter erwartet einen Wert; wird normal weiter verarbeitet
            zwi = E[f].get()
            if (zwi not in [leer, default]):
                aufruf.append(par); aufruf.append(zwi)
        elif (typ == 3):                 # (3) Parameter erwartet keinen Wert
            zwi = E[f].get()
            if (zwi not in ["0", leer]):
                aufruf.append(par)
        elif (typ == 1):                 # (1) Parameter erwartet einen Wert; spezielle Behandlung bei leerer Eingabe
            zwi = E[f].get()
            if zwi != leer:
                aufruf.append(par); aufruf.append(zwi)
        elif (typ == 4):                 # (4) wie 3; zusätzlich wird eine Checkbox abgefragt
            zwi = V[f].get()
            if (zwi == 1):
                aufruf.append(par)
        else:
            pass

    if (len(name_in) == 0):              # kein Name für Eingabedatei
        showinfo(title="Aufruf", message = aufruf)
        x = subprocess.Popen(aufruf, stderr=subprocess.PIPE, universal_newlines=True)
        fehlermeld = x.stderr.read()
        if (len(fehlermeld) > 0):
            showinfo(title="Fehler", message = fehlermeld)

    for f in range(len(name_in)):        # Schleife über alle Eingabedateien
        aufruf_i = aufruf[:]

        for g in range(len(aufruf_i)):   # -- Schleife über alle Parameter
            if (aufruf_i[g] == "-i"):
                g_i = g
            if (aufruf_i[g] == "-o"):
                g_o = g
        aufruf_i[g_i + 1] = name_in[f]
        aufruf_i[g_o + 1] = create_filename(f, aufruf[g_o + 1])
        showinfo(title="Aufruf", message = aufruf_i)
        x = subprocess.Popen(aufruf_i, stderr=subprocess.PIPE, universal_newlines=True)
        fehlermeld = x.stderr.read()
        if (len(fehlermeld) > 0):
            showerror(title="Fehler", message = fehlermeld, icon = ERROR)
    showinfo(title="Bearbeitung", message = "Programm menu_zaehlen beendet")

# -----------------------------------------------------------------------
def init_buttons():
    """legt Buttons an und initialisiert sie."""
    for f in range(len(button_conf)): # Schleife über alle Schaltflächen
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
    showinfo("Hilfe", version_text)
    
# =======================================================================
mm = Tk()
mm.title(programmtitle + programmname)
init_entry_fields()
init_buttons()

mainloop( )

