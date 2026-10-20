class Solution {
public:
    bool isValid(vector<int>& piles, int h, int k) {
        int hoursElapsed = 0;

        for (int pile : piles) {
            hoursElapsed += (pile + k - 1) / k;  // Round up
        }

        return hoursElapsed <= h;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        uint64_t upper = 0;

        for (int pile : piles) {
            upper +=  static_cast<long long>(pile);
        }

        int optimal = upper / h;

        uint64_t l = std::max(optimal, 1);
        uint64_t r = upper;

        while (l < r) {
            long long k = (l + r) / 2;
            if (isValid(piles, h, k)) {
                r = k;
            } else {
                l = k + 1;
            }
        }

        return l;
    }
};
