//Created on July 6th 19:10:25 2021
//@author: Howe Wang
//This following code is created for Programming Assignment Two - Recursive Functions
//This file contains the main file for the program

package recursiontree;
import java.util.Scanner;
import java.util.Arrays;
import java.util.List;

public class recursion_tree_main{	
	
	//require users to enter different components of a parameter one by one
	public static void main(String[] args) {
		System.out.println("Enter your function's different components one by one.\nThe format of your equation is: (a/b)*T(n+operator+(c/d)+(e/f)(n)^(g/h)\nIn total you will need to type in 9 parameters");
		System.out.println("First you should type in an operator, it should be either / or -, / indicates it is a divide and conquer function, - indicates it is a divide and chip function");
		Scanner operator = new Scanner(System.in);
		String operator2 = operator.nextLine();
		System.out.println("Next the parameters, please follow the format above and type in a b c d e f g h sequentially");
		
		Scanner a = new Scanner(System.in);
		Scanner b = new Scanner(System.in);
		Scanner c = new Scanner(System.in);
		Scanner d = new Scanner(System.in);
		Scanner e = new Scanner(System.in);
		Scanner f = new Scanner(System.in);
		Scanner g = new Scanner(System.in);
		Scanner h = new Scanner(System.in);
		
		int a2 = a.nextInt();
		int b2 = b.nextInt();
		int c2 = c.nextInt();
		int d2 = d.nextInt();
		int e2 = e.nextInt();
		int f2 = f.nextInt();
		int g2 = g.nextInt();
		int h2 = h.nextInt();
		
		Rational A = new Rational (a2, b2);
		Rational B = new Rational (c2, d2);
		Rational C = new Rational (e2, f2);
		Rational D = new Rational (g2, h2);
		
		//based on user input and selection, generate intended function and process the recursion, with auxiliary variable k, accordingly
		if(operator2.equals("/")){
			System.out.println("The original function is:\n"+"("+A+")T(n*"+"("+B+"))+"+"("+C+")(n)^("+D+")");		
			System.out.println("Your recursive function is: Divide and Conquer");
			Parameter_DQ.conquerExpand(3,parameterExtract(A,B,C,D));}

		else if(operator2.equals("-")){
			System.out.println("The original function is:\n"+"("+A+")T(n"+operator2+"("+B+"))+"+"("+C+")"+"(n)^("+D+")");		
			System.out.println("Your recursive function is: Divide and Chip");
			Parameter_DC.chipExpand(3,parameterExtract(A,B,C,D));}
		
		else System.out.println("Invalid Format");
		
		operator.close();
		a.close();
		b.close();
		c.close();
		d.close();
		e.close();
		f.close();
		g.close();
		h.close();
}
		
		//create a list of rationals for future extraction
		private static List<Rational> parameterExtract(Rational A,Rational B,Rational C,Rational D) {
			List<Rational> numbers = Arrays.asList( A, B, C, D);		
			return numbers;
}}