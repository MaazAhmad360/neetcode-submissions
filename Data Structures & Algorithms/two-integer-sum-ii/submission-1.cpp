class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;

        while (true){
            int res = numbers[j] + numbers[i];
            if(res == target){
                break;
            }
            else if (res > target){
                j--;
            }
            else if (res < target){
                i++;
            }
        }
        vector<int> output;
        output.insert(output.end(), {i+1, j+1});

        return output;
    }
};
