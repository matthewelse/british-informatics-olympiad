#include <iostream>
#include <limits>
#include <vector>

using namespace std;

int max_satisfaction(const vector<int> &telescopes, int position,
                     int step_count) {
  if (step_count == 0) {
    return 0;
  } else if (step_count == 1) {
    return telescopes[position];
  }

  int satisfaction = telescopes[position];
  int best = numeric_limits<int>::min();

  for (int direction : {-1, 1}) {
    int next_position = direction + position;
    if (next_position >= 0 && next_position < telescopes.size()) {
      int score = max_satisfaction(telescopes, next_position, step_count - 1);

      best = score > best ? score : best;
    }
  }

  return satisfaction + best;
}

int main() {
  int telescope_count, walker_count, satisfaction, uses;
  cin >> telescope_count >> walker_count;

  vector<int> telescopes;
  vector<int> walkers;

  for (int i = 0; i < telescope_count; i++) {
    cin >> satisfaction;
    telescopes.push_back(satisfaction);
  }
  for (int i = 0; i < walker_count; i++) {
    cin >> uses;
    walkers.push_back(uses);
  }

  int total = 0;

  for (auto telescope_count : walkers) {
    total += max_satisfaction(telescopes, 0, telescope_count);
  }

  cout << total << endl;
}