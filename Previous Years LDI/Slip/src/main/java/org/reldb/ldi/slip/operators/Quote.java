package org.reldb.ldi.slip.operators;

import org.reldb.ldi.slip.values.Operator;
import org.reldb.ldi.slip.values.Resolver;
import org.reldb.ldi.slip.values.Value;
import org.reldb.ldi.slip.values.Walker;

/** (quote parm1 parm2 ... parmn) */
public class Quote extends Operator {

	private static final long serialVersionUID = 0;
	
	/** Defer evaluation of list by returning its Value rather than executing it. */
	public Value evaluate(Resolver resolver, Walker args) {
		return args.rest();
	}
	
	/** Obtain operator name. */
	public String getOperatorName() {
		return "quote";
	}
}
