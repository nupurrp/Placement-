class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        long long sum = 0;

        //For storing unique vectors
        set<vector<int>> set;
        vector<vector<int>> out;

        for(int i = 0; i < n-3; i++){
            for(int j = i+1; j < n-2; j++){
                int k = j+1;
                int m = n-1;
                
                while(k<m){
                    sum =   (long long)nums[i] + 
                            (long long)nums[j] + 
                            (long long)nums[k] + 
                            (long long)nums[m];
                    if(sum == target){
                        set.insert({nums[i], nums[j], nums[k], nums[m]});
                        k++;
                        m--;
                    }
                    else if(sum > target){
                        m--;
                    }
                    else{
                        k++;
                    }
                }
            }
        }

        //i is an iterator through the set
        for(auto i : set){
            out.push_back(i);
        }

        return out;
    }
};