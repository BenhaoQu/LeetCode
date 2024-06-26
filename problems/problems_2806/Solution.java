package problems.problems_2806;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        return 100 - (purchaseAmount + 5) / 10 * 10;
    }

    @Override
    public Object solve(String[] values) {
        int purchaseAmount = Integer.parseInt(values[0]);
        return JSON.toJSON(accountBalanceAfterPurchase(purchaseAmount));
    }
}
