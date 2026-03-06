class SegmentTree:

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0]*(4*self.n)
        self.build(nums, 0, 0, self.n-1)

    def build(self, nums, node, l, r):

        if l == r:
            self.tree[node] = nums[l]
            return

        mid = (l+r)//2

        self.build(nums, 2*node+1, l, mid)
        self.build(nums, 2*node+2, mid+1, r)

        self.tree[node] = max(self.tree[2*node+1], self.tree[2*node+2])

    def update(self, node, l, r, idx, val):

        if l == r:
            self.tree[node] = val
            return

        mid = (l+r)//2

        if idx <= mid:
            self.update(2*node+1, l, mid, idx, val)
        else:
            self.update(2*node+2, mid+1, r, idx, val)

        self.tree[node] = max(self.tree[2*node+1], self.tree[2*node+2])

    def query_max(self, node, l, r, ql, qr):

        if qr < l or ql > r:
            return float("-inf")

        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l+r)//2

        left = self.query_max(2*node+1, l, mid, ql, qr)
        right = self.query_max(2*node+2, mid+1, r, ql, qr)

        return max(left, right)


if __name__ == "__main__":

    nums = [2,5,1,4,9,3]

    seg = SegmentTree(nums)

    print(seg.query_max(0,0,len(nums)-1,1,4))

    seg.update(0,0,len(nums)-1,2,10)

    print(seg.query_max(0,0,len(nums)-1,1,4))