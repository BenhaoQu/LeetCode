use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {

    }
}

#[cfg(feature = "solution_72")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let word1: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let word2: String = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::min_distance(word1, word2))
}
