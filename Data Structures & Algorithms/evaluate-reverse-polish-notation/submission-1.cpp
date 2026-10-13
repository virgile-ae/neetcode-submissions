class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack;
        unordered_set<string> operators{
            "+", "-", "*", "/"
        };

        for (string& token : tokens) {
            if (operators.find(token) == operators.end()) {
                stack.push_back(stoi(token));
                continue;
            }

            int r = stack.back();
            stack.pop_back();
            int l = stack.back();
            stack.pop_back();

            int result;

            if (token == "+") {
                result = l + r;
            } else if (token == "-") {
                result = l - r;
            } else if (token == "*") {
                result = l * r;
            } else if (token == "/") {
                result = l / r;
            }
            stack.push_back(result);
        }

        return stack[0];
    }
};
