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
        :return: True if succeeded in defining, false otherwise
        """

        if name in [self.subroutine_table.keys(), self.class_level_table.keys()]:
            # this is not a new variable
            return True

        # this is a new variable
        index = self.var_count(kind) + 1
        if kind in CLASS_SCOPE:
            self.class_level_table[name] = [index, kind, type]
            return True
        elif kind in SUBROUTINE_SCOPE:
            self.subroutine_table[name] = [index, kind, type]
            return True
        return False

    def var_count(self, kind):
        """
        :param kind: static, field, arg, var
        :return: int - num of variables of this kind
        """
        if kind in CLASS_SCOPE:
            #we substract 1, because the indexes are saved from 0 and not 1
            return len([item for item in self.class_level_table.values() if item[1] == kind]) - 1
        elif kind in SUBROUTINE_SCOPE:
            # we substract 1, because the indexes are saved from 0 and not 1
            return len([item for item in self.subroutine_table.values() if item[1] == kind]) - 1
        return 0

    def kind_of(self, name):
        """
        :param name: string - name of variable
        :return: the variable kine e.g static, field, arg or var
        """
        try:
            return self.class_level_table[name][1]
        except:
            try:
                return self.subroutine_table[name][1]
            except:
                #the given variable does not exist
                return None

    def type_of(self, name):
        """
        :param name: string - the name of the variable
        :return: the type of the variable e.g (int, boolean, class_name)
        """
        try:
            return self.class_level_table[name][2]
        except:
            try:
                return self.subroutine_table[name][2]
            except:
                #the given variable does not exist
                return None

    def index_of(self, name):
        """
        :param name: string - the name of the variable
        :return: int - the index in the appropriate stack
        """
        try:
            return self.class_level_table[name][0]
        except:
            try:
                return self.subroutine_table[name][0]
            except:
                #the given variable does not exist
                return None