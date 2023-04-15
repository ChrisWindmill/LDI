package org.reldb.ldi.sili.vm.instructions;

import org.reldb.ldi.sili.vm.Context;
import org.reldb.ldi.sili.vm.Instruction;
import org.reldb.ldi.sili.values.ValueBoolean;

public class OpFalse extends Instruction {
	private final static long serialVersionUID = 0;
	public final void execute(Context context) {
		context.push(ValueBoolean.getFalse());
	}
}
