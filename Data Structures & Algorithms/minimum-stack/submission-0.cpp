class MinStack {
    std::vector<int> stack;
    std::vector<int> min_stack;
public:
    MinStack() {
    }
    
    void push(int val) {
        this->stack.push_back(val);

        int new_min = this->min_stack.size() != 0 && this->min_stack.back() < val
            ? this->min_stack.back()
            : val;

        this->min_stack.push_back(new_min);
    }
    
    void pop() {
        this->stack.pop_back();
        this->min_stack.pop_back();
    }
    
    int top() {
        return this->stack.back();
    }
    
    int getMin() {
        return this->min_stack.back();
    }
};
