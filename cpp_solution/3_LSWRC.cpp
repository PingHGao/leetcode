class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> m;
        int res = 0;
        int lastRepPose = -1;
        
        for(int i = 0; i < s.size(); i++) {
            if(m.find(s[i]) != m.end() && lastRepPose < m[s[i]]) {
                lastRepPose = m[s[i]];
            }
            if (i - lastRepPose > res) {
                res = i - lastRepPose;
            }
            m[s[i]] = i;
        }
        
        return res;
    }
};
