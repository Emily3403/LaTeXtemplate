#!/bin/bash

pdflatex -ini -jobname="template" "&pdflatex" mylatexformat.ltx "template.tex"
rm -f template.log

