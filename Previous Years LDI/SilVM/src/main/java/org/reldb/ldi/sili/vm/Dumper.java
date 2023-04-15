package org.reldb.ldi.sili.vm;

import java.util.Vector;

import org.reldb.ldi.sili.vm.instructions.OpCallInvoke;

import java.util.Collections;
import java.util.HashSet;

public class Dumper {

	private HashSet<String> printed;
	
	public HashSet<Operator> dumpMachineCode(Instruction[] code) {
		var invoked = new HashSet<Operator>();
		var address = 0;
		for (var op : code) {
			if (op == null)
				System.out.print("<NULL>");
			else {
				System.out.println();
				System.out.print(address + ": " + op);
				if (op instanceof OpCallInvoke) {
					Operator invokedOperator = ((OpCallInvoke)op).getOperator();
					invoked.add(invokedOperator);
					String invokedSignature = invokedOperator.getSignature();
					System.out.print(" " + invokedSignature);
				}
			}
			address++;
			System.out.print(" ");
		}
		return invoked;
	}
	
	public void dump(Operator operator) {
		if (printed.contains(operator.toString()))
			return;
		var heading = "--------" + operator.toString() + "--------";
		System.out.print(heading);
		printed.add(operator.toString());
		var operators = new Vector<Operator>(dumpMachineCode(operator.obtainCode()));
		var footer = String.join("", Collections.nCopies(heading.length(), "-"));
		System.out.println("\n" + footer);
		for (var code: operators) {
			dump(code);
		}
	}
	
	/** Dump machine code. */
	public void dumpMachineCode(Operator operator) {
		 printed = new HashSet<String>();
		 dump(operator);
	}

}
