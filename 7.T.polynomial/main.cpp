#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    map<int, int> arr;

    for (int i = 0; i < n; ++i) {
        int t;
        cin >> t;
        for (int j = 0; j < t; ++j) {
            int x, e;
            cin >> x >> e;
            if (arr.find(e) != arr.end()) {
                arr[e] += x;
            } else {
                arr[e] = x;
            }
        }
    }

    vector<pair<int, int>> result;

    for (const auto& entry : arr) {
        if (entry.second != 0) {
            result.push_back(entry);
        }
    }

    sort(result.begin(), result.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.first > b.first;
    });

    if (!result.empty()) {
        cout << result.size() << "\n";
        for (const auto& entry : result) {
            cout << entry.second << " " << entry.first << "\n";
        }
    } else {
        cout << "0 0\n";
    }

    return 0;
}
