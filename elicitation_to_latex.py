import os
import sys

# linguistics gloss abbreviations
abbrvs = ["SG", "PL", "STR", "DUR", "NMLZ", "SFP", "NEG", "IPFV", "PFV", "PERF", "COMP", "REL", "PROG", "DET", "DIST", "PROX", "FOC", "EMPH", "COP", "OBJ", "SUBJ", "PST", "FUT", "PRES", "MULT", "ABESS", "ABIL", "ABL", "ABS", "ABST", "ABSTR", "ABSV", "ACC", "ACH", "ACT", "AD", "ADD", "ADESS", "ADEL", "ADJ", "ADJZ", "ADM", "ADR", "ADV", "ADVS", "ADVZ", "AEQ", "AFF", "AFFT", "AGT", "AJC", "AL", "ALL", "ALLOC", "AN", "ANA", "AND", "ANT", "ANT", "ANTEL", "ANTESS", "ANTIC", "AC", "ANTIP", "AP", "ANTLAT", "AOR", "APL", "APPOS", "APR", "APRT", "APRX", "APUD", "ARG", "ART", "ASC", "ASRT", "ASSUM", "ATR", "ATTEN", "AUD", "AUG", "AUX", "AV", "AVERT", "AVR", "BEN", "BG", "BV", "CAR", "CARD", "CAUS", "CENT", "CERT", "CESS", "CHEZ", "CIRC", "CIRC", "CIS", "CIT", "CJT", "CLF", "CMPL", "CMPR", "CNJ", "CNTF", "CNTR", "CEXP", "COL", "COM", "COMP", "CON", "CONC", "COND", "CONF", "CONJ", "CONJC", "CONN", "CONR", "CONT", "CONT", "COOP", "COORD", "COP", "COR", "CRAS", "CRS", "CTG", "CTM", "CUS", "CV", "CVB", "DAT", "-DE", "DEB", "DECL", "DED", "DEF", "DEL", "DEM", "DENOM", "DEO", "DEOBJ", "DEP", "DEPR", "DER", "DES", "DEST", "DET", "DETR", "-DI", "DIM", "DIR.EV", "DIR", "DISC", "DISJ", "DIST", "DISTR", "DIV", "DNZ", "DO", "DOM", "DON", "DOX", "DR", "DS", "DSC", "DTR", "DU", "DUB", "DUR", "DV", "DY", "DYN", "EGO", "EGR", "ELA", "EMO", "EMP", "EP", "EPIT", "ERG", "ESS", "EV", "EVIT", "EXAL", "EXCL", "EX", "EXCLAM", "EXESS", "EXH", "EXIST", "EXO", "EXP", "EXT", "FAC", "FAM", "FIN", "FMR", "FOC", "FOR", "FPRT", "FRACT", "FREQ", "FRUS", "FS", "FTV", "FUT", "G1", "G2 ", "G3 ", "G4", "GEN", "GER", "GIV", "GNO", "GNR", "GV", "HAB", "HCR", "HES", "HEST", "HIST", "HOD", "HON", "HORT", "HRS", "HUM", "HYP", "IAM", "IDEO", "IGN", "ILL", "IMM", "IMP", "IMPF", "IMPR", "IMPRS", "IN", "INAL", "INAN", "INCH", "INCL, IN", "IND", "INDH", "INDN", "INEL", "INESS", "INF", "INFL", "INFR", "INJ", "INS", "INT", "INTER", "INTF", "INTL", "INTRV", "INTS", "INTV", "INV", "IO", "IPS", "IRR", "ITER", "ITV", "IV", "JUS", "KIN", "KNWN", "L2", "LAT", "LIG", "LIM", "LNK", "LOC", "LOG", "LV", "MAL", "MAN", "MED", "MID", "MIR", "MIT", "MOD", "MOM", "MONO", "MOV", "MSD", "MUL", "N-", "NARR", "NCOMPL", "NCTM", "NDEF", "NEC", "NEG", "NEUT", "NFIN", "NH", "NMZ", "NOM", "NPFV", "NTR", "NUM", "NVIS", "NVOL", "OBJ", "OBL", "OBV", "ONOM", "OPT", "ORD", "ORIG", "PASS", "PAUS", "PAU", "-PE", "PEG", "PEJ", "PERAMB", "PERL", "PERM", "PERS", "PFV", "-PI", "PL", "PLUP", "PLUR, VPL", "PO", "POEL", "POESS", "POL", "POSS", "POSB", "POST", "POSTL", "POT", "PPRT", "PREC", "PRED", "PREP", "PRET", "PRF", "PRIV", "PRO", "PROB", "PROG", "PROH", "PROL", "PROP", "PROS", "PROSP", "PROT", "PROX", "PRS", "PST", "PTCP", "PTV", "PUNC", "PRP", "PV", "PVB", "QUAL", "QUANT", "QUOT", "-R", "RAR", "REAL", "REC", "RECP", "REF", "REFL", "REG", "REGR", "REL", "REM", "REP", "RES", "RESP", "RET", "REV", "ROOT", "ROY", "RPT", "RQ", "RST", "RV", "SAP", "SBEL", "SBESS", "SBJ", "SCEP", "SE", "SEC", "SEJ", "SEM", "SEN", "SEP", "SEQ", "SER", "SG", "SGV", "SIM", "SIMV", "SIT", "SJV", "SKT", "SMBL", "SOC", "SP", "SPECFR", "SPECL", "SPKR", "SS", "STAT", "STEM", "SUB", "SUBL", "SUBR", "SUP", "SUP", "SUPEL", "SUPER", "SUPESS", "SUPL", "SUPP", "-T", "TA", "TAG", "TAM", "TEL", "TEMP", "TENT", "TER", "TKN", "TNS", "TOP", "TOT", "TR", "TRANSL", "TRI", "TRN", "TRZ", "TVF", "UNSP", "UR", "UTIL", "UV", "-V", "VAL", "VB", "VBZ", "VD", "VE", "VEN", "VER", "VERT", "VIA", "VIRT", "VI", "VIS", "VN", "VOC", "VOL", "VR", "VT", "WHQ", "WIT", "ZO"]

# change these according to your file names
input_file_name = 'input.txt'
temp_output_file_name = 'output_temp.txt'
output_file_name = 'output.txt'

if len(sys.argv) > 1: # if argument input
    if sys.argv[1] == "linguex":
        goption = 0
    elif sys.argv[1] == "gb4e":
        goption = 1
    else:
        print("Warning: Glossing package argument invalid; defaulting to linguex.")
        goption = 0
else:
    goption = 0

def replace_tonal(line):

    # special case in Igala
    new_str = line.replace("b͡à", "\\t{b\`{a}}")

    # replace all with -
    new_str = new_str.replace("ā", "\={a}")
    new_str = new_str.replace("ā", "\={a}")
    new_str = new_str.replace("Ā", "\={A}")
    new_str = new_str.replace("Ā", "\={A}")
    new_str = new_str.replace("ē", "\={e}")
    new_str = new_str.replace("ē", "\={e}")
    new_str = new_str.replace("ī", "\={i}")
    new_str = new_str.replace("ī", "\={i}")
    new_str = new_str.replace("Ī", "\={I}")
    new_str = new_str.replace("ō", "\={o}")
    new_str = new_str.replace("ō", "\={o}")
    new_str = new_str.replace("Ō", "\={O}")
    new_str = new_str.replace("Ō", "\={O}")
    new_str = new_str.replace("ū", "\={u}")
    new_str = new_str.replace("ū", "\={u}")
    new_str = new_str.replace("ɔ̄", "\={\\textopeno}")
    new_str = new_str.replace("ɛ̄", "\={\\textepsilon{}}")
    new_str = new_str.replace("n̄", "\={n}")
    
    # replace all with ^
    new_str = new_str.replace("â", "\^{a}")
    new_str = new_str.replace("â", "\^{a}")
    new_str = new_str.replace("ê", "\^{e}")
    new_str = new_str.replace("ê", "\^{e}")
    new_str = new_str.replace("î", "\^{i}")
    new_str = new_str.replace("ô", "\^{o}")
    new_str = new_str.replace("ô", "\^{o}")
    new_str = new_str.replace("û", "\^{u}")
    new_str = new_str.replace("ɔ̂", "\^{\\textopeno}")
    new_str = new_str.replace("ɛ̂", "\^{\\textepsilon{}}")

    # replace all with v
    new_str = new_str.replace("ǎ", "\\v{a}")
    new_str = new_str.replace("ě", "\\v{e}")
    new_str = new_str.replace("ě", "\\v{e}")
    new_str = new_str.replace("ǐ", "\\v{i}")
    new_str = new_str.replace("ǐ", "\\v{i}")
    new_str = new_str.replace("ǒ", "\\v{o}")
    new_str = new_str.replace("ǒ", "\\v{o}")
    new_str = new_str.replace("Ǒ", "\\v{O}")
    new_str = new_str.replace("ǔ", "\\v{u}")
    new_str = new_str.replace("ǔ", "\\v{u}")
    new_str = new_str.replace("ɔ̌", "\\v{\\textopeno}")
    new_str = new_str.replace("ɛ̌", "\\v{\textepsilon{}}")
    new_str = new_str.replace("ň", "\\v{\textepsilon{}}")
    new_str = new_str.replace("ŋ̌", "\\v{\\n{}}")
    
    # replace all with '
    new_str = new_str.replace("á", "\\'{a}")
    new_str = new_str.replace("á", "\\'{a}")
    new_str = new_str.replace("Á", "\\'{A}")
    new_str = new_str.replace("é", "\\'{e}")
    new_str = new_str.replace("é", "\\'{e}")
    new_str = new_str.replace("í", "\\'{i}")
    new_str = new_str.replace("í", "\\'{i}")
    new_str = new_str.replace("Í", "\\'{I}")
    new_str = new_str.replace("ó", "\\'{o}")
    new_str = new_str.replace("ó", "\\'{o}")
    new_str = new_str.replace("ú", "\\'{u}")
    new_str = new_str.replace("ú", "\\'{u}")
    new_str = new_str.replace("ɔ́", "\\'{\\textopeno}")
    new_str = new_str.replace("Ɔ́", "\\'{\\textopeno}")
    new_str = new_str.replace("Ó", "\\'{O}")
    new_str = new_str.replace("ɛ́", "\\'{\\textepsilon{}}")
    new_str = new_str.replace("ń", "\\'{n}")

    # replace all with `
    new_str = new_str.replace("à", "\`{a}")
    new_str = new_str.replace("à", "\`{a}")
    new_str = new_str.replace("À", "\`{A}")
    new_str = new_str.replace("À", "\`{A}")
    new_str = new_str.replace("è", "\`{e}")
    new_str = new_str.replace("è", "\`{e}")
    new_str = new_str.replace("ì", "\`{i}")
    new_str = new_str.replace("ì", "\`{i}")
    new_str = new_str.replace("ò", "\`{o}")
    new_str = new_str.replace("ò", "\`{o}")
    new_str = new_str.replace("Ò", "\`{O}")
    new_str = new_str.replace("ù", "\`{u}")
    new_str = new_str.replace("ù", "\`{u}")
    new_str = new_str.replace("ɔ̀", "\`{\\textopeno}")
    new_str = new_str.replace("ɛ̀", "\`{\\textepsilon{}}")
    new_str = new_str.replace("Ù", "\`{U}")
    new_str = new_str.replace("ǹ", "\`{n}")
    

    # replace all with "
    new_str = new_str.replace("a̋", "\H{a}")
    new_str = new_str.replace("A̋", "\H{A}")
    new_str = new_str.replace("e̋", "\H{e}")
    new_str = new_str.replace("i̋", "\H{i}")
    new_str = new_str.replace("ő", "\H{o}")
    new_str = new_str.replace("ő", "\H{o}")
    new_str = new_str.replace("ű", "\H{u}")
    new_str = new_str.replace("ű", "\H{u}")
    new_str = new_str.replace("ɔ̋", "\H{\\textopeno}")
    new_str = new_str.replace("ɛ̋", "\H{\\textepsilon{}}")
    new_str = new_str.replace("n̋", "\H{n}")

    # replace all other contour tones
    new_str = new_str.replace("o᷇", "\\am{o}")
    new_str = new_str.replace("i᷇", "\\am{i}")
    new_str = new_str.replace("ɔ᷅", "\\textlowrise{\\textopeno}")
    new_str = new_str.replace("o᷅", "\\textlowrise{o}")
    new_str = new_str.replace("a᷄", "\\texthighrise{a}")
    new_str = new_str.replace("e᷄", "\\texthighrise{e}")
    new_str = new_str.replace("ɛ᷆", "\mg{\\textepsilon}")
    new_str = new_str.replace("e᷆", "\mg{e}")
    new_str = new_str.replace("u᷆", "\mg{u}")
    new_str = new_str.replace("o᷆", "\mg{o}")
    new_str = new_str.replace("ɔ᷆", "\mg{\\textopeno}")
    new_str = new_str.replace("i᷆", "\mg{i}")
    new_str = new_str.replace("a᷆", "\mg{a}")

    return new_str

def replace_vowels(line):

    new_str = line.replace("ä", "\"{a}")
    # TODO: add other umlaut variants

    new_str = new_str.replace("ɨ", "\\textbari{}")
    new_str = new_str.replace("ʉ", "\\textbaru{}")
    new_str = new_str.replace("ɯ", "\\textturnm{}")
    new_str = new_str.replace("ɪ", "\\textsci{}")
    new_str = new_str.replace("ʏ", "\\textscy{}")
    new_str = new_str.replace("ʊ", "\\textupsilon{}")
    new_str = new_str.replace("ø̞", "\|‘{\o}")
    new_str = new_str.replace("ø", "\o{}")
    new_str = new_str.replace("ɘ", "\\textreve{}")
    new_str = new_str.replace("ɵ", "\\textbaro{}")
    new_str = new_str.replace("ɤ̞", "\|‘{\\textgamma}")
    new_str = new_str.replace("ɤ", "\\textgamma{}")
    new_str = new_str.replace("o̞", "\|‘{o}")
    new_str = new_str.replace("e̞", "\|‘{e}")
    new_str = new_str.replace("ə", "\\textschwa{}")
    new_str = new_str.replace("ɛ", "\\textepsilon{}")
    new_str = new_str.replace("œ", "\oe{}")
    new_str = new_str.replace("ɜ", "\\textrevepsilon{}")
    new_str = new_str.replace("ɞ", "\\textcloserevepsilon{}")
    new_str = new_str.replace("ʌ", "\\textturnv{}")
    new_str = new_str.replace("ɔ", "\\textopeno{}")
    new_str = new_str.replace("æ", "\\ae{}")
    new_str = new_str.replace("ɐ", "\\textturna{}")
    new_str = new_str.replace("ɶ", "\OE{}")
    new_str = new_str.replace("ɑ", "\\textscripta{}")
    new_str = new_str.replace("ɒ", "\\\textturnscripta{}")
                              
    return new_str


def replace_pulmonic_cons(line):

    new_str = line.replace("ɳ", "\\textrtailn{}")
    new_str = new_str.replace("ɲ", "\\textltailn{}")
    new_str = new_str.replace("ɱ", "\\textltailm{}")
    new_str = new_str.replace("ŋ", "\\n{}")
    new_str = new_str.replace("ʒ", "\Z{}")
    new_str = new_str.replace("ʤ", "d\Z{}")
    new_str = new_str.replace("ɡ", "\\textscriptg{}")
    new_str = new_str.replace("ʃ", "\sh{}")
    new_str = new_str.replace("ɹ", "\\textturnr{}")

    return new_str

def clean_example(line): 

    # any seemingly duplicate replacements are due to different encodings
    # replace tabs with spaces
    new_str = line.strip()

    new_str = new_str.replace("\t", " ")

    # remove new lines at end of lines
    new_str = new_str.replace("\n", "")

    # replace up arrow before falling tone character 
    new_str = new_str.replace("^", "$\\Uparrow$")

    # replace characters with tone
    new_str = replace_tonal(new_str)

    # replace toneless vowels
    new_str = replace_vowels(new_str)

    # replace common pulmonic consonants
    new_str = replace_pulmonic_cons(new_str)

    # replace other common symbols/diacritics
    new_str = new_str.replace("ʷ", "\\textsuperscript{w}")
    new_str = new_str.replace("ʲ", "\\textsuperscript{j}")
    new_str = new_str.replace("ʰ", "\\textsuperscript{h}")
    new_str = new_str.replace("ˤ", "\\textsuperscript{\\textgamma}")
    new_str = new_str.replace("ˠ", "\\textsuperscript{\\textrevglotstop}")
    new_str = new_str.replace("ː", "\\textlengthmark{}")
    new_str = new_str.replace(":", "\\textlengthmark{}")
    new_str = new_str.replace("ꜛ", "\\textupstep{}")
    new_str = new_str.replace("ꜜ", "\\textdownstep{}") 
    new_str = new_str.replace("…", "...") 
    new_str = new_str.replace("’", "'") 
    new_str = new_str.replace("→", "-->")
     
    new_str = new_str.replace("“", "``")
    new_str = new_str.replace("”", "''")

    return new_str

# open input file and (create and) open output file
with open(input_file_name, 'r', encoding="utf8") as i_file, open(temp_output_file_name, 'w') as o_file:
    
    # format 3 line glosses
    ex_num = 1
    gloss_line = 1
    lines = i_file.readlines()
    first_popped = False
    last_popped = False

    while not first_popped: # remove initial empty lines
        if lines[0] in ['\n', '\r\n']:
            lines.pop(0)
        else:
            first_popped = True

    while not last_popped: # remove trailing empty lines
        if lines[-1] in ['\n', '\r\n']:
            lines.pop(-1)
        else:
            last_popped = True

    try:
        for i, line in enumerate(lines):
            if(line.strip()):
                c_line = ""
                c_line = clean_example(line)
                                
                if gloss_line == 1: # if 1st line of example, begin example
                    if goption == 0: # if linguex
                        c_line = "\\exg. " + c_line
                    else: # else gb4e
                        c_line = "\\begin{exe}\n\t\ex\n\t\t\gll " + c_line
                    if c_line[-1] != ".":
                        c_line = c_line + "."
                elif gloss_line == 2: # if 2nd line of example, tab glosses
                    c_line = "\t\t" + c_line + "\\\\"
                elif gloss_line == 3: # if 3rd line of example, tab translation and add quotations
                    if c_line[-1] != "." and c_line[-1] != "?":
                        c_line = c_line + "."
                    c_line = "``" + c_line + "''"
                    c_line = "\t\t" + c_line
                else: # if any other line of example, tab
                    c_line = "\t\t" + c_line

                if (i+1) == len(lines): # if last line of file, finish example
                    if goption == 1: # if gb4e
                        c_line = c_line + "\n\end{exe}"
                elif lines[i+1] in ['\n', '\r\n']: # if next line is empty, finish example
                    if goption == 0: # if linguex
                        c_line = c_line + "\n\n"
                    else: # else gb4e
                        c_line = c_line + "\n\end{exe}\n\n"
                    ex_num += 1
                elif gloss_line != 2:
                    c_line = c_line + "\\\\\n"
                else:
                    c_line = c_line + "\n"

                gloss_line += 1
                #print(c_line)
                o_file.write(c_line)
            else:
                gloss_line = 1
    except:
        print("Error: Example " + str(ex_num) + ", line " + str(gloss_line-1) + ", is formatted incorrectly or has an invalid character.\n")

    # close files
    i_file.close()
    o_file.close()

# replace LING abbreviations to small caps
with open(temp_output_file_name, 'r', encoding="utf8") as i_file:

    source = i_file.read()

    source = source.replace("→", "-->").replace("ː", ":").replace("…", "...").replace("’", "'").replace("“", "``").replace("”", "''")

    for abbvr in abbrvs:
        source = source.replace(abbvr, "\\textsc{" + abbvr.lower() + "}")

    i_file.close() # close file

with open(output_file_name, 'w') as o_file:

    #for line in source:
        #print(line)
    o_file.write(source)

    o_file.close() # close file

    if(os.path.isfile(temp_output_file_name)):
        os.remove(temp_output_file_name)