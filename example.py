# Importing library
from DFConfig import dfc

# Getting String variable data
# Make new variable in code or use print()
# Получаем данные из переменной типа String
# Создайте новую переменную в коде или используйте print()
dfc.getString("example.dfc", "text")    # "Get" arguments is : File name and path, Variable name

# Let's change information to String variable!
# Давайте изменим данные в текстовой переменной
dfc.setString("example.dfc", "text", "This is new context :D")
# "Set" arguments is : File name and path, Variable name, New context

# Integer
dfc.getInteger()
dfc.setInteger()

# Float
dfc.getFloat()
dfc.setFloat()

# Boolean
dfc.getBoolean()
dfc.setBoolean()

