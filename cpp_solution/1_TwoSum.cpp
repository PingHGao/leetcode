class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        int subNum[n];
        vector<int> res(2);
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < i; j++){
                if(subNum[j] == nums[i]){
                    res[0] = j;
                    res[1] = i;
                    return res;
                }
            }
            subNum[i] = target - nums[i];
        }
        
        return res;
    }
};
