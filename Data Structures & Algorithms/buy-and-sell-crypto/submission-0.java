class Solution {
    public int maxProfit(int[] prices) {
        int minBuy = prices[0];
        int maxPrice = 0;

        for (int sell: prices) {
            maxPrice = Math.max(maxPrice, sell - minBuy);
            minBuy = Math.min(minBuy, sell);
        }
        
        return maxPrice;
    }
}
