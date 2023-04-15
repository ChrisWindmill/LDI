package org.reldb.ldi.sili.vm.instructions;

import org.reldb.ldi.sili.vm.Context;
import org.reldb.ldi.sili.vm.Instruction;

public final class OpAdd extends Instruction {
	private static final long serialVersionUID = 0L;
	public final void execute(Context context) {
		context.push(context.pop().add(context.pop()));
	}
}
