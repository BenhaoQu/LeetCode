use serde_json::{json, Value};
use library::lib::node_neighbors::{Node, array_to_node_neighbors, node_neighbors_to_array};

pub struct Solution;

// Definition for a Node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct Node {
//   pub val: i32,
//   pub neighbors: Vec<Rc<RefCell<Node>>>,
// }
//
// impl Node {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     Node {
//       val,
//       neighbors: Vec::new(),
//     }
//   }
// }
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn clone_graph(node: Option<Rc<RefCell<Node>>>) -> Option<Rc<RefCell<Node>>> {

    }
}


/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution;
 * let data: Option<Rc<RefCell<Node>>> = obj.clone_graph(node);
 */

#[cfg(feature = "solution_133")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
    let input_vec0: Option<Vec<Vec<i32>>> = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
    let node: Option<Rc<RefCell<Node>>>= array_to_node_neighbors(input_vec0);
    json!(node_neighbors_to_array(&Solution::clone_graph(node)))
}
