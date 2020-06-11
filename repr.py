class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def is_match_helper(s_index, p_index):
            if s[s_index] == '\0' and p[p_index] == '\0':
                return True
            
            if s[s_index] != '\0' and p[p_index] == '\0':
                return False

            if p[p_index + 1] == '*':
                if s[s_index] == p[p_index] or (p[p_index] == '.' and s[s_index] != '\0'):
                    return is_match_helper(s_index+1, p_index + 2) \
                        or is_match_helper(s_index+1, p_index)\
                        or is_match_helper(s_index, p_index+2)
                else:
                    return is_match_helper(s_index+1, p_index+2)
            if (s[s_index] == p[p_index] or (p[p_index] == '.' and s[s_index] != '\0')):
                return is_match_helper(s_index+1, p_index+1)
            
            return False


        s += '\0'
        p += '\0'
        return is_match_helper(0, 0)


if __name__ == "__main__":
    s = "mississippi"
    p = "mis*is*p*."
    solution = Solution()
    print(solution.isMatch(s, p))