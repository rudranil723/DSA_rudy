// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution {
    public int findMin(int[] nums) {
        if (nums == null || nums.length == 0){return -1;}
        int min =nums[0];
        int minIndex =0;
        for (int i=1;i <nums.length;i++){
            if (nums[i]<min){
                min=nums[i];
                minIndex=i;
            }
        }
        return nums[minIndex];
    }
}