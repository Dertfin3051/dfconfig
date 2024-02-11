# DF Config
# Use Documentation.docx for learn functions


_version = "0.2b"


def checkForDFC(file):
    if file[-4:] == ".dfc":
        return True
    else:
        return False


# def checkType(context):
#     if type(context) == str:
#         return "String"
#     elif type(context) == int:
#         return "Integer"
#     elif type(context) == float:
#         return "Float"
#     elif type(context) == bool:
#         return "Boolean"


def getString(file, variable):
    with open(file, "r", encoding = 'utf-8') as cfg_file:
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
        return "Variable not found!"


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
        return "Variable not found!"


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
        return "Variable not found!"


def getBoolean(file, variable):
    with open(file, "r", encoding='utf-8') as cfg_file:
        cfg_lines = cfg_file.readlines()
    tech_var_name = "_" + variable + "_"
    for i in range(len(cfg_lines)):
        if tech_var_name in cfg_lines[i]:
            if "\n" in cfg_lines[i]:
                boolean = cfg_lines[i][len(tech_var_name + ' = '):(len(cfg_lines[i]) - 1)]
            else:
                boolean = cfg_lines[i][len(tech_var_name + ' = '):len(cfg_lines[i])]
            if boolean.lower() == "true":
                return True
            elif boolean.lower() == "false":
                return False
            else:
                return "Non-correct boolean used in .dfc file! Use True/False"
        else:
            i += 1
    else:
        return "Variable not found!"


def setString(file, variable, context):
    with open(file, "r", encoding='utf-8') as cfg_file_r:
        cfg_lines = cfg_file_r.readlines()
    tech_var_name = "_" + variable + "_"
    for i in range(len(cfg_lines)):
        if tech_var_name in cfg_lines[i]:
            cfg_lines[i] = tech_var_name + " = \"" + str(context) + "\"\n"
            with open(file, "w", encoding='utf-8') as cfg_file_w:
                cfg_file_w.writelines(cfg_lines)
            return variable + " successfully replaced to " + str(context)
        else:
            i += 1
    else:
        return "Variable not found"


def setInteger(file, variable, context):
    with open(file, "r", encoding='utf-8') as cfg_file_r:
        cfg_lines = cfg_file_r.readlines()
    tech_var_name = "_" + variable + "_"
    for i in range(len(cfg_lines)):
        if tech_var_name in cfg_lines[i]:
            cfg_lines[i] = tech_var_name + " = " + str(context) + "\n"
            with open(file, "w", encoding='utf-8') as cfg_file_w:
                cfg_file_w.writelines(cfg_lines)
            return variable + " successfully replaced to " + str(context)
        else:
            i += 1
    else:
        return "Variable not found"


def setFloat(file, variable, context):
    with open(file, "r", encoding='utf-8') as cfg_file_r:
        cfg_lines = cfg_file_r.readlines()
    tech_var_name = "_" + variable + "_"
    for i in range(len(cfg_lines)):
        if tech_var_name in cfg_lines[i]:
            cfg_lines[i] = tech_var_name + " = " + str(context) + "\n"
            with open(file, "w", encoding='utf-8') as cfg_file_w:
                cfg_file_w.writelines(cfg_lines)
            return variable + " successfully replaced to " + str(context)
        else:
            i += 1
    else:
        return "Variable not found"


def setBoolean(file, variable, context):
    with open(file, "r", encoding='utf-8') as cfg_file_r:
        cfg_lines = cfg_file_r.readlines()
    tech_var_name = "_" + variable + "_"
    for i in range(len(cfg_lines)):
        if tech_var_name in cfg_lines[i]:
            cfg_lines[i] = tech_var_name + " = " + str(context) + "\n"
            with open(file, "w", encoding='utf-8') as cfg_file_w:
                cfg_file_w.writelines(cfg_lines)
            return variable + " successfully replaced to " + str(context)
        else:
            i += 1
    else:
        return "Variable not found"


def exist(file, variable):
    with open(file, "r", encoding='utf-8') as cfg_file_r:
        cfg_lines = cfg_file_r.readlines()
    tech_var_name = "_" + variable + "_"
    for i in range(len(cfg_lines)):
        if tech_var_name in cfg_lines[i]:
            return True
        else:
            i += 1
    return False

def add(file, variable, content):
    with open(file, "r", encoding='utf-8') as cfg_file_r:
        cfg_lines = cfg_file_r.readlines()
    tech_var_name = "_" + variable + "_"
    cfg_lines.append(tech_var_name)
    if type(content) == int:
        setInteger(file, variable, content)
    elif type(content) == str:
        setString(file, variable, content)
    elif type(content) == float:
        setFloat(file, variable, content)
    elif type(content) == bool:
        setBoolean(file, variable, content)