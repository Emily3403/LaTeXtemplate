#!/bin/bash

templateVersions=(templateSmall templateMath templateMedium templateAll)

for vers in "${templateVersions[@]}"
do
  pdflatex -ini -jobname="clatex/$vers" "&pdflatex" mylatexformat/mylatexformat.ltx "latex/$vers.tex" &
done

wait

rm clatex/*.log
