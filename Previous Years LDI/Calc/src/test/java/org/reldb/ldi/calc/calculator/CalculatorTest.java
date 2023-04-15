package org.reldb.ldi.calc.calculator;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class CalculatorTest {
	private Calculator calc = new Calculator();

	@Test
	void tenPlusTwo() {
		calc.push_integer("10");
		calc.push_integer("2");
		calc.add();
		assertThat(calc.pop().intValue()).isEqualTo(12);
	}

	@Test
	void tenMinusTwo() {
		calc.push_integer("10");
		calc.push_integer("2");
		calc.subtract();
		assertThat(calc.pop().intValue()).isEqualTo(8);
	}

	@Test
	void tenDivTwo() {
		calc.push_integer("10");
		calc.push_integer("2");
		calc.div();
		assertThat(calc.pop().intValue()).isEqualTo(5);
	}
}
