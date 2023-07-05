class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> ans;
        int candy1=INT_MIN;
        int candy2=INT_MIN;
        int life1=0;
        int life2=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(nums[i]==candy1){
                life1++;
            }
            else if(nums[i]==candy2){
                life2++;
            }
            else if(life1==0){
                candy1=nums[i];
                life1=1;
            }
            else if(life2==0){
                candy2=nums[i];
                life2=1;
            }
            else{
                life1--;
                life2--;
            }
        }
        int count1=0;
        int count2=0;
        for(int i=0;i<n;i++){
            if(nums[i]==candy1){
                count1++;
            }
            if(nums[i]==candy2){
                count2++;
            }
        }
        if(count1>n/3)ans.push_back(candy1);
        if(count2>n/3)ans.push_back(candy2);
        return ans;
    }
};