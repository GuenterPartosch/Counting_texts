#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# please adjust these two lines if necessary

# multizaehlen_ini_en.py

# (C) Günter Partosch 2021

# english texts for ini file
# Stand: 2020-09-01 (Anfangsversion)

# Dependencies:
# + is loaded in multizaehlen.py
# + is loaded in menu_multizaehlen.py

# globale Parameter
# -------------------------------------------------------------------
# do not touch

menu_multizaehlen_ini_date  = "2021-03-06"  
menu_multizaehlen_ini_vers  = "1.1.12"
menu_multizaehlen_date      = "2020-08-27" # menu_multizaehlen.py
menu_multizaehlen_vers      = "1.2.10"     # menu_multizaehlen.py
multizaehlen_ini_date       = "2020-08-26" # multizaehlen_ini.py
multizaehlen_ini_en_date    = "2020-09-01" # multizaehlen_in_en.py


# Output Strings
# ===================================================================

# global program parameters
# -------------------------------------------------------------------
# do not change

main_caption_text  = "Comparative counting of words in texts"
##prg_name_text      = "multizaehlen.py"
##prg_author_text    = "Günter Partosch"
##author_email_text  = "Guenter.Partosch@hrz.uni-giessen.de"
##author_institution = "Justus-Liebig-Universität Gießen, Hochschulrechenzentrum"

# Argparse
# -------------------------------------------------------------------
# Do not change

files_text     = "Specify input file(s) [*.pkl]"
files_anz_text = "Beschränkung der Dateien-Zahl (*.plk) mit Zeichenkette"
sort1_text     = "Specify 1st sorting (a+|a-|A+|A-)"
sort2_text     = "Specify 2nd sorting (L+|L-|F+|F-)"
out_text       = "Specify name of the output file"
template_text  = "Limitation by specified word templates"
lengths_text   = "Limitation by specified word lengths"
rank_text      = "Limitation by specified ranks"
freq_text      = "Limitation by specified word frequencies"
version_text   = "Show version of the program and exit"
autor_text     = "Show author of the program and exit"
fd_text        = "Show distribution of word frequencies"
ld_text        = "Show distribution of word lengths"
sd_text        = "Show distribution of separator characters"
cd_text        = "Show distribution of characters"

argp_pos_par   = 'Positional parameters'
argp_opt_par   = 'Optional parameters'
argp_default   = 'Default'

# Kopf, allgemein                                                         # header, general
# -------------------------------------------------------------------     # max width: 43
# Can be changed

head_content   = "Contents"
head_prg_name  = "Name of the program"
head_prg_vers  = "Version of the program"
head_prg_date  = "Date of last changes"
prg_author     = "Author of the program"
author_email   = "Author's eMail address"
author_inst    = "Author's institution"
res_pre_ld     = "Results (distribution of lengths before filtering)"
res_pre_fd     = "Results (distribution of frequencies before filtering)"
res_pre_cd     = "Results (distribution of characters before filtering)"
res_pre_sd     = "Results (distribution of separators before filtering)"
head_prg_para  = "parameters of the program"
head_result    = "Results"
head_summary   = "Summary"

# header, program parameters
# -------------------------------------------------------------------     # max width: 57
# can be changed

sub_caption    = "Program parameters"
prg_call       = "Program call"

# header, table legend
# -------------------------------------------------------------------
# can be changed

caption_leg    = "Results"
leg_rank       = "Sequence of ranks (sequential number)"
leg_str_len    = "Length of string"
leg_string     = "String"
leg_str_freq   = "Frequency of thnis string in all input files"
leg_acc_freq   = "Accumulated frequency of this string"
leg_file_nr    = "Number of input files with this string"
leg_in_file    = "Name of input file"

# output, summary
# -------------------------------------------------------------------     # max width: 42
# can be changed

result_summ    = "Summary"
res_token_pre  = "Number of tokens (before filtering)"
res_types_pre  = "Number of types (before filtering)"
res_ratio_pre  = "Ratio types/tokens (before filtering)"
res_token_post = "Number of tokens (after filtering)"
res_types_post = "Number of types (after filtering)"
res_ratio_post = "Ratio types/tokens (after filtering)"
types_pre_post = "Ratio types (after/before filtering)"
token_pre_post = "Ratio tokens (after/before filtering)"

# output, distribution word lengths
# -------------------------------------------------------------------
# can be changed

caption_ld     = "Results (distribution of lengths before filtering)"
ld_hdr_nr      = "sequential number"
ld_hdr_length  = "Length"
ld_hdr__word_nr= "Number of words with this length in all files"
ld_hdr_files_nr= "Number of files with words with this length"
ld_hdr_infile  = "Name of input file"
ld_summary_sum = "Sum:"
ld_modus       = "Modus:"
ld_at          = "at:"
ld_wa_short    = "wa"
ld_wa_long     = "(wa = weighted average)"
ld_min_length  = "Minimal length"
ld_max_length  = "Maximal length"

# output, distribution of frequencies
# -------------------------------------------------------------------
# can be changed

caption_fd     = "Results (distribution of frequencies before filtering) "
fd_hdr_nr      = ld_hdr_nr
fd_hdr_freq    = "Frequency"
fd_hdr_freq_nr = "Number of words with this frequency in all files"
fd_hdr_files_nr= "Number of files with words with this frequency"
fd_hdr_infile  = ld_hdr_infile
fd_summary_sum = ld_summary_sum
fd_modus       = ld_modus
fd_at          = ld_at
fd_min_freq    = "Minimal frequency"
fd_max_freq    = "Maximal frequency"

# output, distribution of characters
# -------------------------------------------------------------------"
# can be changed

caption_cd     = "Results (distribution of characters before filtering)" 
cd_hdr_nr      = ld_hdr_nr
cd_hdr_char    = "Character"
cd_hdr_hex     = "Associated hex code"
cd_hdr_char_nr = "Number of thnis character in all files"
cd_hdr_files_nr= "Number of files with this character"
cd_hdr_infile  = ld_hdr_infile
cd_summary_sum = ld_summary_sum
cd_modus       = ld_modus
cd_at          = ld_at

# output, distribution of separators
# -------------------------------------------------------------------
# can be changed

caption_sd     = "Results (distribution of separators before filtering)"
sd_hdr_nr      = ld_hdr_nr
sd_hdr_char    = cd_hdr_char
sd_hdr_hex     = cd_hdr_hex
sd_hdr_char_nr = cd_hdr_char_nr
sd_hdr_files_nr= cd_hdr_files_nr
sd_hdr_infile  = ld_hdr_infile
sd_summary_sum = ld_summary_sum
sd_modus       = ld_modus
sd_at          = ld_at

# Error messages and warnings
# -------------------------------------------------------------------
# do not touch

err_out        = "---Output file {0} could not be opened; program exits!"
err_pkl_open   = "---File {0} could not be opened; program exits!"
err_type       = "---File {0} has not the correct type; program exits!"
err_compatib   = "---Structures of the former result files are not compatible; program exits!"
err_no_files   = "---No files specified; program exits!"
warn_no_ini    = "---Warning: zaehlen_ini.py not found"
