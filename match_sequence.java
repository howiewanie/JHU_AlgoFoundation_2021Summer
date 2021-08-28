//********************************************************************
//  match_sequence.java       Author: Howe Wang
//	Date: August 17th 2021
//	This is part of the interweaving signals algorithm for PA.4 
//	for Foundations of Algorithms
//  This file defines the method that matches two arrays to generate
// 	the arrays that are left after they are matched
//********************************************************************

package interweaving_signals;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class match_sequence{
	
	//This segment was assisted by question I asked on stackoverflow
	//https://stackoverflow.com/questions/68797369/bug-in-methods-that-find-unmatched-integers-between-two-arrays
	public static results match_sequence(int[] original, int[] match) {
	    int[] matched = null;
	    int[] original_rest = original;
		for(int j = 0; j < Math.min(match.length, original_rest.length); j++) {
	    //set a initial starting point plus i if we are not starting from 0
	    if(original_rest[j] == match[j]) {
	    match = subarray.subArray(match, j + 1, match.length - 1);
	    original_rest = subarray.subArray(original_rest, j + 1, original_rest.length - 1);}
	    else if(original_rest[j] != match[j]) {
	    original_rest = subarray.subArray(original_rest, j, original_rest.length - 1);
	    match = subarray.subArray(match, j, match.length - 1);
	    break;}
	    matched = Arrays.copyOfRange(original, 0, j);
	    j--;}
	    return new results(match, original_rest, matched);}	
	
	public static void main(String[] args){
	  int[] original = {1,0,1,0,0};
	  int[] match = {1,0,1,0,0};
	  //bug1: there is mismatch over here and should be resolved through debugging
	  int[] rest_of_match = match_sequence(original,match).getArray1();
	  System.out.println("Final match"+Arrays.toString(rest_of_match));
	  int[] original_rest = match_sequence(original,match).getArray2();
	  System.out.println("Final original"+Arrays.toString(original_rest));
	  int[] matched = match_sequence(original,match).getArray3();
	  System.out.println("Final matched"+Arrays.toString(matched));}}