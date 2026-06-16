class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int bot = 1;
        int top = 0;
        //finding actual max value which will be top
        for (int p: piles) {
            top = Math.max(top, p);
        }
        int result = top;

        while (bot <= top) {
            int k = bot + (top - bot) / 2;
            long totalHours = 0;
            for (int i = 0; i < piles.length; i++) {
                totalHours += (piles[i] + k - 1) / k;
            }
            if (totalHours <= h) {
                result = k;
                top = k - 1;
            }
            else {
                bot = k + 1;
            }
        }
        return result;
    }
}