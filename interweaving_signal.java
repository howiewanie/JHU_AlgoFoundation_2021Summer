//********************************************************************
//  interweaving_signal.java       Author: Howe Wang
//	Date: August 17th 2021
//	This is part of the interweaving signals algorithm for PA.4 
//	for Foundations of Algorithms
//  This file functions as the main driver for different method created
//	that analyze the interweave of different subarrays
//********************************************************************

package interweaving_signals;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class interweaving_signal{
	public static void main(String[] args) {
        
	    int[] rest_first_match = null;
	    int[] rest_second_match = null;
	    int[] rest_original = null;
	    results returned = null;
	    int[] starting_noise = null;
	    int[] ending_noise = null;
	    
	  	Scanner original2 = new Scanner(System.in);
    	Scanner matched1 = new Scanner(System.in); 
    	Scanner matched2 = new Scanner(System.in);  
    	
        System.out.println("*******************************************************************************************************");
        System.out.println("This algorithm tells you if an original string is an interweaving of two substrings."+ "\n"+"It will also tell you starting and ending noise. "
        		+ "\n"+"Please enter the long strings and two substrings of your choice");

        System.out.println("Enter the original long string to be matched: ");
        String original23 = original2.next();
        
        System.out.println("Enter the one string to be matched: ");
        String matched12 = matched1.next();
        
        System.out.println("Enter the another string to be matched: ");
        String matched22 = matched2.next();

	    //Problem: Can not figure out a situation when the first element is a noise but it is also matching one of the two substrings' first element
	    //also there should be better way to optimize what is the best first or second element
	    int[] original= Arrays.stream(original23.split("")).mapToInt(Integer::parseInt).toArray();
	    int x[]= Arrays.stream(matched12.split("")).mapToInt(Integer::parseInt).toArray();       
	    int y[]= Arrays.stream(matched22.split("")).mapToInt(Integer::parseInt).toArray();

	    //Select one of the two strings as a starting strings for matching based on the first element in the array
	    for (int i = 0; i < original.length; i++) {//O(n) here as time complexity, n is the original string's length
		if(original[i]==x[0]) {
			rest_first_match = x;
			rest_second_match = y;
			if(i > 0){
			starting_noise =  subarray.subArray(original, 0, i); //identifying the starting noise if we do not match the first element
			rest_original = subarray.subArray(original, i+1, original.length-1);}
			else {rest_original=original;}
			break;}
			
			else if(original[i]==y[0]&&original[i]!=x[0]) { //match the second string
			rest_first_match = y;
			rest_second_match = x;
			if(i > 0){
			starting_noise =  subarray.subArray(original, 0, i);
			rest_original = subarray.subArray(original, i+1, original.length-1);}
			else {rest_original=original;}
			break;}
	    }
	    //print out what are the matching outcomes
		System.out.println("Starting first match string after this round of matching is: "+Arrays.toString(rest_first_match));
		System.out.println("Starting second match string is after this round of matching: "+Arrays.toString(rest_second_match));

		System.out.println("The original array for testing is: "+Arrays.toString(original));
		System.out.println("----------------------");
		
		//below are the lay out of different algorithm scenarios based on matching outcome
		
		//not a match if the size of two substrings are larger than the original string
		if ((rest_second_match.length+rest_first_match.length > rest_original.length )) {
		System.out.println("String is not a valid match of two sub strings, two elements together are too long");
		}
		
		else 
		//create a loop if the match substrings are not consumed yet and if the the original still have residuals for matching
		{ if((rest_first_match.length >0)||(rest_second_match.length >0)) {
		while(((rest_first_match.length >0)&&(rest_first_match[0]==rest_original[0]))
		||((rest_second_match.length>0&&rest_second_match[0]==rest_original[0]))){ 

		//loop between rest first match and rest second match	
		returned = match_sequence.match_sequence(rest_original,rest_first_match);
		rest_first_match = returned.getArray1();
		rest_original = returned.getArray2();
	    System.out.println("Rest of the first match string after this round of matching: "+Arrays.toString(rest_first_match));
	    System.out.println("Rest of the original string after this round of matching: "+Arrays.toString(rest_original));
	    System.out.println("-----------");
	    
		returned = match_sequence.match_sequence(rest_original,rest_second_match);
		rest_second_match = returned.getArray1();
		rest_original = returned.getArray2();
		System.out.println("Rest of the second match string after this round of matching: "+Arrays.toString(rest_second_match));
		System.out.println("Rest of the original string after this round of matching: "+Arrays.toString(rest_original));	
		System.out.println("-----------");}
		
		//if in the end the string is not completely consumed and neither are both the substrings there is a mismatch
		if(((rest_first_match.length+rest_second_match.length)>0)&&(rest_original.length>0)) {
			if(((rest_first_match.length>0)&&(rest_original[0]!=rest_first_match[0]))&&((rest_second_match.length>0)&&(rest_original[0]!=rest_first_match[0]))){
		System.out.println("String is not a valid match of two sub strings");}}
		
		//if the substrings are not all zero but the original is finished, the string is not an interweave of two substrings
		if	(rest_original.length==0&&((rest_first_match.length+rest_second_match.length)>0)){
		System.out.println("---String is not an interweaving of two substrings. The two substrings contain unmatched elements---"); }
	
		//if we have a situation where the string contains multiple combinations of two substrings, then after finishing the first loop
		//we will continue looping through the rest of the substrings
		else if	(rest_original.length>0&&((rest_first_match.length+rest_second_match.length)==0)){
		System.out.println("---String is an interweaving of two substrings.Continue test the rest of the string for match---");
		
		
		for (int i = 0; i < rest_original.length; i++) {
		if(rest_original[i]==x[0]) {
			rest_first_match = x;
			rest_second_match = y;
			break;}
		else if(rest_original[i]==y[0]&&rest_original[i]!=x[0]) {
			rest_first_match = y;
			rest_second_match = x;
			break;}   }
		
		while (((rest_first_match.length >0)&&(rest_first_match[0]==rest_original[0]))
			||((rest_second_match.length>0&&rest_second_match[0]==rest_original[0]))){ 
			
			//and either one of the two elements' first element is a match
			returned = match_sequence.match_sequence(rest_original,rest_first_match);
			rest_first_match = returned.getArray1();
			rest_original = returned.getArray2();
		    System.out.println("Rest of the first match string after this round of matching: "+Arrays.toString(rest_first_match));
		    System.out.println("Rest of the original string after this round of matching: "+Arrays.toString(rest_original));
		    System.out.println("-----------");
		    
			returned = match_sequence.match_sequence(rest_original,rest_second_match);
			rest_second_match = returned.getArray1();
			rest_original = returned.getArray2();
			System.out.println("Rest of the second match string after this round of matching: "+Arrays.toString(rest_second_match));
			System.out.println("Rest of the original string after this round of matching: "+Arrays.toString(rest_original));	
			System.out.println("-----------");}
		if(rest_original.length>0 && (rest_first_match.length+rest_second_match.length >0)){
		    System.out.println("Original array exhausted.");}}}}
		
		//An outside main loop to match main original string and rest of substrings when we have a situation when length of either substrings
		//are not 0 and there is a match between them and the first element of the rest of original string
		while(((rest_first_match.length >0)&&(rest_first_match[0]==rest_original[0]))
			||((rest_second_match.length>0&&rest_second_match[0]==rest_original[0]))){ 
			//and either one of the two elements' first element is a match
			
			returned = match_sequence.match_sequence(rest_original,rest_first_match);
			rest_first_match = returned.getArray1();
			rest_original = returned.getArray2();
		    System.out.println("Rest of the first match string after this round of matching: "+Arrays.toString(rest_first_match));
		    System.out.println("Rest of the original string after this round of matching: "+Arrays.toString(rest_original));
		    System.out.println("-----------");
			    
			returned = match_sequence.match_sequence(rest_original,rest_second_match);
			rest_second_match = returned.getArray1();
			rest_original = returned.getArray2();
			System.out.println("Rest of the second match string after this round of matching: "+Arrays.toString(rest_second_match));
			System.out.println("Rest of the original string after this round of matching: "+Arrays.toString(rest_original));	
			System.out.println("-----------");}
		
		//print out if we have starting or ending noise in the results
			ending_noise = rest_original;
			if(starting_noise!= null&&starting_noise.length >0) {System.out.println("Starting noise of the string is : "+Arrays.toString(starting_noise));}
			if(ending_noise!= null&&ending_noise.length > 0) {System.out.println("Ending noise of the string is : "+Arrays.toString(ending_noise));}
				
			else if	(rest_original.length>0&&((rest_first_match.length+rest_second_match.length)>0)){
			System.out.println("---String is not an interweaving of two substrings.---"); }

			else if	(rest_original.length==0&&((rest_first_match.length+rest_second_match.length)==0)){
			System.out.println("---String is an interweaving of two substrings.---"); }}}