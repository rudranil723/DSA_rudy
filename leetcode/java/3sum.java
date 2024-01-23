import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        //creating a neww arrray to store the values 
        List<List<Integer>> result = new ArrayList<>(); 

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue; // Skip duplicates
            }

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    // Skip duplicates
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }

                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }
}



// Sorting:

// Arrays.sort(nums);: The input array nums is sorted in ascending order. Sorting is a crucial step to efficiently find triplets with a sum of zero.
// Looping Through Elements:

// for (int i = 0; i < nums.length - 2; i++) {: The outer loop iterates through each element in the array. It goes up to the third-to-last element (nums.length - 2) to ensure there are enough elements for left and right pointers.
// Skip Duplicates:

// if (i > 0 && nums[i] == nums[i - 1]) { continue; }: Skip duplicates to avoid redundant triplets. This condition ensures that we skip duplicates and only consider the first occurrence of each unique value.
// Initialize Pointers:

// int left = i + 1; and int right = nums.length - 1;: Initialize two pointers, left and right, to find a pair with a sum of zero.
// Two-Pointers Approach:

// while (left < right) {: Enter a while loop that continues as long as the left pointer is less than the right pointer.
// Sum Calculation:

// if (nums[i] + nums[left] + nums[right] == 0) {: Check if the sum of the current triplet is zero.
// Triplet Found:

// result.add(Arrays.asList(nums[i], nums[left], nums[right]));: If a triplet is found, add it to the result list.
// Skip Duplicates (Inside While Loop):

// while (left < right && nums[left] == nums[left + 1]) { left++; }: Skip duplicates for the left pointer.
// while (left < right && nums[right] == nums[right - 1]) { right--; }: Skip duplicates for the right pointer.
// These two while loops ensure that you don't count duplicate triplets.
// Move Pointers:

// left++; and right--;: Move the pointers to explore new combinations.
// Adjust Pointers for Sum Conditions:

// else if (sum < 0) { left++; }: If the sum is less than zero, move the left pointer to increase the sum.
// else { right--; }: If the sum is greater than zero, move the right pointer to decrease the sum.
// Return Result:

// Finally, the function returns the list of unique triplets found.
// This algorithm uses a two-pointers approach and takes advantage of the sorted nature of the array to efficiently find unique triplets with a sum of zero.







