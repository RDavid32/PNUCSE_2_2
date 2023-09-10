#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<string, int>> money_list;
    string result = "NONE";

    for (int q = 0; q < n; q++) {
        string a;
        int b;
        cin >> a >> b;
        money_list.push_back(make_pair(a, b));
    }

    sort(money_list.begin(), money_list.end(), [](const pair<string, int>& x, const pair<string, int>& y) {
        return x.second > y.second;
    });

    int max_money = money_list[0].second;
    result = money_list[0].first;
    int check = 0;

    for (int q = 1; q < n; q++) {
        if (money_list[q].second == max_money) {
            check = 1;
        } else if (money_list[q].second < max_money) {
            if (check == 0) {
                cout << result << endl;
                return 0;
            }
            max_money = money_list[q].second;
            check = 0;
        }
        result = money_list[q].first;
    }

    cout << "NONE" << endl;

    return 0;
}
