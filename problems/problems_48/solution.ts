/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const matrix: number[][] = JSON.parse(inputValues[0]);
	rotate(matrix)
	return matrix;
}
