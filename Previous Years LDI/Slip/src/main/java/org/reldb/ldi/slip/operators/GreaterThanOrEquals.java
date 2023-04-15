package org.reldb.ldi.slip.operators;

import org.reldb.ldi.slip.values.Value;

/** (>= parm1 parm2 ... parmn) */
public class GreaterThanOrEquals extends Comparison {

	private static final long serialVersionUID = 0;
	
	boolean comparison(Value left, Value right) {
		return left.gte(right).booleanValue();
	}

	public String getOperatorName() {
		return ">=";
	}

}
