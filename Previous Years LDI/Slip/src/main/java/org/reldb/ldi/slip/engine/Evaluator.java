package org.reldb.ldi.slip.engine;

import org.reldb.ldi.slip.operators.*;
import org.reldb.ldi.slip.values.Bunch;
import org.reldb.ldi.slip.values.Resolver;
import org.reldb.ldi.slip.values.RootResolver;
import org.reldb.ldi.slip.values.Value;

import java.io.IOException;
import java.io.PrintStream;
import java.io.Reader;
import java.io.StringReader;

public class Evaluator {

	private static Resolver resolver;
	
	static {
		resolver = new RootResolver();
		resolver.put(new Quote());
		resolver.put(new Or());
		resolver.put(new And());
		resolver.put(new Not());
		resolver.put(new LessThan());
		resolver.put(new LessThanOrEquals());
		resolver.put(new GreaterThan());
		resolver.put(new GreaterThanOrEquals());
		resolver.put(new Equals());
		resolver.put(new NotEquals());
		resolver.put(new Plus());
		resolver.put(new Subtract());
		resolver.put(new Mult());
		resolver.put(new Div());
		resolver.put(new If());
		resolver.put(new Put());
		resolver.put(new Sput());
		resolver.put(new Fun());
		resolver.put(new Prog());
		resolver.put(new Cond());
		resolver.put(new Let());
		resolver.put(new Set());				
	};
	
	public static Value eval(Bunch l) throws IOException {
		return l.evaluate(resolver);
	}
	
	public static Value eval(String s) throws IOException {
		return eval((new Parser(new Lexer(new StringReader(s)))).parse());
	}
	
	public static void eval(Reader input, PrintStream output) throws IOException {
		Parser p = new Parser(new Lexer(input));
		while (true)
			eval(p.parse());
	}
	
}
