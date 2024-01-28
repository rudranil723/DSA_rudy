class Solution {
    public static int kthSmallest(int[] arr, int l, int r, int k) {
        if (l == r) {
            return arr[l];
        }
        int pivotIndex = partition(arr, l, r);
        if (pivotIndex == k - 1) {
            return arr[pivotIndex];
        } else if (pivotIndex > k - 1) {
            return kthSmallest(arr, l, pivotIndex - 1, k);
        } else {
            return kthSmallest(arr, pivotIndex + 1, r, k);
        }
    }

    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[left + (int) (Math.random() * (right - left + 1))];
        int i = left, j = right;
        while (i <= j) {
            while (arr[i] < pivot) {
                i++;
            }
            while (arr[j] > pivot) {
                j--;
            }
            if (i <= j) {
                swap(arr, i, j);
                i++;
                j--;
            }
        }
        swap(arr, left, j);
        return j;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}