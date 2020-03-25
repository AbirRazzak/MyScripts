import java.util.ArrayList;

public class IntCodeComputer {

    private ArrayList<Integer> opcodeProgram;

    public IntCodeComputer(ArrayList<Integer> program) {
        opcodeProgram = program;
    }

    public void setOpcodeTo(int opcodeIndex, int opcode) {
        opcodeProgram.set(opcodeIndex, opcode);
    }

    public int getOpcodeAt(int opcodeIndex) {
        return opcodeProgram.get(opcodeIndex);
    }

    public void runProgram() {
        int currentOpcodeIndex = 0;
        while(currentOpcodeIndex < opcodeProgram.size()) {
            int currentOpcode = opcodeProgram.get(currentOpcodeIndex);
            if(currentOpcode == 99) return;
            else {
                performOpcode(currentOpcodeIndex, currentOpcode);
                currentOpcodeIndex += 4;
            }
        }
    }

    private void performOpcode(int opcodeIndex, int opcode) {
        int index1 = opcodeIndex + 1;
        int index2 = opcodeIndex + 2;
        int index3 = opcodeIndex + 3;

        if(opcode == 1) addAndStore(index1, index2, index3);
        else if (opcode == 2) multiplyAndStore(index1, index2, index3);
    }

    private void addAndStore(int opcodeIndex1, int opcodeIndex2, int opcodeIndex3) {
        int value1 = opcodeProgram.get(opcodeProgram.get(opcodeIndex1));
        int value2 = opcodeProgram.get(opcodeProgram.get(opcodeIndex2));
        int storageIndex = opcodeProgram.get(opcodeIndex3);
        opcodeProgram.set(storageIndex, value1 + value2);
    }

    private void multiplyAndStore(int opcodeIndex1, int opcodeIndex2, int opcodeIndex3) {
        int value1 = opcodeProgram.get(opcodeProgram.get(opcodeIndex1));
        int value2 = opcodeProgram.get(opcodeProgram.get(opcodeIndex2));
        int storageIndex = opcodeProgram.get(opcodeIndex3);
        opcodeProgram.set(storageIndex, value1 * value2);
    }
}
