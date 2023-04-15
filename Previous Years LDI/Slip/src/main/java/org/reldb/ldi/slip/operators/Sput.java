package org.reldb.ldi.slip.operators;

import org.reldb.ldi.slip.values.*;

/** (sput parm1 parm2 ... parmn) */
public class Sput extends Operator {

	private static final long serialVersionUID = 0;
	
	/** Print to string. */
	public Value evaluate(Resolver resolver, Walker args) {
		throwIfNullArguments(args);
		StringBuilder out = new StringBuilder();
		while (args.hasNext())
			out.append(args.next().evaluate(resolver).stringValue());
		return new Str(out.toString());
	}
	
	/** Obtain operator name. */
	public String getOperatorName() {
		return "sput";	
	}
}
