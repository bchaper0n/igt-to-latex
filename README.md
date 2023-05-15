![alt text](https://icons.iconarchive.com/icons/custom-icon-design/all-country-flag/64/Nigeria-Flag-icon.png "NG Flag")
# Igala (Niger-Congo) to LaTeX

A project to convert elicitation data to 3 line glosses in LaTeX.


## Instructions:
1. Paste your examples (with gloss, translation, and/or notes) in 'input_unformatted_text.txt' as such:
   
    > ì nâ l(a) īmótō           
    > 3SG PROG buy car           
    > S/he was buying a car.     
    >                            
    > ì nâ ɲa l(a) īmótō        
    > 3SG PROG go buy car
    > He is gone to buy a car    
    > --> answer to 'where are they'?

2. Go into the console (e.g., Windows Powershell, Terminal) in current directory.
3. Run `python elicitation_to_latex.py`
4. Results in output file:

    >     \begin{exe}
    >       \ex
    >           \gll \`{i} n\^{a} l(a) \={i}m\'{o}t\={o}.\\
    >           3\sc{sg} \sc{prog} buy car\\
    >           S/he was buying a car.
    >     \end{exe}
    > 
    >     \begin{exe}
	>       \ex
	>    	    \gll \`{i} n\^{a} \textltailn{}a l(a) \={i}m\'{o}t\={o}.\\
	>    	    3\sc{sg} \sc{prog} go buy car\\
	>    	    He is gone to buy a car.\\
	>    	    --> answer to 'where are they'?
    >     \end{exe}