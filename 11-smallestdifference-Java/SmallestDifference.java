// Write the function smallestDifference(a) that takes a list of integers and returns 
// the smallest absolute difference between any two 
// integers in the list. If the list is empty, return -1. For example:
//       assert(smallestDifference([19,2,83,6,27]) == 4)
// The two closest numbers in that list are 2 and 6, and their difference is 4.
import java.util.*;

public class SmallestDifference {

    public int smallestDifference(int[] a) {
        int n = a.length;
        int sum = 10^2;
        for(int i = 0; i < n -1;i++){
            for(int j = 0; j < n;j++){
                if(sum < (a[i] - a[j])) {
                    sum = (a[i] - a[j]);
                }
            }
        }
        return sum;
    }
}
