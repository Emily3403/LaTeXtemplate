#!/bin/bash

pdflatex -ini -jobname="template" "&pdflatex" mylatexformat.ltx "compileTemplate.tex"
rm -f template.log
