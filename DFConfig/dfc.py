# DF Config
# Use Documentation.txt for learn functions


_version = "0.1.4b"


def getString(file, variable):
    with open(file, "r", encoding='utf-8') as cfg_file:
        cfg_lines = cfg_file.readlines()
    tech_var_name = "_" + variable + "_"
    for i in range(len(cfg_lines)):
        if tech_var_name in cfg_lines[i]:
            if "\n" in cfg_lines[i]:
                string_text = cfg_lines[i][len(tech_var_name + ' = "'):(len(cfg_lines[i]) - 2)]
            else:
                string_text = cfg_lines[i][len(tech_var_name + ' = "'):(len(cfg_lines[i]) - 1)]
            return string_text
        else:
            i += 1
    else:
        return "empty"


def getInteger(file, variable):
    with open(file, "r", encoding='utf-8') as cfg_file:
        cfg_lines = cfg_file.readlines()
    tech_var_name = "_" + variable + "_"
    for i in range(len(cfg_lines)):
        if tech_var_name in cfg_lines[i]:
            if "\n" in cfg_lines[i]:
                integer = int(cfg_lines[i][len(tech_var_name + ' = '):(len(cfg_lines[i]) - 1)])
            else:
                integer = int(cfg_lines[i][len(tech_var_name + ' = '):len(cfg_lines[i])])
            return integer
        else:
            i += 1
    else:
        return 0


def getFloat(file, variable):
    with open(file, "r", encoding='utf-8') as cfg_file:
        cfg_lines = cfg_file.readlines()
    tech_var_name = "_" + variable + "_"
    for i in range(len(cfg_lines)):
        if tech_var_name in cfg_lines[i]:
            if "\n" in cfg_lines[i]:
                flt = float(cfg_lines[i][len(tech_var_name + ' = '):(len(cfg_lines[i]) - 1)])
            else:
                flt = float(cfg_lines[i][len(tech_var_name + ' = '):len(cfg_lines[i])])
            return flt
        else:
            i += 1
    else:
        return 0.0

