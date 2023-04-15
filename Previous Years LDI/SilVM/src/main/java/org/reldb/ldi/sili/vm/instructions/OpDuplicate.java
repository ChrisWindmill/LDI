package org.reldb.ldi.sili.vm.instructions;

import org.reldb.ldi.sili.vm.Context;
import org.reldb.ldi.sili.vm.Instruction;

public class OpDuplicate extends Instruction {
	private final static long serialVersionUID = 0;
	public final void execute(Context context) {
		context.duplicate();
	}
}
