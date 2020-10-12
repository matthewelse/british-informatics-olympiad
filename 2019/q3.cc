/* BIO Q3
 *
 * I don't know whether this is the right solution, since it takes ~30x too long
 * on the slowest example, but with g++ -std=c++17 -O3 q3.cc, I can get 22/24
 * with this, when I could only get 18 with the corresponding Python implementation.
 * 
 * 3(b): BOI, OBI, OIB, IBO, IOB (2 marks) 
 * 3(c): We require that there can't be any triples (a, b, c) across the two parts
 * such that a < b < c. Since all elements of the left hand side are smaller than
 * all elements of the right hand side, we know at least one of the inequalities
 * must hold by definition. We therefore can't have any as and bs in either the left
 * or right chunks where a < b. They must therefore both be the letters in reverse
 * alphabetical order (~2/3 marks?)
 * 3 (d): l = 19. alphabetical order. what is 1st? what is 1 billionth?
 *
 */

#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

std::ostream& operator<< (std::ostream& out, const std::vector<char>& v) {
    if (!v.empty()) {
        for (char c : v) {
            out << (char)(c + 'A');
        }
    }
    return out;
}

bool is_valid_addition(std::vector<char> &prefix, char next, int available) {
    int smallest = -1;

    for (char c : prefix) {
        if (smallest == -1 || c < smallest) {
            smallest = c;
        } else if (c > smallest && c < next) {
            // this would produce a triple of (a, b, c) whee a < b < c
            return false;
        }
    }

    if (smallest != -1 && next > smallest) {
        // we can prune additional choices, by asserting that this must be
        // the largest number available, since this will create a triple
        // later down the line.

        int base = 0xFFFFFFFF;

        if ((available & (base << (next + 1))) != 0) {
            return false;
        }
    } 

    return true;
}

long int seen = 0;

int count(std::vector<char> &prefix, int available, int len) {
    if (available == 0) {
        // cout << prefix << endl;
        seen++;
        if (seen == 1 || seen == 1000000000) {
            cout << prefix << endl;
        } else if ((seen % 10000000) == 0) {
            cout << "seen " << seen << endl;
        }
        return 1;
    }

    int total_count = 0;
    for (char c = 0; c < len; c++) {
        if (((available & (1 << c)) != 0) && is_valid_addition(prefix, c, available)) {
            prefix.push_back(c);
            total_count += count(prefix, available & ~(1 << c), len);
            prefix.pop_back();
        }
    }

    return total_count;
}

int main() {
    int len;
    std::string prefix_s;

    cin >> len >> prefix_s;

    // convert the string to a std::vector<char>
    
    std::vector<char> prefix;
    int all = 0x0;

    for (int i = 0; i < len; i++) {
        all |= 1 << i;
    }

    int available = all;

    for (char c : prefix_s) {
        char i = c - 'A';
        prefix.push_back(i);

        available &= ~(1 << i);
    }

    int result = count(prefix, available, len);

    cout << result << endl;

    return 0;
}
