/* BIO 2014: Q1, but faster. */
#include <iostream>
#include <list>

using namespace std;

int main () {
    list<int> numbers;
    int target, lower, higher;
    cin >> target;

    for (int i = 0; i < 10000; i++) {
        numbers.push_back(2 * i + 1);
    }

    for (auto it = numbers.begin(); it != numbers.end(); it++) {
        const int step = *it;

        if (step < target) {
            lower = step;
        } else if (step > target) {
            higher = step;
            break;
        }

        if (step == 1) {
            continue;
        }

        int i = 0;
        for (auto inner_it = numbers.begin(); inner_it != numbers.end(); inner_it++) {
            if ((i + 1) % step == 0) {
                inner_it = numbers.erase(inner_it);

                // erase returns an iterator to the element after the one we
                // delete, so increment i to compensate
                i++;
            }

            i++;
        }        
    }

    cout << lower << " " << higher << endl;
}