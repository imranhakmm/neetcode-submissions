class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        std::unordered_map<char,char> closetopen= {
            {')','('},
            {'}','{'},
            {']','['}
        };
        for (char c:s){
            if (closetopen.count(c)){
                if (!stack.empty() && stack.top()==closetopen[c]){
                    stack.pop();
                }   else{
                    return false;
                }
            }   else {
                stack.push(c);
            }
        }
        return stack.empty();
    }   
};
