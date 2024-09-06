const PROBLEMS: [[&str; 2]; 4] = [["problems", "LCR_049"], ["problems", "LCR_093"], ["problems", "51"], ["problems", "32"]];

#[cfg(test)]
mod test {
	use test_executor::run_test::run_test;
	use crate::PROBLEMS;

	use solution_LCR_049 as solution0;
	use solution_LCR_093 as solution1;
	use solution_51 as solution2;
	use solution_32 as solution3;

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
