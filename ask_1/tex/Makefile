all: ai-report-1.pdf
ai-report-1.pdf: ai-report-1.tex title/* 
		xelatex -shell-escape ai-report-1.tex
spell:
		aspell -l el_gr --ignore-case=true -c ai-report-1.tex
