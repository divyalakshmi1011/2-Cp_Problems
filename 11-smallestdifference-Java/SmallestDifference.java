// Write the function smallestDifference(a) that takes a list of integers and returns 
// the smallest absolute difference between any two 
// integers in the list. If the list is empty, return -1. For example:
//       assert(smallestDifference([19,2,83,6,27]) == 4)
// The two closest numbers in that list are 2 and 6, and their difference is 4.
import java.util.*;
import java.lang.*;
import java.lang.Math; 
public class SmallestDifference {

    public int smallestDifference(int[] a) {
        int n = a.length;
        Arrays.sort(a);
           // Initialize difference as infinite 
           int diff = Integer.MAX_VALUE; 
           // Find the min diff by comparing adjacent 
           // pairs in sorted array 
           for (int i=0; i<n-1; i++) 
              if (a[i+1] - a[i] < diff) 
                  diff = a[i+1] - a[i];
           // Return min diff 
           return diff;
    }
}
