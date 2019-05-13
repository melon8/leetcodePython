class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)
        # A是短的那个list，B是长的list
        if m > n:
            A, B, m, n = B, A, len(nums2), len(nums1)

        # i是指向A中元素的指针（包括m），j是指向B中元素的指针(包括)，
        # i 和 j 的含义是左边的元素是两数组的一半的数,所以i随意算则[0,m],j随之确定
        # 如果A[i-1]< B[j] and A[i] > B[j-1]，则：
        # 如果 m+n 是偶数，则两指针左边数的总数(m+n)/2， 
        # 则中位数是(max(A[i-1],B[j-1]), min(A[i], B[j]))/2
        # 如果奇数则两指针左边总数(m+n+1)/2，左边多一个
        # 中位数是 min(A[i],B[j])
        
        # 使用二分的选择 i 来优化 (python 3 // 结果是int，/结果是float)
        imin, imax = 0, m
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i
            if i < m and A[i] < B[j-1]:
                # i小了，需要变大
                imin = i+1
            elif i > 0 and A[i-1] > B[j]:
                # i大了，需要变小
                imax = i-1
            else:
                # i 已经正确了
                max_left, min_right = 0, 0
                if i == 0:max_left = B[j-1]
                elif j == 0:max_left = A[i-1]
                else:max_left = max(A[i-1], B[j-1])
                # 奇数
                if (m+n) % 2 == 1:
                    return max_left
                
                # 偶数
                if i == m:min_right = B[j]
                elif j == n:min_right = A[i]
                else:min_right = min(A[i], B[j])

                return (max_left + min_right)/2
            
        
        
            