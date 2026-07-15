class Solution {
public:
    int jump(vector<int>& nums) {
        int res = 0;
        int r = 0, l = 0;
        

        while (r < nums.size() - 1) {
            int maxJump = 0;
            for (int i = l; i <= r; i++) {
                maxJump = max(maxJump, i + nums[i]);
            }
            l = r + 1;
            r = maxJump;
            res += 1;
        }

        return res;
    }
};
