class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums,target):
            i=0
            j=len(nums)-1
            while i<=j:
                mid=i+(j-i)//2
                if nums[mid]<target:
                    i=mid+1
                else:
                    j=mid-1
            return i
        def find_right(nums,target):
            i=0
            j=len(nums)-1
            while i<=j:
                mid = i+(j-i)//2
                if nums[mid]<=target:
                    i=mid+1
                else:
                    j=mid-1
            return j
        x=find_left(nums,target)
        y=find_right(nums,target)
        if x<=y:
            return [x,y]
        else:
            return [-1,-1]
