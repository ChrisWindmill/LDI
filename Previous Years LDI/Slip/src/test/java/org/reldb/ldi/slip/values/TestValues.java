package org.reldb.ldi.slip.values;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class TestValues {

	@Test
	public void testValueList() {
		Bunch v = new Bunch();
		v.insert(new Str("union"));
		v.insert(new Int(3));
		v.insert(new Int(4));
		Walker i = v.getWalker();
		Value p = i.next();
		assertEquals("union", p.toString());
		p = i.next();
		assertEquals("3", p.toString());
		p = i.next();
		assertEquals("4", p.toString());
		String s = v.toString();
		assertEquals("(union 3 4)", s);
	}

	@Test
	public void testValueInteger() {
		Int one = new Int(1);
		Int five = new Int(5);
		Int nFive = new Int(-5);
		assertEquals(6, one.add(five).longValue());
		assertEquals(-4, one.add(nFive).longValue());
		assertEquals(-25, nFive.mult(five).longValue());
	}

	@Test
	public void testValueBoolean() {
		Bool t = new Bool(true);
		Bool f = new Bool(false);
		assertTrue(t.neq(f).booleanValue());
		assertTrue(t.or(f).booleanValue());
		assertFalse(t.and(f).booleanValue());
	}

	@Test
	public void testValueDouble() {
		Rational onePointTwoFive = new Rational(1.25);
		Rational fivePointThree = new Rational(5.3);
		Rational nFivePointFourEight = new Rational(-5.48);
		assertEquals(6.55, onePointTwoFive.add(fivePointThree).doubleValue());
		assertEquals(-4.23, onePointTwoFive.add(nFivePointFourEight).doubleValue());
		assertEquals(-29.044, nFivePointFourEight.mult(fivePointThree).doubleValue());
	}

}
