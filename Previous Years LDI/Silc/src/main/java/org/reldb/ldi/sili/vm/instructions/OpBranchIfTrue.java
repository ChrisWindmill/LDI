package org.reldb.ldi.sili.vm.instructions;

import org.reldb.ldi.sili.vm.Context;
import org.reldb.ldi.sili.vm.Instruction;

public class OpBranchIfTrue extends Instruction {
	private final static long serialVersionUID = 0;

	private int address;

	/* For serialization support */
	
	public OpBranchIfTrue() {
		this.address = -1;
	}
	
	public void setAddress(int address) {
		this.address = address;
	}
	
	public int getAddress() {
		return address;
	}
	
	/* End of serialization support */

	public OpBranchIfTrue(int address) {
		this.address = address;
	}
	
	public final void execute(Context context) {
		context.branchIfTrue(address);
	}
		
	public String toString() {
		return getName() + " " + address;
	}

}
