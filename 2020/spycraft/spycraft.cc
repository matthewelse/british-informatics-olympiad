/**
 * Spycraft
 *
 * I could be completely wrong with this question, but I think it only ever
 * makes sense to pick corners... I'm probably wrong, but it works for the
 * example, and I can't think of how else to answer this question.
 */
#include <iostream>
#include <limits>
#include <vector>

using namespace std;

int distance_between(const pair<int, int> &a, const pair<int, int> &b) {
  int dx = abs(a.first - b.first);
  int dy = abs(a.second - b.second);

  return max(dx, dy);
}

int min_route(const vector<vector<pair<int, int>>> corners, int spy_index,
              int corner_index) {
  if (spy_index == corners.size() - 1) {
    return 0;
  }

  int min_distance = numeric_limits<int>::max();

  for (int next_corner = 0; next_corner < corners[spy_index + 1].size();
       next_corner++) {
    int distance = distance_between(corners[spy_index][corner_index],
                                    corners[spy_index + 1][next_corner]) +
                   min_route(corners, spy_index + 1, next_corner);

    if (distance < min_distance) {
      min_distance = distance;
    }
  }

  return min_distance;
}

int main() {
  int c, p, q, r, s;
  vector<vector<pair<int, int>>> corners;

  cin >> c;

  for (int i = 0; i < c; i++) {
    cin >> p >> q >> r >> s;

    corners.emplace_back(4);

    corners[i][0] = make_pair(p, q);
    corners[i][1] = make_pair(r, s);
    corners[i][2] = make_pair(p, s);
    corners[i][3] = make_pair(r, q);
  }

  int best = numeric_limits<int>::max();

  for (int i = 0; i < 4; i++) {
    best = min(min_route(corners, 0, i), best);
  }

  cout << best << endl;
}