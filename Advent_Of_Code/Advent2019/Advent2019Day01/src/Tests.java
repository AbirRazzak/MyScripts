import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;

public class Tests {

    @Test
    public void testFuelCalculation() {
        FuelCalculator fuelCalc = new FuelCalculator(null, null);

        int massToTest = 12;
        int fuelExpected = 2;
        int fuelActual = fuelCalc.convertMassToFuel(massToTest);
        Assert.assertEquals(fuelExpected, fuelActual);

        massToTest = 14;
        fuelExpected = 2;
        fuelActual = fuelCalc.convertMassToFuel(massToTest);
        Assert.assertEquals(fuelExpected, fuelActual);

        massToTest = 1969;
        fuelExpected = 654;
        fuelActual = fuelCalc.convertMassToFuel(massToTest);
        Assert.assertEquals(fuelExpected, fuelActual);

        massToTest = 100756;
        fuelExpected = 33583;
        fuelActual = fuelCalc.convertMassToFuel(massToTest);
        Assert.assertEquals(fuelExpected, fuelActual);
    }

    @Test
    public void testReadingFile() {
        MassInputReader reader = new MassInputReader("testInputFile.txt", null);
        String expected = "This is a test file\n" +
                "Making sure that the InputReader works properly\n" +
                "I sure hope it does\n";

        String actual = null;
        try {
            actual = reader.readFile();
        } catch (IOException e) {
            e.printStackTrace();
        }

        Assert.assertEquals(expected, actual);
    }
}
