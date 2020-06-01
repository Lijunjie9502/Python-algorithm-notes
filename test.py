class Solution:
    def replaceSpace(self, s: str) -> str:
        if len(s) == 0: return ''
        num_of_blanks = 0
        for ch in s:
            if ch = ' ':
                num_of_blanks += 1

        res_length = len(s) + num_of_blanks*2
        str_list = [None]*(res_length)

        for ch in reversed(s):
            if ch != ' ':
                res_length -= 1
                str_list[res_length] = ch
            else:
                res_length -= 1
                str_list[res_length] = '0'
                res_length -= 1
                str_list[res_length] = '2'
                res_length -= 1
                str_list[res_length] = '%'
        return ''.join(str_list)
        
        
