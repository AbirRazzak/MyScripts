import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class MassInputReader extends Filter {

    private String fileName;

    public MassInputReader(String fileName, Pipe output_) {
        super(null, output_);
        this.fileName = fileName;
    }

    @Override
    protected void transform() {
        try {
            BufferedReader reader =
                    new BufferedReader(new FileReader(fileName));

            String currentLine;
            while ((currentLine = reader.readLine()) != null) {
                output_.put(currentLine);
            }

            reader.close();
            output_.put("STOP");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    String readFile() throws IOException {
        String lines = "";
        BufferedReader reader =
                new BufferedReader(new FileReader(fileName));

        String currentLine = reader.readLine();
        while (currentLine != null) {
            lines += currentLine;
            lines += "\n";
            currentLine = reader.readLine();
        }

        reader.close();
        return lines;
    }
}
