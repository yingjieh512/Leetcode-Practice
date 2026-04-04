class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        letter_dict={}
        result=[]
        result_curr_index=0
        for i,char in enumerate(s):
            if char not in letter_dict:
                letter_dict[char]=[i,i]
            else:
                letter_dict[char][1]=i
        end=-1
        for char_index in range(len(s)):
            if char_index<=end:
                continue
            char=s[char_index]
            length_interval=letter_dict[char][1]-letter_dict[char][0]+1
            print(length_interval)
            start=letter_dict[char][0]
            end=letter_dict[char][1]
            result.append(length_interval)
            while True:
                for spanned in range(start,end+1):
                    spanned_char=s[spanned]
                    if letter_dict[spanned_char][1]>end:
                       end=letter_dict[spanned_char][1]
                       result[result_curr_index]=end-start+1
                max_end=end
                for spanned in range(start,end+1):
                    spanned_char=s[spanned]
                    if letter_dict[spanned_char][1]>end:
                       max_end=letter_dict[spanned_char][1]
                if max_end==end:
                    break
            result_curr_index+=1
        return result
            
        
       
        
                    
