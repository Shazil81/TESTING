class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # optimal solution two pointer approach
        my_dict = {}
        max_length, left, right = 0, 0, 0
        n = len(fruits)
        while right < n:
            # dict me add kro fruits ko count kr k
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1
            # according to question yhi hai ki 2 se zyada fruits nhi le skte hain
            if len(my_dict) > 2:
                # ab jab 2 se zayad fruit hoga dict me to us fruit ka count ghata denge
                my_dict[fruits[left]] -= 1
                # agar koi fruit ka dict me count 0 ho gya to us fruit ko delete kr do dict se
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                # window ko valid krne k liye left ko badha do
                left+=1
            # jab length dict ka 2 ya usse kam rhega tb hi max length update hoga
            if len(my_dict) <= 2:
                max_length = max(max_length, right-left+1)
            right+=1
        return max_length
