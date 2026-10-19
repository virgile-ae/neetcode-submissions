class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix[0].size();
        int l = 0;
        int r = matrix.size() * m - 1;

        auto next_idx = [&m, &l, &r]() {
            int mid = (l + r) / 2;
            int x = mid / m;
            int y = mid % m;
            return std::tuple{x, y, mid};
        };

        while (l < r) {
            auto [x, y, mid] = next_idx();

            if (target == matrix[x][y]) {
                return true;
            } else if (target < matrix[x][y]) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        
        auto [x, y, _] = next_idx();

        return matrix[x][y] == target;
    }
};
