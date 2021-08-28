//********************************************************************
//  subarray.java       Author: Howe Wang
//	Date: August 17th 2021
//	This is part of the interweaving signals algorithm for PA.4 
//	for Foundations of Algorithms
//  This file defines results a subarray method that extracts a segment
//	of the original array
//********************************************************************

package interweaving_signals;

import java.util.Arrays;
 
public class subarray
{
    // Generic method to get subarray of a non-primitive array
    // between specified indices
    public static<T> int[] subArray(int[] arr, int beg, int end) {
        return Arrays.copyOfRange(arr, beg, end+1);
    }}
