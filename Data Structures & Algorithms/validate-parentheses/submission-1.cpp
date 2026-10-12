class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        unordered_map<char, char> other{
            {')', '('},
            {']', '['},
            {'}', '{'},
        };

        for (char ch : s) {
            switch (ch) {
                case '(':
                case '[':
                case '{':
                    stack.push_back(ch);
                    break;
                case ')':
                case ']':
                case '}':
                    if (stack.size() == 0) {
                        return false;
                    }
                    char back = stack.back();
                    stack.pop_back();
                    if (back != other[ch]) {
                        return false;
                    }
                    break;
            }
        }

        return stack.size() == 0;
    }
};
