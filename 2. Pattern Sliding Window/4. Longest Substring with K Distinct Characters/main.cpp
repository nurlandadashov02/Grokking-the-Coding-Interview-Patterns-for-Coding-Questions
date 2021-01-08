#include <bits/stdc++.h>

using namespace std;

int main() {
    int k;
    cin >> k;

    string str;
    cin >> str;

    int windowStart = 0, maxLength = 0;
    map<char, int> charFrequencyMap;

    for(int windowEnd = 0; windowEnd < str.length(); windowEnd++) {
        char rightChar = str.at(windowEnd);
        charFrequencyMap.insert(make_pair(rightChar, charFrequencyMap[rightChar] + 1));

        while(charFrequencyMap.size() > k) {
            char leftChar = str.at(windowStart);
            charFrequencyMap.insert(make_pair(leftChar, charFrequencyMap[leftChar] - 1));
            if(charFrequencyMap[leftChar] == 0) {
                charFrequencyMap.erase(leftChar);
            }
            windowStart++;
        }
        maxLength = max(maxLength, windowEnd - windowStart + 1);
    }

    cout << maxLength;

    return 0;
}
