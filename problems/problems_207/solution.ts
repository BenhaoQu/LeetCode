function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const numCourses: number = JSON.parse(inputValues[0]);
	const prerequisites: number[][] = JSON.parse(inputValues[1]);
	return canFinish(numCourses, prerequisites);
}
