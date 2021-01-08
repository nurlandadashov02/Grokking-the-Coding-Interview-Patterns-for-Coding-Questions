#include <bits/stdc++.h>

using namespace std;

int main() {

    string str;
    cin >> str;

    int windowStart = 0, maxLength = 0;
    map<char, int> charIndexMap;

    for(int windowEnd = 0; windowEnd < str.length(); windowEnd++) {
        char rightChar = str.at(windowEnd);

        if(charIndexMap.find(rightChar) != charIndexMap.end()) {
            windowStart = max(windowStart, charIndexMap.at(rightChar) + 1);
        }
        charIndexMap[rightChar] = windowEnd;
        maxLength = max(maxLength, windowEnd - windowStart + 1);
    }

    cout << maxLength;

    return 0;
}
