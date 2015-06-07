#include <cstdlib>
#include <fstream>

#include <set>
#include <map>
#include <vector>
#include <algorithm>

#include <iostream>

using namespace std;

ifstream infile("input.txt");
ofstream outfile("output.txt");

struct Process {
	int n;
	int time;
	set<int> workers;
};

bool cmp_time(const Process a, const Process b) {
	return a.time < b.time;
}

int main(int argc, char** argv) {
	int n;
	infile >> n;
	
	vector<Process> processes;
	map<int, set<int> > mutually_exclusive;
	
	int highest_time = 0;
	
	for (int i = 0; i < n; i++) {
		Process new_process;
		infile >> new_process.time;		
		new_process.n = i;
		processes.push_back(new_process);
		set<int> blank;
		mutually_exclusive[i] = blank;
	}
	
	for (int i = 0; i < n - 1; i++ ) {
		int p_a;
		int p_b;
		
		infile >> p_a >> p_b;
		
		processes[p_a - 1].workers.insert(i);
		processes[p_b - 1].workers.insert(i);
		
		mutually_exclusive[p_a - 1].insert(p_b - 1);
		mutually_exclusive[p_b - 1].insert(p_a - 1);
	}
	
	sort(processes.begin(), processes.end(), cmp_time);
	
	int current_time;
	
	
	outfile << current_time - 1;
	
	return 0;
}
