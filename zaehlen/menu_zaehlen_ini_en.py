#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# menu_zaehlen_ini_en.py

# (C) Günter Partosch 2018-2020

# (english version for ini file)

# Stand:
# 2020-08-28 (erste Version)
# 2020-08-29 (kl. Korrekturen)

# noch:
# + restliche englische Texte
# + Laden von zaehlen_ini.py noch besser abfedern

# --------------------------------------------------------
# do not touch

remote_program_name        = "zaehlen.py"
program_name               = "menu_zaehlen.py"                    # das aktuelle Menü-Programm menu_zaehlen.py

menu_zaehlen_ini_date      = "2020-08-30"                         # menu-zaehlen_ini.py: Datum der letzten Änderung
menu_zaehlen_ini_en_date   = "2020-08-30"

# --------------------------------------------------------
# verschiedene strings
# can be changed

msg1                     = "Input fields/check boxes"
msg2                     = "Buttons"
msg3                     = "Comments"
msg4                     = "Version(s)"
tuple_text               = 'Tuple with {0} file(s)'
error_text               = "Error"
execution_text           = "Execution"
end_text                 = "Program menu_zaehlen.py finished"
call_text                = "Call"

programmtitle            = "Counting the words in text files: menu for the program "
E0_text                  = "input file(s)"
E1_text                  = "word separators [template]"
E2_text                  = "file with stop words"
E3_text                  = "file with go words"
E4_text                  = "1st sorting [a+|a-|A+|A-]"
E5_text                  = "2nd sorting [L+|L-|F+|F-]"
E6_text                  = "Output file"
E7_text                  = "Limitation by specified word templates"
E8_text                  = "Limitation by specified word lengths"
E9_text                  = "Limitation by specified rank sequence"
E10_text                 = "Limitation by specified word frequencies"

C0_text                  = "Generate word frequency distribution"
C1_text                  = "Generate word lengths distribution"
C2_text                  = "Generate separators distribution"
C3_text                  = "Generate characters distribution"
C4_text                  = "'Silent' mode"

B0_text                  = 'Browse... [input file(s)]'
B1_text                  = 'Browse... [stop file]'
B2_text                  = 'Browse... [go file]'
B4_text                  = 'Reset'
B5_text                  = 'Delete all'
B6_text                  = 'Start'
B7_text                  = 'Terminate'
B8_text                  = 'Input fields/check boxes'
B9_text                  = 'Buttons'
B10_text                 = 'Comments'
B11_text                 = 'Version(s)'

fields_boxes_text        = "There are the following input fields / check boxes (defaults in parentheses):"
buttons_text             = "There are the following buttons:"
for_parameter            = "for parameter"
calls_text               = "calls"

# --------------------------------------------------------
# error messages and warnings
# can be changed

err_ini_text             = "--- Warning: initialization file {0} could not be loaded; --> defaults taken"
err_value_text           = "--- Error {1} at {0}; --> defaults taken"
err1_file_text           = "--- File {1} at {0} could not be opened; defaults taken"
err2_file_text           = "--- File {1} at {0} could not be opened; please correct and restart"

# --------------------------------------------------------
# help texts
# can be changed

comments_text = """
Comments:
 
(*) to [E0], [E2], [E3] und [E6]: Correct names for files are exspected.
(*) to [E2] and [E3]: You can select a file by a button ([B1] a/o [B2]).
(*) to [E0]: You can select some input files by the button [B0]. The program is executed for every selected file.
(*) to [E2]: Words which are found in this file (one per line) are not included in the results.
(*) to [E3]: Only words which are found in this file (one per line) are included in the results.
(*) to [E1] and [E7]: A correct template (regular expression) is exspected.
(*) to [E1]: Input lines are split into words byt these characters.
(*) to [E4] and [E5]: Specification for sorting: only the listed specifications are allowed; "+" means in ascending order, "-" in descending order.
(*) to [E4]: 1st (alphabetic) sorting:
    a+/a-: Sorting is not case-sensitive.
    A+/A-: Sorting is case-sensitive.
(*) to [E5]: 2nd sorting:
    L+/L-: Sorting with respect to word lengths
    F+/F-: Sorting with respect to word frenquencies
(*) to [E7]-[E10]: Limitation of output:
(*) to [E7]: Limitation with respect to specified word templates (regular expreession);
    default means: all words with one character at minimum
    Example: '^[aeiou]+en$': only words, which begin with a lower vowel [aeiou] and end with "en"
(*) to [E8]: Limitation with respect to specified word lengths
    Example: '2,10': all words with 2-9 characters
(*) to [E9]: Limitation with respect to specified rank sequence
(*) to [E10]: Limitation with respect to specified word frequencies
    Example: '2,200': all words which are 1-199 tines listed
(*) to [C0]: Distribution of word frequencies is calculated; there is no calculation if not choosen
(*) to [C1]: Distribution of word engths is calculated; there is no calculation if not choosen
(*) to [C2]: Distribution of separator frequencies is calculated; there is no calculation if not choosen
(*) to [C3]: Distribution of character frequencies is calculated; there is no calculation if not choosen

(*) to [B0]-[B2]: Buttons for the choice of files
(*) to [B4]-[B7]: Buttons for the managing of the program
(*) to [B4]: Resets all input fields by defaults.
(*) to [B5]: Clears all input fields.
(*) to [B6]: Start of the program with the given values
(*) to [B7]: Terminates the program without any calculation.
(*) to [B8]: Help text: here for input fields / checkboxes
(*) to [B9]: Help text: here for buttons
(*) to [B10]: Help text: here for additional comments)
(*) to [B11]: Information text: version(s) of the involved program(s)
"""

version_help_text = """
Chain of calls:
===============
menu_zaehlen.py
    ---calls---> menu_zaehlen_ini.py
    ---calls---> zaehlen.py
zaehlen.py
    ---calls---> zaehlen_ini.py

Versions of the involved programs:
==================================
zaehlen.py [Program for counting the words of a text]
    {0}, {1}
menu_zaehlen.py [Menu for zaehlen.py]
    {2}

Versions of the involved configuration files:
=============================================
menu_zaehlen_ini.py [configuration for menu_zaehlen.py]
    {3}
zaehlen_ini.py [configuration for zaehlen.py]
    {4}
"""

# --------------------------------------------------------
# Konfiguration für Labels und Felder/Checkboxen:
# do not touch
#
# Sequenz von 4-elementigen Listen:
# (Label, assoziierte Variable, assoziierter Aufruf-Parameter, Parameter-Typ)
#   + Label: Text, der das Feld kennzeichnet
#   + assoziierte Variable: Vorbesetzung des Feldes (aus zaehlen_ini.py)
#   + assoziierter Aufruf-Parameter: Aufruf-Parameter, den zaehlen.py erwartet
#   + Parameter-Typ: Hinweis, wie Eingaben weiter bearbeitet werden
#     1: Parameter erwartet einen Wert; spezielle Behandlung bei leerer Eingabe
#     2: Parameter erwartet einen Wert; wird normal weiter verarbeitet
#     3: Parameter erwartet keinen Wert
#     4: wie 3; zusätzlich wird eine Checkbox abgefragt

conf = [
("[E0] (-i) "  + E0_text,   in_name,                "-i",  1),
("[E1] (-s) "  + E1_text,   separator,              "-s",  2),
("[E2] (-S) "  + E2_text,   stop_name,              "-S",  2),
("[E3] (-G) "  + E3_text,   go_name,                "-G",  2),
("[E4] (-s1) " + E4_text,   sort_first,             "-s1", 2),
("[E5] (-s2) " + E5_text,   sort_second,            "-s2", 2),
("[E6] (-o) "  + E6_text,   out_name,               "-o",  1),
("[E7] (-t) "  + E7_text,   word_template,          "-t",  2),
("[E8] (-l) "  + E8_text,   p_lengths,              "-l",  2),
("[E9] (-r) "  + E9_text,   p_rank,                 "-r",  2),
("[10] (-f) "  + E10_text,  p_frequency,            "-f",  2),
("[C0] (-fd) " + C0_text,   frequency_distribution, "-fd", 4),
("[C1] (-ld) " + C1_text,   length_distribution,    "-ld", 4),
("[C2] (-sd) " + C2_text,   separator_distribution, "-sd", 4),
("[C3] (-cd) " + C3_text,   character_distribution, "-cd", 4),
("[C4] (-sm) " + C4_text,   silent_mode,            "-sm", 4)
]

# --------------------------------------------------------
# Konfiguration für Buttons
# do not touch

button_conf = [
("[B0]  " + B0_text,  "ask_in_file",         0, 2),
("[B1]  " + B1_text,  "ask_stop_file",       2, 2),
("[B2]  " + B2_text,  "ask_go_file",         3, 2),
##('[B3] Durchsuchen... (Ausgabedatei)', "ask_out_file",        6, 2),
("[B4]  " + B4_text,  "reset_entry_fields", 18, 0),
("[B5]  " + B5_text,  "clear_entry_fields", 18, 1),
("[B6]  " + B6_text,  "start",              19, 0),
("[B7]  " + B7_text,  "mm.destroy",         19, 1),
("[B8]  " + B8_text,  "help1",              18, 2),
("[B9]  " + B9_text,  "help2",              19, 2),
("[B10] " + B10_text, "help3",              18, 3),
("[B11] " + B11_text, "version",            19, 3)
]

# --------------------------------------------------------
# Text für Hilfetext 1

help_text1 = programmtitle + remote_program_name + ':\n\n'
help_text1 += fields_boxes_text + "\n\n"
for f in range(len(conf)):
    help_text1 += str(conf[f][0]) + " (" + str(conf[f][1]) + "); {0} ".format(for_parameter) + conf[f][2] + "\n"

# --------------------------------------------------------
# Text für Hilfetext 2

help_text2 = buttons_text + "\n\n"
for f in range(len(button_conf)):
    help_text2 += str(button_conf[f][0]) + "; {0} '".format(calls_text) + str(button_conf[f][1]) + "'\n"

# --------------------------------------------------------
# Text für Hilfetext 3

help_text3 = comments_text

# --------------------------------------------------------
# Texte für Hilfetext "version"

version_msg_text = version_help_text.format(zaehlen_vers, zaehlen_date, menu_zaehlen_date, menu_zaehlen_ini_date, zaehlen_ini_date)

