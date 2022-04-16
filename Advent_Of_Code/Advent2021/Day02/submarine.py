import abc
from enum import Enum

from pydantic import BaseModel


class SubmarineCommandType(str, Enum):
    forward = 'forward'
    down = 'down'
    up = 'up'


class SubmarineCommand(BaseModel):
    type: SubmarineCommandType
    quantity: int


class SubmarineInstruction(BaseModel):
    instruction: str

    def to_command(self) -> SubmarineCommand:
        command_components = self.instruction.split()

        command_type = command_components[0]
        command_quantity = int(command_components[1])

        return SubmarineCommand(
            type=SubmarineCommandType(command_type),
            quantity=command_quantity
        )


class Submarine(BaseModel, abc.ABC):
    horizontal_position: int = 0
    depth: int = 0

    @abc.abstractmethod
    def execute(
        self,
        command: SubmarineCommand
    ):
        pass


class SubmarinePart1(Submarine):
    def execute(
        self,
        command: SubmarineCommand,
    ):
        if command.type == SubmarineCommandType.forward:
            self.horizontal_position += command.quantity
        elif command.type == SubmarineCommandType.down:
            self.depth += command.quantity
        elif command.type == SubmarineCommandType.up:
            self.depth -= command.quantity


class SubmarinePart2(Submarine):
    aim: int = 0

    def execute(
        self,
        command: SubmarineCommand
    ):
        if command.type == SubmarineCommandType.forward:
            self.horizontal_position += command.quantity
            self.depth += self.aim * command.quantity
        elif command.type == SubmarineCommandType.down:
            self.aim += command.quantity
        elif command.type == SubmarineCommandType.up:
            self.aim -= command.quantity
