class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map <int,int> mp;
        int result;
        int min = INT_MIN;

        for(int i=0;i<nums.size();i++)
        {
            mp[nums[i]]++;
        }

        for(auto it: mp)
        {
            if(it.second>min)
            {
                min=it.second;
            }
        
        }


        for(auto it: mp)
        {
            if(it.second==min)
            {
                result=it.first;
            }
        
        }

        return result;
    }
};