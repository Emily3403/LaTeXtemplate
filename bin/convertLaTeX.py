#!/usr/bin/env python3
import os
import re
from pathlib import Path


# This is an attempt at bundling all referenced includes from a single tex file into a single one again.
# It does not work currently.

def main() -> None:
    with open("main.tex") as f:
        _commit_hash = re.findall("Generated with commit hash: \"(.*?)\"", f.read())

    if len(_commit_hash) != 1:
        print(f"Could not get the commit hash: {_commit_hash = }")
        exit(1)

    commit_hash = _commit_hash[0]
    os.system(f"cd src; git checkout {commit_hash}")

    files = {}
    for file in Path("src").rglob("*"):
        if file.is_file():
            with file.open() as f:
                files[os.path.splitext(file.name)[0]] = f"\n\n\n% --- Start of file {file.name} ---\n{f.read()}\n% -/- End of file {file.name} ---\n\n\n"

    output_buffer = []

    with open("src/template.sty") as f:
        for line in f.readlines():
            package = re.match(" *\\\\(?:RequirePackage|usepackage){(.*)} *", line)
            if package is None:
                output_buffer.append(line)
                continue

            assert len(package.groups()) == 1
            if (pack := package.groups()[0]) in files:
                output_buffer.append(files[pack])

    with open("converted.sty", "w") as f:
        f.write("".join(output_buffer))



if __name__ == '__main__':
    main()
