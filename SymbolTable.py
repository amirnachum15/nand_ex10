STATIC = "static"
VAR = "var"
FIELD = "field"
ARG = "argument"
CLASS_SCOPE = [STATIC, FIELD]
SUBROUTINE_SCOPE = [VAR, ARG]
KINDS = CLASS_SCOPE + SUBROUTINE_SCOPE

class SymbolTable:
    def __init__(self):
        self.class_level_table = {}
        self.subroutine_table = {}

    #this function should be called whenever you start a new subroutine
    def start_subroutine(self):
        self.subroutine_table = {}

    def define(self, name, type, kind):
        """
        :param name: name of the variable
        :param type: the type of the variable e.g int, boolean, class_name, etc
        :param kind: STATIC, FIELD, ARG, VAR
        :return:
        """
        if kind in CLASS_SCOPE:
            self.class_level_table[name] =

    def var_count(self, kind):
        """
        :param kind: static, field, arg, var
        :return: num of variables of this kind
        """



    def kind_of(self, name):
        """
        :param name: string - name of variable
        :return: the variable kine e.g static, field, arg or var
        """

    def type_of(self, name):
        """
        :param name: string - the name of the variable
        :return: the type of the variable e.g (int, boolean, class_name)
        """

    def index_of(self, name):
        """
        :param name: string - the name of the variable
        :return: int - the index in the appropriate stack
        """