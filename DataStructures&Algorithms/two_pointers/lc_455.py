class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()
        c_p = 0
        content_children = 0
        while c_p < len(s) and content_children < len(g):
            if s[c_p] >= g[content_children]:
                content_children += 1
            c_p += 1
        return content_children
