const PROBLEMS: [[&str; 2]; 4] = [["problems", "1143"], ["problems", "31"], ["problems", "LCR_014"], ["problems", "LCR_036"]];

#[cfg(test)]
mod test {
	use test_executor::run_test::run_test;
	use crate::PROBLEMS;

	use solution_1143 as solution0;
	use solution_31 as solution1;
	use solution_LCR_014 as solution2;
	use solution_LCR_036 as solution3;

	#[test]
	fn test_solutions() {
		for (i, problem) in PROBLEMS.iter().enumerate() {
			let (folder, id) = (problem[0], problem[1]);
			println!("Testing problem {}", id);
			run_test(id, folder, match i {
				0 => solution0::solve,
				1 => solution1::solve,
				2 => solution2::solve,
				3 => solution3::solve,
				_ => panic!("Unknown solution"),
			});
		}
	}
}
