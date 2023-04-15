package org.reldb.ldi.sili.vm.instructions;

import org.reldb.ldi.sili.vm.Context;
import org.reldb.ldi.sili.vm.Instruction;
import org.reldb.ldi.sili.values.Value;

public class OpSubtract extends Instruction {
	private final static long serialVersionUID = 0;
	public final void execute(Context context) {
		Value v = context.pop();
		context.push(context.pop().subtract(v));
	}
}
