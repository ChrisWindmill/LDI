package org.reldb.ldi.sili.values;

import java.io.PrintStream;
import java.io.Serializable;

/** An abstract Value, that defines all possible operations on abstract ValueS.
 * 
 *  If an operation is not supported, throw SemanticException.
 */
public interface Value extends Serializable, Comparable<Value> {
	
	/** Output name of the type of this Value. */
	public String getTypeName();
	
	/** Output this Value to a PrintStream. */
	public void toStream(PrintStream p, int depth);
	
	/** Write as parsable string. */
	public String toParsableString();
	
	/** Write as final string. */
	public String toString();
	
	/** Compare this value and another. */
	public int compareTo(Value v);

	/** Check for equality. */
	public boolean equals(Object o);
	
	/** Perform logical XOR on this value and another. */
	public Value xor(Value v);
	
	/** Perform logical OR on this value and another. */
	public Value or(Value v);
	
	/** Perform logical AND on this value and another. */
	public Value and(Value v);
	
	/** Perform logical NOT on this value. */  
	public Value not();
	
	/** Add this value to another. */
	public Value add(Value v);
	
	/** Subtract another value from this. */
	public Value subtract(Value v);
	
	/** Multiply this value with another. */
	public Value mult(Value v);
	
	/** Divide another value by this. */
	public Value div(Value v);
	
	/** Return unary plus of this value. */
	public Value unary_plus();
	
	/** Return unary minus of this value. */
	public Value unary_minus();
	
	/** Convert this to a primitive boolean. */
	public boolean booleanValue();
	
	/** Convert this to a primitive long. */
	public long longValue();
	
	/** Convert this to a primitive double. */
	public double doubleValue();

	/** Convert this to a primitive string. */
	public String stringValue();
	
	/** Test this value and another for equality. */
	public Value eq(Value v);
	
	/** Test this value and another for non-equality. */
	public Value neq(Value v);
	
	/** Test this value and another for >= */
	public Value gte(Value v);
	
	/** Test this value and another for <= */
	public Value lte(Value v);
	
	/** Test this value and another for > */
	public Value gt(Value v);
	
	/** Test this value and another for < */	
	public Value lt(Value v);
}
