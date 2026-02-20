class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ''
        subs = []
        cnt, start = 0, 0
        for i in range(len(s)):
            cnt += 1 if s[i] == '1' else -1
            if cnt == 0:
                inner = self.makeLargestSpecial(s[start+1:i])
                subs.append('1' + inner + '0')
                start = i + 1
        subs.sort(reverse=True)
        return ''.join(subs)
