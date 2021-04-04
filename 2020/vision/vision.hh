// cppimport
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

long max_satisfaction(unordered_map<long, unordered_map<long, long>> memos,
                      const vector<long> &telescopes, size_t position,
                      long step_count) {
  if (step_count == 0) {
    return 0;
  } else if (step_count == 1) {
    return telescopes[position];
  } else if (memos[position].find(step_count) != memos[position].end()) {
    return memos[position][step_count];
  }

  long satisfaction = telescopes[position];
  long best = numeric_limits<long>::min();

  for (long direction : {-1, 1}) {
    size_t next_position = direction + position;
    if (next_position >= 0 && next_position < telescopes.size()) {
      long score =
          max_satisfaction(memos, telescopes, next_position, step_count - 1);

      best = score > best ? score : best;
    }
  }

  memos[position][step_count] = satisfaction + best;

  return satisfaction + best;
}

long solve(std::vector<long> satisfactions, std::vector<long> walkers) {
  long total = 0;
  unordered_map<long, unordered_map<long, long>> memos;

  for (auto telescope_count : walkers) {
    total += max_satisfaction(memos, satisfactions, 0, telescope_count);
  }

  return total;
}
