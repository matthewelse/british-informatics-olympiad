#include <iostream>
#include <queue>
#include <unordered_set>
#include <vector>

using namespace std;

unordered_set<int> primes(int prime_limit) {
  vector<int> possible_primes(prime_limit + 1);

  // pick a generous starting size
  unordered_set<int> definite_primes;

  for (int i = 0; i < prime_limit; i++) {
    possible_primes[i] = i;
  }

  possible_primes[1] = 0;

  for (int i = 2; i <= prime_limit; i++) {
    if (possible_primes[i] == 0) continue;

    definite_primes.insert(i);

    for (int j = i * 2; j <= prime_limit; j += i) {
      possible_primes[j] = 0;
    }
  }

  return definite_primes;
}

int compute_shortest_path(unordered_set<int> &definite_primes, int start,
                          int end) {
  // distance * number
  queue<pair<int, int>> q;

  q.push({1, start});
  definite_primes.erase(start);

  while (!q.empty()) {
    pair<int, int> next = q.front();
    q.pop();

    int distance = next.first;
    int node = next.second;

    if (node == end) {
      return distance;
    }

    for (int i = 0; i < 24; i++) {
      int diff = 1 << i;

      if (definite_primes.count(node + diff) == 1) {
        definite_primes.erase(node + diff);
        q.push({distance + 1, node + diff});
      }

      if (definite_primes.count(node - diff) == 1
          ) {
        definite_primes.erase(node - diff);
        q.push({distance + 1, node - diff});
      }
    }
  }

  cerr << "not found" << endl;
  return -1;
}

int main() {
  int max_prime, start, end;

  cin >> max_prime >> start >> end;

  unordered_set<int> definite_primes = primes(max_prime);
  int shortest_path = compute_shortest_path(definite_primes, start, end);

  cout << shortest_path << endl;

  return 0;
}