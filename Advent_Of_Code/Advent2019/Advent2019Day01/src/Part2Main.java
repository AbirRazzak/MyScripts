public class Part2Main {

    public static void main(String[] args) {
        Pipe reader_calc = new PipeImpl();
        Pipe calc_counter = new PipeImpl();

        Filter reader = new MassInputReader("part1input.txt", reader_calc);
        Filter calculator = new AdvancedFuelCalculator(reader_calc, calc_counter);
        Filter counter = new FuelCounter(calc_counter);

        reader.start();
        calculator.start();
        counter.start();

        reader.stop();
        calculator.stop();
        counter.stop();
    }
}
