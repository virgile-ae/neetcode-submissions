class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix[0].size();
        int l = 0;
        int r = matrix.size() * m - 1;

        while (l < r) {
            int mid = (l + r) / 2;
            int x = mid / m;
            int y = mid % m;

            if (target == matrix[x][y]) {
                return true;
            } else if (target < matrix[x][y]) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        int mid = (l + r) / 2;
        int x = mid / m;
        int y = mid % m;

        return matrix[x][y] == target;
    }
};
