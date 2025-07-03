
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        判断s t是否为字母异或词，即判断两者中的字母出现的数量是否一致
        这里直接使用26位字符串来记录字母出现的次数(s t仅包含小写字母)
        : params s: string s
        : params t: string s
        : return bool:
        """

        def stat_char(input_s: str) -> str:
            """
            统计字母出现的次数
            :param input_s:
            :return:
            """
            char_num = [0] * 26

            for char in input_s:
                char_num[ord(char) - ord("a")] += 1

            return ''.join(map(str, char_num))

        return stat_char(s) == stat_char(t)
