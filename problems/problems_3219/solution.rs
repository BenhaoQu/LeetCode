use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn minimum_cost(m: i32, n: i32, horizontal_cut: Vec<i32>, vertical_cut: Vec<i32>) -> i64 {
        
    }
}

#[cfg(feature = "solution_3219")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let m: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let n: i32 = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	let horizontal_cut: Vec<i32> = serde_json::from_str(&input_values[2]).expect("Failed to parse input");
	let vertical_cut: Vec<i32> = serde_json::from_str(&input_values[3]).expect("Failed to parse input");
	json!(Solution::minimum_cost(m, n, horizontal_cut, vertical_cut))
}