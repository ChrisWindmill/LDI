package org.reldb.ldi.slip.operators;

import org.reldb.ldi.slip.values.Value;

/** (- parm1 parm2 ... parmn) */
public class Subtract extends Accumulator {

	private static final long serialVersionUID = 0;

	/** Accumulate right Value into left using appropriate operator. */
	Value accumulate(Value left, Value right) {
		return left.subtract(right);
	}
	
	/** Obtain operator name. */
	public String getOperatorName() {
		return "-";
	}
}
