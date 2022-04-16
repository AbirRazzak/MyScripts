import pytest

from Day02.submarine import (
    SubmarineInstruction,
    SubmarineCommand,
    SubmarinePart1,
    SubmarineCommandType,
    SubmarinePart2
)


@pytest.mark.parametrize(
    'instruction, expected_command',
    [
        ('forward 5', SubmarineCommand(type=SubmarineCommandType('forward'), quantity=5)),
        ('down 4', SubmarineCommand(type=SubmarineCommandType('down'), quantity=4)),
        ('up 3', SubmarineCommand(type=SubmarineCommandType('up'), quantity=3))
    ]
)
def test_submarine_instruction_to_command_forward(instruction, expected_command):
    sub_instruction = SubmarineInstruction(instruction=instruction)
    result = sub_instruction.to_command()

    assert result == expected_command


def test_submarine1_execute():
    command1 = SubmarineCommand(type=SubmarineCommandType('forward'), quantity=5)
    command2 = SubmarineCommand(type=SubmarineCommandType('down'), quantity=4)
    command3 = SubmarineCommand(type=SubmarineCommandType('up'), quantity=2)
    expected_submarine = SubmarinePart1(horizontal_position=5, depth=2)

    submarine = SubmarinePart1()
    submarine.execute(command1)
    submarine.execute(command2)
    submarine.execute(command3)

    assert submarine == expected_submarine


def test_submarine2_execute():
    command1 = SubmarineCommand(type=SubmarineCommandType('down'), quantity=4)
    command2 = SubmarineCommand(type=SubmarineCommandType('up'), quantity=2)
    command3 = SubmarineCommand(type=SubmarineCommandType('forward'), quantity=5)
    expected_submarine = SubmarinePart2(horizontal_position=5, depth=10, aim=2)

    submarine = SubmarinePart2()
    submarine.execute(command1)
    submarine.execute(command2)
    submarine.execute(command3)

    assert submarine == expected_submarine
