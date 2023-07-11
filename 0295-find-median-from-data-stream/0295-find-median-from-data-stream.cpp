class MedianFinder {
public:
    priority_queue<int>pq1; //Max pq
    priority_queue<int,vector<int>,greater<int>>pq2; //Min Pq
    MedianFinder() {
    }
    
    void addNum(int num)
{
    if(pq1.size()==0&&pq2.size()==0)
    {
        pq1.push(num);
        return;
    }

    if(pq1.top()>=num)
    {
        pq1.push(num);
        if(pq1.size()-1>pq2.size())
        {
            pq2.push(pq1.top());
            pq1.pop();
        }
    }

    else
    {
        pq2.push(num);
        // cout<<"adding in pq2"<<num<<endl;
        if(pq2.size()-1>pq1.size())
        {
            pq1.push(pq2.top());
            pq2.pop();
        }
    }
}
    
    double findMedian() {
        double x=-1;
        if(pq2.empty()&&pq1.empty())
        {
            return x;
        }
        else if(pq2.empty())
        {
            return pq1.top();
        }

        if(pq1.size()==pq2.size())
        {
            return (pq1.top()+pq2.top())/2.0;
        }
        else if(pq1.size()>pq2.size())
        {
            return pq1.top();
        }
        else
        {
            return pq2.top();
        }
        
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */