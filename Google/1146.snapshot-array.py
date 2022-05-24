#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

# @lc code=start
class SnapshotArray:

    def __init__(self, length: int):

        self.nums = {}
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.nums[index] = val
        #print(self.snaplist)
        #print(self.snapid)

    def snap(self) -> int:
        self.snaps.append(self.nums.copy())
        return len(self.snaps) - 1  

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        else:
            return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

