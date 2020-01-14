# segments constants
CONST = "const"
ARG = "arg"
LOCAL = "local"
STATIC = "static"
THIS = "this"
THAT = "that"
POINTER = "pointer"
TEMP = "temp"
SEGMENTS = [CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP]

# arithmetic commands constants
ADD = "add"
SUB = "sub"
NEG = "neg"
EQ = "eq"
GT = "gt"
LT = "lt"
AND = "and"
OR = "or"
NOT = "not"
COMMANDS = [ADD, SUB, NEG, EQ, GT, LT, AND, OR, NOT]

ALL_CONSTANTS = [COMMANDS, SEGMENTS]

class VMWriter:
    def __init__(self, outputfile):
        """
        :param outputfile: string - name of outputfile
        """
        self.file = open(outputfile, "w")

    def write_push(self, segment, index):
        """
        :param segment: segment e.g (CONST, ARG, ,LOCAL, STATIC, THIS, THAT, POINTER, TEMP)
        :param index: integer
        :return:
        """
        output = f"push {segment} {index}"
        self.write_line_to_file(output)

    def write_pop(self, segment, index):
        """
        :param segment: segment e.g (CONST, ARG, ,LOCAL, STATIC, THIS, THAT, POINTER, TEMP)
        :param index: integer
        :return:
        """
        output = f"pop {segment} {index}"
        self.write_line_to_file(output)

    def write_arithmetic(self, command):
        """
        :param command: ADD, SUB, NEG, EQ, GT, LT, AND, OR, NOT
        :return:
        """
        if command not in COMMANDS:
            print("unknown command")
        else:
            self.write_line_to_file(command)
        return

    def write_label(self, label):
        """
        :param label: string
        :return:
        """
        self.write_line_to_file(label)
        return

    def write_goto(self, label):
        """
        :param label: string
        :return:
        """
        output = f"goto {label}"
        self.write_line_to_file(output)

    def write_if(self, label):
        """
        :param label: string
        :return:
        """
        output = f"if-goto {label}"
        self.write_line_to_file(output)

    def write_call(self, name, num_args):
        """
        :param name: name of function to call to
        :param num_args: number of arguments the function takes
        :return:
        """
        output = f"call {name} {num_args}"
        self.write_line_to_file(output)

    def write_function(self, name, num_locals):
        """
        :param name: name of function to declare
        :param num_locals: number of local variables this function uses
        :return:
        """
        output = f"function {name} {num_locals}"
        self.write_line_to_file(output)

    def write_return(self):
        output = "ret"
        self.write_line_to_file(output)

    def write_line_to_file(self, line):
        self.file.write(line)

    def write_lines_to_file(self, lines):
        for line in lines:
            self.write_line_to_file(line)

    def close(self):
        self.file.close()
