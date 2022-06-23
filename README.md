# LaTeX template
A template for LaTeX


# Compiling LaTeX

LaTeX can be compiled into a *very* fast format file. This is done with the [mylatexformat](https://ctan.org/pkg/mylatexformat).

You can either use the existing `mylatexformat.ltx` in the repository to compile your code, or you can compile it yourself. Since it doesn't change frequently it should be fine to take the one in the repository.

Unfortunately these format files are not shareable across different compilers. This means that, if you update your `pdflatex`, you will have to re-generate the format file.

Compiling is done by executing the command `pdflatex -ini -jobname="{output file}" &pdflatex" mylatexformat.ltx "{source file}"`. This is automated by the `compile.sh` script.

# Compiling for Overleaf

A problem, which appears with Overleaf is that the executable is so different from the one on my system that it can't use the format file. Thus, we have to use the Overleaf `pdflatex` to generate the format file. 

You will first have to set up the required files:
- `compileOverleaf.tex`
- `compileTemplate.tex`
- `mylatexformat.ltx`
- `src/*.sty`

Once these are uploaded, you can go ahead and compile `compileOverleaf.tex`. The output is available from "Logs" → "Other logs and files".
