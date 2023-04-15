package org.reldb.ldi.sili.vm.instructions;

import org.reldb.ldi.sili.values.Value;
import org.reldb.ldi.sili.vm.Context;
import org.reldb.ldi.sili.vm.Instruction;

public class OpGt extends Instruction {
	private final static long serialVersionUID = 0;
	public final void execute(Context context) {
		Value v = context.pop();
		context.push(context.pop().gt(v));
	}
}
