#include <iostream>
#include <stack>
using namespace std;

int N,K;

void find_combination (stack<int> current_combination, int current_total_prices, int start_index, int prices[]) {

    if (current_total_prices == K) {
        while (!current_combination.empty()) {
            cout << current_combination.top() << endl;
            current_combination.pop();
        }
        exit(0);
    }
    else if (current_total_prices > K)
        return;
    for (int i = start_index; i < N; i++){
        current_combination.push(prices[i]);

        find_combination(current_combination, current_total_prices +prices[i], i + 1,prices);
        current_combination.pop();
    }
}


int main() {
    int temp;
    cin >> N >> K;
    int prices [N];
    for (int i = 0; i  <= N - 1 ; i ++){
        cin >> prices[i];

    }
    stack <int> current_combination;
    for (int i = 0; i < N - 1; i++)
    {
        for (int j = 0; j < N - 1 - i; j++)
        {
            if (prices[j] < prices[j + 1])
            {
                temp        = prices[j];
                prices[j]     = prices[j + 1];
                prices[j + 1] = temp;
            }
        }
    }

    find_combination(current_combination, 0, 0, prices);
    cout << "0";
}

