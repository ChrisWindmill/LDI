/** Convenient runner for Calc org.reldb.ldi.calc package. */

public class Calc {
	public static void main(String[] args) {
		while (true)
			try {
				org.reldb.ldi.calc.parser.Calc.main(args);
			} catch (Throwable t) {
				System.out.println("Error: " + t);
			}
	}
}
