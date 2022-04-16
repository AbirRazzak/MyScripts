public class AdvancedFuelCalculator extends FuelCalculator {

    public AdvancedFuelCalculator(Pipe input_, Pipe output_) {
        super(input_, output_);
    }

    @Override
    protected void transform() {
        try {
            Object currentInput = input_.get();
            while (currentInput != null && !currentInput.equals("STOP")) {
                int massToConvert = Integer.parseInt(currentInput.toString());
                advancedFuelCalculation(massToConvert);
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

    void advancedFuelCalculation(int initialMass) {
        int subFuel = convertMassToFuel(initialMass);
        if(subFuel > 0) {
            output_.put(subFuel);
            advancedFuelCalculation(subFuel);
        }
    }
}
