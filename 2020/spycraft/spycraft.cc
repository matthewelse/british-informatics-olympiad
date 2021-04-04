#include <iostream>
#include <queue>
#include <tuple>
#include <unordered_set>
#include <vector>

using namespace std;

long distance_to(tuple<long, long> start, tuple<long, long> end) {
  long x0, y0, x1, y1;

  tie(x0, y0) = start;
  tie(x1, y1) = end;

  long dx = abs(x0 - x1);
  long dy = abs(y0 - y1);

  long diagonal_distance = min(dx, dy);

  return dx + dy - diagonal_distance;
}

long shortest_path(const vector<vector<tuple<long, long>>>& boxes, size_t start,
                   size_t end) {
  priority_queue<tuple<long, size_t, tuple<long, long>>,
                 std::vector<tuple<long, size_t, tuple<long, long>>>,
                 std::greater<tuple<long, size_t, tuple<long, long>>>>
      q;

  long distance;
  size_t box;
  tuple<long, long> corner;

  for (auto corner : boxes[start]) {
    q.push({0, start, corner});
  }

  while (!q.empty()) {
    tie(distance, box, corner) = q.top();
    q.pop();

    if (box == end) {
      return distance;
    }

    for (auto next_corner : boxes[box + 1]) {
      q.push(
          {distance + distance_to(corner, next_corner), box + 1, next_corner});
    }
  }

  return 0;
}

int main() {
  long num_contacts, x0, y0, x1, y1;
  vector<vector<tuple<long, long>>> boxes;

  cin >> num_contacts;

  for (long i = 0; i < num_contacts; i++) {
    cin >> x0 >> y0 >> x1 >> y1;

    boxes.push_back({{x0, y0}, {x1, y1}, {x1, y0}, {x0, y1}});
  }

  long length = shortest_path(boxes, 0, boxes.size() - 1);

  cout << length << endl;
}
