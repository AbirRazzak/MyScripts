import java.util.ArrayList;

public class InputParser {

    public static ArrayList<Integer> parseInput(String input) {
        ArrayList<Integer> convertedIntInputs = new ArrayList<>();
        String[] stringInputs = input.split(",");
        for (String stringInput : stringInputs) {
            convertedIntInputs.add(Integer.parseInt(stringInput));
        }
        return convertedIntInputs;
    }
}
