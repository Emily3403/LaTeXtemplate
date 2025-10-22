if [ -z ${SCRIPT_DIR+x} ]; then
    echo "ERROR: The script dir is not set. I am not continuing!"
    exit 1
fi

if [ ! -z ${_COMPILE_SHARED_LOCK+x} ]; then
    # Prevent double sourcing this file
    return
fi
_COMPILE_SHARED_LOCK=1

if [ ! -f "$SCRIPT_DIR/main.tex" ]; then
    printf "I could not find the main file to compile.\nLooking for %s/main.tex" "$SCRIPT_DIR"
    exit 1
fi

if [ ! "$(command -v latexmk)" ] && [ ! "$(command -v pdflatex)" ]; then
    echo "Failed to detect a LaTeX compiler. Make sure to have LaTeX installed."
    exit 1
fi

# A little activity notice. Inspired by https://stackoverflow.com/a/48213967/18680554
{
    while true; do
        printf "\rcompiling    "
        sleep 0.5
        printf "\rcompiling .  "
        sleep 0.5
        printf "\rcompiling .. "
        sleep 0.5
        printf "\rcompiling ..."
        sleep 0.5
    done
} &

export RUNNING_PID=$!

# We might need a separate output dir in `out` due to tikz-externalize.
mkdir -p out/out/

# First only compile the template producing a raw memory image of the compiler state.
# This can be used in consecutive runs to have a head-start instead of re-compiling the template every time.
if [ ! -f "$SCRIPT_DIR/out/template.fmt" ]; then
    pdflatex -ini -jobname="$SCRIPT_DIR/out/template" "&pdflatex" mylatexformat.ltx "$SCRIPT_DIR/main.tex" > /dev/null
fi
