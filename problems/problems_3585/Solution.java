package problems.problems_3585;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findMedian(int n, int[][] edges, int[][] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[][] queries = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(findMedian(n, edges, queries));
    }
}
