use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn can_make_square(grid: Vec<Vec<char>>) -> bool {

    }
}

#[cfg(feature = "solution_3127")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let grid: Vec<Vec<char>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::can_make_square(grid))
}
