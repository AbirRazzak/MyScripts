public class FuelCounter extends Filter {

    private int totalFuel;

    public FuelCounter(Pipe input_) {
        super(input_, null);
        totalFuel = 0;
    }

    @Override
    protected void transform() {
        try {
            Object currentInput = input_.get();
            while (currentInput != null && currentInput != "STOP") {
                int fuelToAdd = (int) currentInput;
                totalFuel += fuelToAdd;
                currentInput = input_.get();
            }

            System.out.println(totalFuel);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    int getTotalFuel() {
        return totalFuel;
    }
}
