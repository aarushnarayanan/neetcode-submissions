class Solution {
    public int[] productExceptSelf(int[] nums) {
        int [] output = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            int left [] = Arrays.copyOfRange(nums, 0, i);
            int right [] = Arrays.copyOfRange(nums, i + 1, nums.length);
            int leftProduct = 1;
            int rightProduct = 1;
            for (int l = 0; l < left.length; l++){
                leftProduct = left[l] * leftProduct;
            }
            for (int r = 0; r < right.length; r++){
                rightProduct = right[r] * rightProduct;
            }
            output[i] = leftProduct * rightProduct;
        }
        return output;

    }
}  
