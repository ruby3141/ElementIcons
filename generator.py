# SPDX-License-Identifier: MIT

import string, subprocess
from typing import List

inkscape_location = "C:/Program Files/Inkscape/bin/inkscape.com"

template_file = open("template.svg", "r")
template = string.Template(template_file.read())

data_file = open("elements.csv", "r")
data = {}
processes: List[subprocess.Popen] = []
for element in data_file.readlines():
    data["number"], data["name"], data["symbol"] = element.strip().split(",")
    p = subprocess.Popen([inkscape_location, "-p", f"--export-filename=./result/{data['number']}_{data['name']}.png", "-C"],
                   stdin=subprocess.PIPE, text=True)
    try:
        p.communicate(input=template.substitute(data), timeout=0)
    except subprocess.TimeoutExpired:
        pass

    processes.append(p)

for process in processes:
    process.wait()
