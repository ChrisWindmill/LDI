package org.reldb.ldi.sili.exceptions;

/**
 * This exception is thrown when fatal errors are encountered.
 */
public class ExceptionFatal extends Error {

	static final long serialVersionUID = 0;
	
	public ExceptionFatal(String message) {
		super(message);
	}

}
