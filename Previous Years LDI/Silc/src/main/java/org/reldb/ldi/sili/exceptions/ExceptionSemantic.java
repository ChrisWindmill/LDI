package org.reldb.ldi.sili.exceptions;
/**
 * This exception is thrown when semantic errors are encountered.
 */
public class ExceptionSemantic extends Error {

	static final long serialVersionUID = 0;
	
	public ExceptionSemantic(String message) {
		super(message);
	}

}
