from abc import abstractmethod
from enum import IntEnum, Enum

int_code = [1002, 4, 3, 4, 33]
# int_code = [2,4,4,5,99,0]


class VirtualMachine:
    def __init__(self, initial_state):
        self.next = 0
        self.memory = [0] * len(initial_state)
        for index, value in enumerate(initial_state):
            self.memory[index] = value

    def write(self, address, value):
        self.memory[address] = value

    def read(self, address):
        return self.memory[address]

    def read_next(self):
        value = self.memory[self.next]
        self.next += 1
        return value

    def __str__(self):
        return str(self.memory)


class Operations(IntEnum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    HALT = 99


class ParameterType(Enum):
    POSITION = 0
    IMMEDIATE = 1
    Halt = 99


def parameter(value, parameter_type):
    if parameter_type == ParameterType.POSITION.value:
        return PositionParameter(value)
    else:
        return ImmediateParameter(value)


class Parameter:
    def __init__(self, value):
        self.value = value


class PositionParameter(Parameter):
    pass


class ImmediateParameter(Parameter):
    pass


class Parser:
    @staticmethod
    def parse_operation(vm):
        operation = vm.read_next()
        if operation > 99:
            command = Parser.parse_parameter_operation(operation, vm)
        else:
            command = Parser.parse_position_operation(operation, vm)
        return command

    @staticmethod
    def parse_parameter_operation(operation, vm):
        command = None
        instruction_as_string = str(operation)
        operation = int(instruction_as_string[-2:])
        if operation == Operations.ADD or operation == Operations.MULTIPLY:
            first_parameter_mode = int(instruction_as_string[-3])
            second_parameter_mode = int(instruction_as_string[-4])
            try:
                store_at_parameter_mode = int(instruction_as_string[-5])
            except IndexError:
                store_at_parameter_mode = 0
            first = parameter(vm.read_next(), first_parameter_mode)
            second = parameter(vm.read_next(), second_parameter_mode)
            value = parameter(vm.read_next(), store_at_parameter_mode)
            if operation == Operations.ADD:
                command = Add(first, second, value)
            else:
                command = Multiply(first, second, value)
        if operation == Operations.INPUT or operation == Operations.OUTPUT:
            store_at_parameter_mode = int(instruction_as_string[0])
            value = parameter(vm.read_next(), store_at_parameter_mode)
            if operation == Operations.INPUT:
                command = Input(value)
            else:
                command = Output(value)
        if operation == Operations.HALT:
            command = Halt()
        return command

    @staticmethod
    def parse_position_operation(operation, vm):
        command = None
        if operation == Operations.ADD:
            first = PositionParameter(vm.read_next())
            second = PositionParameter(vm.read_next())
            store_at = ImmediateParameter(vm.read_next())
            command = Add(first, second, store_at)
        elif operation == Operations.MULTIPLY:
            first = PositionParameter(vm.read_next())
            second = PositionParameter(vm.read_next())
            store_at = ImmediateParameter(vm.read_next())
            command = Multiply(first, second, store_at)
        elif operation == Operations.INPUT:
            store_at = vm.read_next()
            command = Input(store_at)
        elif operation == Operations.OUTPUT:
            read_from = vm.read_next()
            command = Output(read_from)
        elif operation == Operations.HALT:
            command = Halt()
        return command


class Command:
    @abstractmethod
    def execute(self, memory):
        pass


class ThreeParamCommand(Command):
    def __init__(self, first, second, store_at):
        self.first = first
        self.second = second
        self.store_at = store_at

    def load_values(self, vm):
        first = vm.read(self.first.value) if isinstance(self.first, PositionParameter) else self.first.value
        second = vm.read(self.second.value) if isinstance(self.second, PositionParameter) else self.second.value
        address = self.store_at.value
        return first, second, address

    @abstractmethod
    def execute(self, vm):
        pass


class Halt(Command):
    def execute(self, vm):
        pass


class Input(Command):
    def __init__(self, store_at):
        self.store_at = store_at

    def execute(self, vm):
        value = input("INPUT PLZ: ")
        if isinstance(self.store_at, ImmediateParameter):
            vm.write(self.store_at, value)
        else:
            vm.write(vm.read(self.store_at), value)


class Output(Command):
    def __init__(self, read_from):
        self.read_from = read_from

    def execute(self, vm):
        if self.read_from[0] == ParameterType.IMMEDIATE:
            vm.read(self.read_from)


class Add(ThreeParamCommand):
    def execute(self, memory):
        first, second, address = self.load_values(memory)
        result = first + second
        memory[address] = result


class Multiply(ThreeParamCommand):
    def execute(self, vm):
        first, second, address = self.load_values(vm)
        result = first * second
        vm.write(address, result)


if __name__ == '__main__':
    virtualMachine = VirtualMachine(int_code)
    to_execute = Parser.parse_operation(virtualMachine)
    while not isinstance(to_execute, Halt):
        to_execute.execute(virtualMachine)
        to_execute = Parser.parse_operation(virtualMachine)
    print(virtualMachine)
