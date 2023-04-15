package org.reldb.ldi.sili.vm.instructions;

import org.reldb.ldi.sili.vm.Context;
import org.reldb.ldi.sili.vm.Instruction;
import org.reldb.ldi.sili.vm.Operator;

public class OpCallInvoke extends Instruction {
	private final static long serialVersionUID = 0;

	private Operator operator;
	
	/* For serialization support */
	
	public OpCallInvoke() {
		operator = null;
	}
	
	public void setOperator(Operator operator) {
		this.operator = operator;
	}
	
	public Operator getOperator() {
		return this.operator;
	}
	
	/* End of serialization support */
	
	public OpCallInvoke(Operator operator) {
		this.operator = operator;
	}
	
	public final void execute(Context context) {
		context.call(operator);
	}	
}
