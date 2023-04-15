package org.reldb.ldi.silc.compiler;

import org.reldb.ldi.sili.vm.instructions.OpParameterGet;
import org.reldb.ldi.sili.vm.instructions.OpParameterSet;

public class Parameter extends Slot {
	
	public Parameter(int depth, int offset) {
		super(depth, offset);
	}

	@Override
	public void compileGet(Generator generator) {
		// Compile retrieval of parameter value
		generator.compileInstruction(new OpParameterGet(getDepth(), getOffset()));
	}

	@Override
	public void compileSet(Generator generator) {
		// compile assignment
		generator.compileInstruction(new OpParameterSet(getDepth(), getOffset()));
	}
}

