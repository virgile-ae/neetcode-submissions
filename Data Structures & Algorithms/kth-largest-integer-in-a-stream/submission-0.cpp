class KthLargest {
    int k;
    vector<int> queue;
public:
    KthLargest(int k, vector<int>& nums) : k(k), queue(nums) {
        std::sort(queue.begin(), queue.end());
    }
    
    int add(int val) {
        auto it = std::lower_bound(queue.begin(), queue.end(), val);
        queue.insert(it, val);
        return queue[queue.size() - k];
    }
};
