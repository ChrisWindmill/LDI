package sili.values;

import org.junit.jupiter.api.Test;
import org.reldb.ldi.sili.values.ValueInteger;

import static org.assertj.core.api.Assertions.assertThat;

class ValueIntegerTest {
	ValueInteger one = new ValueInteger(1);
	ValueInteger negfive = new ValueInteger(-5);
	ValueInteger ten = new ValueInteger(10);

	@Test
	void oneIsJavaOne() {
		assertThat(one.longValue()).isEqualTo(1);
	}

	@Test
	void tenMinusOneIsNine() {
		assertThat(ten.subtract(one).longValue()).isEqualTo(9);
	}

	@Test
	void tenDivNegFiveIsNegTwo() {
		assertThat(ten.div(negfive).longValue()).isEqualTo(-2);
	}

	@Test
	void tenIsGreaterThanOne() {
		assertThat(ten.gt(one).booleanValue()).isTrue();
	}
}
