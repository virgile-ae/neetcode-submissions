class Solution {
public:
    /* Hypothetical minimum: m = sum(piles) / h
     * sum(piles / k) = h
     * ceil(p1/k) + ceil(p2/k) + ... + ceil(pn/k) = h
     * m <= k < sum(piles)
     */
    bool isValid(vector<int>& piles, int h, int k) {
        int hoursElapsed = 0;

        for (int pile : piles) {
            hoursElapsed += (pile + k - 1) / k;  // Round up
        }

        return hoursElapsed <= h;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        long long upper = 0;

        for (int pile : piles) {
            upper +=  static_cast<long long>(pile);
        }

        int optimal = upper / h;

        std::cout << "optimal: " << optimal << " upper: " << upper << '\n';

        long long l = std::max(optimal, 1); // To avoid getting divide by zero error
        long long r = upper;

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
