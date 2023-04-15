package org.reldb.ldi.slip.engine;

import org.junit.jupiter.api.Test;
import org.reldb.ldi.slip.values.Bunch;
import org.reldb.ldi.slip.values.Value;
import org.reldb.ldi.slip.values.Walker;

import java.io.IOException;
import java.io.StringReader;

import static org.assertj.core.api.Assertions.assertThat;

public class TestEngine {

    @Test
    public void testLexer() throws IOException {
        String s = "This is  a test   of  the tokenizer\nLine two\nLine three";
        Lexer p = new Lexer(new StringReader(s));
        assertThat(p.getToken()).isEqualTo("This");
        assertThat(p.getToken()).isEqualTo("is");
        assertThat(p.getToken()).isEqualTo("a");
        assertThat(p.getToken()).isEqualTo("test");
        assertThat(p.getToken()).isEqualTo("of");
        assertThat(p.getToken()).isEqualTo("the");
        assertThat(p.getToken()).isEqualTo("tokenizer");
        assertThat(p.getToken()).isEqualTo("Line");
        assertThat(p.getToken()).isEqualTo("two");
        assertThat(p.getToken()).isEqualTo("Line");
        assertThat(p.getToken()).isEqualTo("three");
        assertThat(p.getToken()).isNull();
    }

    @Test
    public void testListIterator() throws IOException {
        String s = "(blah 5 10 -1)";
        Parser p = new Parser(new Lexer(new StringReader(s)));
        Walker l = ((Bunch) p.parse().getHead().getItem()).getWalker();
        assertThat(l.hasNext()).isTrue();
        assertThat(l.next().toString()).isEqualTo("blah");
        assertThat(l.hasNext()).isTrue();
        assertThat(l.next().toString()).isEqualTo("5");
        assertThat(l.hasNext()).isTrue();
        assertThat(l.next().toString()).isEqualTo("10");
        assertThat(l.hasNext()).isTrue();
        assertThat(l.next().toString()).isEqualTo("-1");
        assertThat(l.hasNext()).isFalse();
    }

    @Test
    public void testCode() throws IOException {
        String s = "(prog (put 'prog1\\n') (put 'prog2\\n') (put 'prog3\\n'))";
        Evaluator.eval(s);
    }

    @Test
    public void testParser0() throws IOException {
        String s = "(+ 3 4)";
        Parser p = new Parser(new Lexer(new StringReader(s)));
        assertThat(p.parse().toString()).isEqualTo("(" + s + ")");
    }

    @Test
    public void testParser1() throws IOException {
        String s = "(+ 3 4 (5 (7 8) 6)) // End of line comment";
        Parser p = new Parser(new Lexer(new StringReader(s)));
        assertThat(p.parse().toString()).isEqualTo("((+ 3 4 (5 (7 8) 6)))");
    }

    @Test
    public void testParser2() throws IOException {
        String s = "(+ 3 4 /* inline comment */ \"this " + "\\" + "\"" + " is \\065\\064 string\" (5 6))";
        Parser p = new Parser(new Lexer(new StringReader(s)));
        assertThat(p.parse().toString()).isEqualTo("((+ 3 4 this \" is A@ string (5 6)))");
    }

    @Test
    public void testEngine0() throws IOException {
        String s = "((+ 3.0 4.0 (+ 5.2 6.0)))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("18.2");
    }

    @Test
    public void testEngine1() throws IOException {
        String s = "(if (< 1 2 3 5) 1 2)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("1");
    }

    @Test
    public void testEngine2() throws IOException {
        String s = "(if (< 2 1 10) 1 2)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("2");
    }

    @Test
    public void testEngine3() throws IOException {
        String s = "(put 1 2 3 \"fish\" (quote 5 6 (7 8)) \"\\n\" \"Next Line?\")";
        Evaluator.eval(s);
    }

    @Test
    public void testEngine4() throws IOException {
        String s = "(- 4.0 3.0 (- 6.0 2.0))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("-3.0");
    }

    @Test
    public void testEngine5() throws IOException {
        String s = "(sput 1 2 3 \"fish\" (quote 5 6 (7 8)) \"\\n\" \"Next Line?\")";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("123fish(5 6 (7 8))\nNext Line?");
    }

    @Test
    public void testEngine6() throws IOException {
        String s = "(* 4.0 3.0 (* 6.0 2.0))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("144.0");
    }

    @Test
    public void testEngine7() throws IOException {
        String s = "(/ 12.0 2.0 (/ 6.0 2.0))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("2.0");
    }

    @Test
    public void testEngine8() throws IOException {
        String s = "(> 10 5 -1)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("true");
    }

    @Test
    public void testEngine9() throws IOException {
        String s = "(> 5 10 -1)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("false");
    }

    @Test
    public void testEngine10() throws IOException {
        String s = "(>= 10 10 5 -1)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("true");
    }

    @Test
    public void testEngine11() throws IOException {
        String s = "(>= 9 10 -1)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("false");
    }

    @Test
    public void testEngine12() throws IOException {
        String s = "(<= -1 5 10 10)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("true");
    }

    @Test
    public void testEngine13() throws IOException {
        String s = "(<= 9 10 -1)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("false");
    }

    @Test
    public void testEngine14() throws IOException {
        String s = "(= 10 10 10)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("true");
    }

    @Test
    public void testEngine15() throws IOException {
        String s = "(= 9 10 -1)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("false");
    }

    @Test
    public void testEngine16() throws IOException {
        String s = "(!= 10 10 10)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("false");
    }

    @Test
    public void testEngine17() throws IOException {
        String s = "(!= 9 10 -1)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("true");
    }

    @Test
    public void testEngine18() throws IOException {
        String s = "(or false false true)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("true");
    }

    @Test
    public void testEngine19() throws IOException {
        String s = "(or false false false)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("false");
    }

    @Test
    public void testEngine20() throws IOException {
        String s = "(and true true true)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("true");
    }

    @Test
    public void testEngine21() throws IOException {
        String s = "(and true true false)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("false");
    }

    @Test
    public void testEngine22() throws IOException {
        String s = "(quote blah blat zorg)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("(blah blat zorg)");
    }

    @Test
    public void testEngine23() throws IOException {
        String s = "(not true)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("false");
    }

    @Test
    public void testEngine24() throws IOException {
        String s = "(not false)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("true");
    }

    @Test
    public void testEngine25() throws IOException {
        String s = "(not false true false)";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("(true false true)");
    }

    @Test
    public void testEngine26() throws IOException {
        String s = "((sput 'blah'))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("blah");
    }

    @Test
    public void testEngine27() throws IOException {
        String s = "((fun (p1 p2 p3) " +
                "(sput (+ p2 p1 p3))) 'blah' 'blat' 'zot')";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("blatblahzot");
    }

    @Test
    public void testEngine28() throws IOException {
        String s = "(cond " +
                "((> 3 4) 'First') " +
                "((< 3 4) 'Second'))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("Second");
    }

    @Test
    public void testEngine29() throws IOException {
        String s = "(cond " +
                "((> 5 4) 'First') " +
                "((< 3 4) 'Second'))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("First");
    }

    @Test
    public void testEngine30() throws IOException {
        String s = "(let (" +
                "(a 1) " +
                "(b 2) " +
                "(c)) " +
                "(sput (+ '' a b c)))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("12nil");
    }

    @Test
    public void testEngine31() throws IOException {
        String s = "(prog " +
                "(set x (+ 2 3)) " +
                "(put x) " +
                "(x))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("5");
    }

    @Test
    public void testEngine32() throws IOException {
        String s = "(prog " +
                "(set (+ 'x' 'y') (+ 2 3) " +
                "     z 3) " +
                "(sput xy z))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("53");
    }

    @Test
    public void testEngine33() throws IOException {
        String s = "(let (" +
                "(a 1) " +
                "(b 2) " +
                "(c)) " +
                "(set b 3) " +
                "(sput (+ '' a b c)))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("13nil");
    }

    @Test
    public void testEngine34() throws IOException {
        String s = "(prog " +
                "(set a (fun (n) (+ 1 n))) " +
                "(a 3))";
        Value v = Evaluator.eval(s);
        assertThat(v.toString()).isEqualTo("4");
    }
}
