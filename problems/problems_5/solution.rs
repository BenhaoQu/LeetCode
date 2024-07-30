use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn longest_palindrome(s: String) -> String {

    }
}

#[cfg(feature = "solution_5")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let s: String = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	json!(Solution::longest_palindrome(s))
}
