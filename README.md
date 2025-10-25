# Textfile glosses to LaTeX

A project to convert [Interlinear Glossed Text (IGT)](https://en.wikipedia.org/wiki/Interlinear_gloss) to 3 line glosses in LaTeX.


## Instructions:
1. Add following packages and commands to your LaTeX preamble:

    > \usepackage{libertine} % font with many IPA symbols.  
    > \usepackage{tipa} % fonts and macros for IPA  
    >   
    > \newcommand{\sh}{\textipa{S}}     
    > \newcommand{\supw}{\textsuperscript{w}}   
    > \newcommand{\supj}{\textsuperscript{j}}   
    > \newcommand{\nj}{\textltailn}     
    > \newcommand{\opo}{\textopeno}     
    > \newcommand{\E}{\textepsilon}     
    > \newcommand{\Z}{\textyogh}    
    > \newcommand{\n}{\textipa{\ng}}    
    > \newcommand{\turnr}{\textipa{\textturnr}}
    
    1.1. Depending on which glossing package you prefer, choose one of the following:

    > \usepackage{linguex}
    
    > \usepackage{gb4e}

2. Paste your examples (with gloss, translation, and/or notes) in `input.txt`:
   
    > ì nâ l(a) īmótō   
    > 3SG PROG buy car  
    > S/he was buying a car.    
    > --> some comment

3. Go into the console (*e.g.,* Windows Powershell, Terminal) in current directory.
4. Run script
    
    > python elicitation_to_latex.py
    
    4.1. You can add your preferred glossing package as an argument (default=`linguex`):
    
    > python elicitation_to_latex.py gb4e

5. Results in `output.txt` file:

    with `linguex`:
    >       \exg. \`{i} n\^{a} l(a) \={i}m\'{o}t\={o}.\\
    >           3\sc{sg} \sc{prog} buy car\\
    >           ``S/he was buying a car.''

    with `gb4e`:
    >     \begin{exe}
    >       \ex
    >           \gll \`{i} n\^{a} l(a) \={i}m\'{o}t\={o}.\\
    >           3\sc{sg} \sc{prog} buy car\\
    >           ``S/he was buying a car.''

    >     \end{exe}
