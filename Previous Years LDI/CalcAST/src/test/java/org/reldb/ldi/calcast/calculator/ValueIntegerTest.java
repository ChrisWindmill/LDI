package org.reldb.ldi.calcast.calculator;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class ValueIntegerTest {
	ValueInteger one = new ValueInteger(1);
	ValueInteger negfive = new ValueInteger(-5);
	ValueInteger ten = new ValueInteger(10);

	@Test
	void oneIsJavaOne() {
		assertThat(one.intValue()).isEqualTo(1);
	}

	@Test
	void tenMinusOneIsNine() {
		assertThat(ten.subtract(one).intValue()).isEqualTo(9);
	}

	@Test
	void tenDivNegFiveIsNegTwo() {
		assertThat(ten.div(negfive).intValue()).isEqualTo(-2);
	}

	@Test
	void tenIsGreaterThanOne() {
		assertThat(ten.gt(one).booleanValue()).isTrue();
	}
}
