package org.reldb.ldi.slip.operators;

import org.reldb.ldi.slip.values.*;

public abstract class Comparison extends Operator {

	private static final long serialVersionUID = 1L;

	/** Perform comparison. */
	abstract boolean comparison(Value left, Value right);
	
	/** Evaluate. */
	public Value evaluate(Resolver resolver, Walker args) {
		throwIfNullArguments(args);
		if (args.hasNext()) {
			Value accumulator = args.next().evaluate(resolver);
			while (args.hasNext()) {
				Value v = args.next().evaluate(resolver); 
				if (!comparison(accumulator, v)) {
					args.terminate();
					return new Bool(false);
				}
				accumulator = v;
			}
		}
		return new Bool(true);
	}
}
