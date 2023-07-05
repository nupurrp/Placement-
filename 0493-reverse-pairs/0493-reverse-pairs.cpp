class Solution {
public:
     int merge(vector<int>& nums, int lo , int mid , int hi )
    {
        int cnt = 0;
        for (int i = mid+1; i <= hi; i++)
        {
            int x = nums[i];
          auto up =   upper_bound(nums.begin()+lo, nums.begin()+mid+1,2*(1ll)*x);
           cnt += ((nums.begin() + mid) - up + 1 ) ;

        }
        vector<int> temp;

        int i = lo;
          int j = mid+1;

        while(i <= mid && j <= hi)
        {
            if(nums[i] < nums[j])
            {
                temp.push_back(nums[i]);
                i++;
            }

            else

            {
             temp.push_back(nums[j]);
                j++;
            }
        }

        while(i <= mid)
        {
            
                temp.push_back(nums[i]);
                i++;
            

        }

        while(j <= hi)
        {
                 temp.push_back(nums[j]);
                j++;
            
        }
        

        for (int i = lo; i <= hi; i++)
        {
            nums[i]= temp[i-lo];
        }

        return cnt;
    }
    int mergesort(vector<int>& nums, int lo , int hi)
    {
        if(hi <= lo)
        return 0;
        int mid = (lo+hi)/2;

        int cnt = 0;

        cnt+= mergesort(nums,lo,mid);
        cnt+= mergesort(nums,mid+1,hi);

            
    
        cnt+=merge( nums,lo,mid,hi );

        return cnt;

    }
    int reversePairs(vector<int>& nums) {
        
       return mergesort(nums,0,nums.size()-1);

   
    }
};