class Solution {
    public int maxArea(int[] heights) {
        int start = 0;
        int end = heights.length - 1;
        int maxWater = 0;

        while (start < end) {

            if (heights[start] < heights[end] ) {
                maxWater = Math.max(maxWater, (end - start) * heights[start]);
                start++;
            }
            else if (heights[end] < heights[start]) {
                maxWater = Math.max(maxWater, (end - start) * heights[end]);
                end--;
            }
            else{
                maxWater = Math.max(maxWater, (end - start) * heights[end]);
                end--;
            }
        }
        return maxWater;
    }
}
