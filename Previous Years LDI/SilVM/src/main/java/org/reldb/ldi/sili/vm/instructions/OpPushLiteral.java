package org.reldb.ldi.sili.vm.instructions;

import org.reldb.ldi.sili.vm.Context;
import org.reldb.ldi.sili.vm.Instruction;
import org.reldb.ldi.sili.values.Value;

public class OpPushLiteral extends Instruction {
	private final static long serialVersionUID = 0;

	private Value v;
	
	/* For serialization */
	
	public OpPushLiteral() {
		v = null;
	}
	
	public void setValue(Value v) {
		this.v = v;
	}
	
	public Value getValue() {
		return this.v;
	}
	
	/* End of serialization definitions */
	
	public OpPushLiteral(Value v) {
		this.v = v;
	}
	
	public final void execute(Context context) {
		context.pushLiteral(v);
	}
	
	public String toString() {
		return getName() + " " + v;
	}
}
