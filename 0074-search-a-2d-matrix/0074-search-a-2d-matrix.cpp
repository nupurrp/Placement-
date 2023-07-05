class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int row = 0;
        int column = matrix[0].size() - 1;      // column size

        while(row < matrix.size() && column >= 0) {
            if(matrix[row][column] == target)
                return true;

            if(matrix[row][column] < target) 
                row++;
            
            else 
                column--;
        }

        return false;
    }
};