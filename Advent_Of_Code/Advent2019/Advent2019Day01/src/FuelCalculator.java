public class FuelCalculator extends Filter {

    public FuelCalculator(Pipe input_, Pipe output_) {
        super(input_, output_);
    }

    @Override
    protected void transform() {
        try {
            Object currentInput = input_.get();
            int i = 1;
            while (currentInput != null && !currentInput.equals("STOP")) {
                int massToConvert = Integer.parseInt(currentInput.toString());
                int currentFuelCalculation = convertMassToFuel(massToConvert);
                System.out.println(i + ". " + massToConvert + " -> " + currentFuelCalculation);
                output_.put(currentFuelCalculation);
                i++;
                currentInput = input_.get();
            }

            if(currentInput == "STOP") {
                output_.put("STOP");
            }

            if(currentInput == null) {
                throw new NullPointerException("Fuel Calculator received a null from its input pipe.");
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    int convertMassToFuel(int mass) {
        return (mass / 3) - 2;
    }
}
