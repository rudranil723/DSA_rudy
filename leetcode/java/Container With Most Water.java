import java.util.Arrays;

class Solution {
    public int maxArea(int[] height) {
        if (height.length == 0 && height.length ==1){
            return 0;
        }
        int max=0;
        int left =0;
        int right = height.length-1;
        while (left < right){
            int h = Math.min(height[left],height[right]);
            int w =  right-left;
            max= Math.max(max, h*w);

            if (height[left]<height[right]){left++;}
            else{right--;}
        }
        return max;
    }
}


// need to study pointers 