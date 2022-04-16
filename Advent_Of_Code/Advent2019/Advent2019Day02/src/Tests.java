import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class Tests {

    @Test
    public void testParseInput() {
        String input = "1,2,3,4,5";
        ArrayList<Integer> expected = new ArrayList<>(
                List.of(1, 2, 3, 4, 5)
        );
        ArrayList<Integer> actual = InputParser.parseInput(input);

        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testRunProgram() {
        ArrayList<Integer> program = InputParser.parseInput("1,9,10,3,2,3,11,0,99,30,40,50");
        IntCodeComputer computer = new IntCodeComputer(program);
        computer.runProgram();

        Assert.assertEquals(3500, computer.getOpcodeAt(0));
    }
}
