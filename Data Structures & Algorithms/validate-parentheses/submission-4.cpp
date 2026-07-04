class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> truth;
        truth[')'] = '(';
        truth['}'] = '{';
        truth[']'] = '[';

        stack<char> para;

        bool is_complete = true;
        for (int i = 0; i < s.size(); i++){
            bool is_open_para= false;
            for (const auto& pair : truth){
                if (pair.second == s[i]){
                    para.push(s[i]);
                    is_open_para= true;
                    break;
                }
            }
            if (is_open_para){
                continue;
            }

            if ((!para.empty()) && (truth.find(s[i]) != truth.end()) && truth[s[i]] == para.top()){
                para.pop();
            }
            else{
                is_complete = false;
                break;
            }

        }
        if (!para.empty()){
            is_complete = false;
        }
        return is_complete;
        
    }
};
