class Solution {
public:
    int findMin(vector<int> &nums) {
        if (nums[0] < nums.back()) return nums[0];
        int l = 0;
        int r = nums.size() - 1;
        int mid = (l + r) / 2;

        while (l < r && mid != l) {
            if (nums[l] < nums[mid]) {
                l = mid;
            } else {
                r = mid;
            }
            mid = (l + r) / 2;
        }

        return nums[r];
    }
};
