# Logic:


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Define variables(window length, length of nums, ans array)
        window = 2 * k + 1
        n = len(nums)
        ans = [-1] * n

        # Edge case: 
        # Return ans array if WINDOW is greater than length of nums array
        if window > n:
            return ans
        # Calc our first window and add avg to ans[]
        curr = 0
        for i in range(window):
            curr += nums[i]
        ans[k] = curr // window
 
        # Go through remaining num values (which would be everything from window to end of array) and add avgs to ans
        for i in range(window, n):
            # Add next num value and subtract first num value
            curr += nums[i] - nums[i - window]
            # Add avg to next ans element which would be next element minus the k size
            ans[i - k] = curr // window
        
        return ans



            
