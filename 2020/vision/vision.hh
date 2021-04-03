/**
 * This problem seemed surprisingly easy, so maybe I missed a more efficient way
 * to answer this problem than DFS? I threw in some memoisation in case that
 * speeds things up, but there's no mark scheme so shrug.
 */

#include <iostream>
#include <limits>
#include <unordered_map>
#include <vector>

using namespace std;

int max_satisfaction(unordered_map<int, unordered_map<int, int>> memos,
                     const vector<int> &telescopes, int position,
                     int step_count) {
  if (step_count == 0) {
    return 0;
  } else if (step_count == 1) {
    return telescopes[position];
  } else if (memos[position].find(step_count) != memos[position].end()) {
    return memos[position][step_count];
  }

  int satisfaction = telescopes[position];
  int best = numeric_limits<int>::min();

  for (int direction : {-1, 1}) {
    int next_position = direction + position;
    if (next_position >= 0 && next_position < telescopes.size()) {
      int score =
          max_satisfaction(memos, telescopes, next_position, step_count - 1);

      best = score > best ? score : best;
    }
  }

  memos[position][step_count] = satisfaction + best;

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
  unordered_map<int, unordered_map<int, int>> memos;

  for (auto telescope_count : walkers) {
    total += max_satisfaction(memos, telescopes, 0, telescope_count);
  }

  cout << total << endl;
}