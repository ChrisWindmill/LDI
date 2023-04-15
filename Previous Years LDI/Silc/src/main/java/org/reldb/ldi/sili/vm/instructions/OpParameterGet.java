package org.reldb.ldi.sili.vm.instructions;

import org.reldb.ldi.sili.vm.Context;
import org.reldb.ldi.sili.vm.Instruction;

public class OpParameterGet extends Instruction {
	private final static long serialVersionUID = 0;

	private int depth;
	private int offset;

	/* For serialization support */
	
	public OpParameterGet() {
		this.depth = -1;
		this.offset = -1;
	}
	
	public void setDepth(int depth) {
		this.depth = depth;
	}
	
	public int getDepth() {
		return this.depth;
	}
	
	public void setOffset(int offset) {
		this.offset = offset;
	}
	
	public int getOffset() {
		return this.offset;
	}
	
	/* End of serialization support. */
	
	public OpParameterGet(int depth, int offset) {
		this.depth = depth;
		this.offset = offset;
	}
	
	public final void execute(Context context) {
		context.parmGet(depth, offset);
	}
	
	public String toString() {
		return getName() + " " + depth + " " + offset;
	}
}
