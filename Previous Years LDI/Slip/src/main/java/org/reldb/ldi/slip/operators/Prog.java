package org.reldb.ldi.slip.operators;

import org.reldb.ldi.slip.values.Operator;
import org.reldb.ldi.slip.values.Resolver;
import org.reldb.ldi.slip.values.Value;
import org.reldb.ldi.slip.values.Walker;

/** (prog parm1 parm2 ... parmn) */
public class Prog extends Operator {

	private static final long serialVersionUID = 0;
	
	/** Sequentially evaluate each item in a list. */
	public Value evaluate(Resolver resolver, Walker args) {
		return evaluateBody(resolver, args);
	}
	
	/** Obtain operator name. */
	public String getOperatorName() {
		return "prog";
	}
}
