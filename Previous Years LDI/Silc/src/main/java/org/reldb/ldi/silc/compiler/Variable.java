package org.reldb.ldi.silc.compiler;

import org.reldb.ldi.sili.vm.instructions.OpVariableGet;
import org.reldb.ldi.sili.vm.instructions.OpVariableSet;

public class Variable extends Slot {
	
	public Variable(int depth, int offset) {
		super(depth, offset);
	}
	
	@Override
	public void compileGet(Generator generator) {
		// Compile retrieval of variable value
		generator.compileInstruction(new OpVariableGet(getDepth(), getOffset()));
	}

	@Override
	public void compileSet(Generator generator) {
		// compile assignment
		generator.compileInstruction(new OpVariableSet(getDepth(), getOffset()));
	}
}
