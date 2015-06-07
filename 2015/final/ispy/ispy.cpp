// file access stuff
#include <cstdlib>
#include <fstream>

// debugging
#include <iostream>

// data types
#include <set>
#include <utility>
#include <map>

using namespace std;

ifstream infile("input.txt");
ofstream outfile("output.txt");

#define DEBUG

#ifdef DEBUG
void print_map(map<int, set<int> > m) {
	for (map<int, set<int> >::iterator it = m.begin(); it != m.end(); it++) {
		cout << it->first << ": ";
		
		for (set<int>::iterator it2 = it->second.begin(); it2 != it->second.end(); it2++) {
			cout << *it2 << " ";
		}
		
		cout << endl;
	}
}

void print_pair(pair<int, int> p) {
	cout << p.first << ", " << p.second << endl;
}
#else
void print_map(map<int, set<int> > m) {}
void print_pair(pair<int, int> p) {}
#endif

pair<int, int> investigate_spies(int start, map<int, set<int> > connections, set<int> *investigated, bool group_a = true) {
	int a = group_a ? 1 : 0; // the first one is arbitrarily assigned to set a.
	int b = group_a ? 0 : 1;
	
	// make sure it hasn't already been investigated, to avoid infinite recursion
	if (investigated->count(start) != 0)
		return pair<int, int>(0, 0);
	
	#ifdef DEBUG
	cout << "-> Investigating " << start << endl;
	#endif

	
	investigated->insert(start);
	
	for (set<int>::iterator it = connections[start].begin(); it != connections[start].end(); it++) {
		pair<int, int> results = investigate_spies(*it, connections, investigated, !group_a);
		
		a += results.first;
		b += results.second;
	}
	
	return pair<int, int>(a, b);
}

int main(int argc, char** argv) {
	// store all of the connections
	map<int, set<int> > connections;
	
	// get the number of spies
	int n;
	infile >> n;
	
	int a;
	int b;
	
	infile >> a;
	infile >> b;
	
	while (a != -1 && b != -1) {
		// make sure they both exist in the connections map		
		if (connections.count(a) == 0) {
			set<int> conns;
			connections[a] = conns;
		}
		
		if (connections.count(b) == 0) {
			set<int> conns;
			connections[b] = conns;
		}
		
		connections[a].insert(b);
		connections[b].insert(a);
		
		infile >> a;
		infile >> b;
	}
	
	print_map(connections);
	
	// now work out the max
	
	int all_others = n - connections.size();
	
	#ifdef DEBUG
	cout << all_others << " not included in input" << endl;;
	#endif

	int big_count = 0;
	
	// keep track of all of the spies we've looked at.
	set<int> investigated;
	
	for (map<int, set<int> >::iterator it = connections.begin(); it != connections.end(); it++) {
		// go through each of the spies the input talks about...
		if (investigated.count(it->first))
			continue;
		
		#ifdef DEBUG
		cout << "Investigating " << it->first << endl;
		#endif
		
		pair<int, int> result = investigate_spies(it->first, connections, &investigated);
		print_pair(result);
		big_count += max(result.first, result.second);
	}
	
	#ifdef DEBUG
	cout << "count: " << big_count;
	#endif
	
	// answer = max(a, b) + all_others
	outfile << (big_count + all_others);
	
	return 0;
}
