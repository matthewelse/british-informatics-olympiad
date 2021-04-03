/* Entry point for running vision.hh as a standalone binary. */

#include "vision.hh"

#include <iostream>

int main() {
  int num_telescopes, num_walkers;
  long satisfaction, steps;
  vector<long> satisfactions, walkers;

  cin >> num_telescopes >> num_walkers;

  for (int i = 0; i < num_telescopes; i++) {
    cin >> satisfaction;
    satisfactions.push_back(satisfaction);
  }

  for (int i = 0; i < num_walkers; i++) {
    cin >> steps;
    walkers.push_back(steps);
  }

  cout << solve(satisfactions, walkers) << endl;
  return 0;
}
