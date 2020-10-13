/* See q2.py for notes. This solution is fast enough to get full marks :) */

#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

vector<vector<int>> construct_map(int r, vector<int> plan) {
  vector<vector<int>> connections(r);
  unordered_set<int> chosen;
  unordered_set<int> all;

  for (int i = 0; i < r; i++) {
    all.insert(i);
  }

  while (plan.size() > 0) {
    int next = plan.back();
    int picked = -1;

    // cout << "next = " << next << endl;

    for (int i = 0; i < r; i++) {
      if (chosen.count(i) == 0 &&
          find(plan.begin(), plan.end(), i) == plan.end()) {
        picked = i;
        chosen.insert(i);
        break;
      }
    }

    if (picked == -1) {
      throw "trying to pick -1";
    }

    // cout << "connecting " << next << " and " << picked << endl;
    connections[next].push_back(picked);
    connections[picked].push_back(next);

    plan.pop_back();
  }

  std::vector<int> available;

  for (int i = 0; i < r; i++) {
    if (chosen.count(i) == 0) {
      available.push_back(i);
    }
  }

  int x = available.at(0);
  int y = available.at(1);

  // cout << "connecting " << x << " and " << y << endl;

  connections[x].push_back(y);
  connections[y].push_back(x);

  for (int i = 0; i < r; i++) {
    sort(connections[i].begin(), connections[i].end());
  }

  return connections;
}

int main() {
  string plan_s;
  vector<int> plan;
  int p, q;

  cin >> plan_s >> p >> q;

  for (int i = plan_s.length() - 1; i >= 0; i--) {
    // the plan is in reverse, so we can use the thing as a stack.
    plan.push_back(int(plan_s.at(i) - 'A'));
  }

  int r = plan.size() + 2;

  auto connections = construct_map(r, plan);

  for (int i = 0; i < r; i++) {
    for (int connection_i : connections[i]) {
      char connection = 'A' + char(connection_i);

      cout << connection;
    }

    cout << endl;
  }

  // now run the game
  int start_room = 0, move_count = 0;
  int current_room = start_room;

  std::vector<int> room_counts(r);
  std::vector<std::vector<int>> leave_counts(r);
  for (int i = 0; i < r; i++) {
    leave_counts[i].resize(r);
  }

  room_counts[start_room] = 1;

  while (move_count < q) {
    int visit_count = room_counts[current_room];
    int leave_through = -1;

    if (visit_count % 2 == 1) {
      // odd
      leave_through = connections[current_room][0];
    } else {
      auto &exits = connections[current_room];

      for (int i = 0; i < exits.size(); i++) {
        auto exit = exits[i];
        if (leave_counts[current_room][exit] % 2 == 1) {
          if (i == exits.size() - 1) {
            leave_through = exit;
          } else {
            leave_through = exits[i + 1];
          }
          break;
        }
      }
    }

    leave_counts[current_room][leave_through] += 1;
    room_counts[leave_through] += 1;
    current_room = leave_through;

    move_count++;

    if (move_count == p) cout << char('A' + current_room);
    if (move_count == q) cout << char('A' + current_room);
  }

  cout << endl;
  return 0;
}