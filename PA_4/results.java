//********************************************************************
//  results.java       Author: Howe Wang
//	Date: August 17th 2021
//	This is part of the interweaving signals algorithm for PA.4 
//	for Foundations of Algorithms
//  This file defines results class that allows for extracting of 
//	three different arrays
//********************************************************************

package interweaving_signals;
import java.util.Arrays;

public class results {     
      private int[] array1; //array2
      private int[] array2; //array1
      private int[] array3; //array1

      public results (int[] result1, int[] result2, int[] result3)
      {
         array1 = result1;
         array2 = result2;
         array3 = result3;
      }
      public int[] getArray1() { return array1; }
      public int[] getArray2() { return array2; }
      public int[] getArray3() { return array3; }}