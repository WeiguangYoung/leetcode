LCR 165. 解密数字

现有一串神秘的密文 ciphertext，经调查，密文的特点和规则如下：

密文由非负整数组成
数字 0-25 分别对应字母 a-z
请根据上述规则将密文 ciphertext 解密为字母，并返回共有多少种解密结果。



示例 1:
输入: ciphertext = 216612
输出: 6
解释: 216612 解密后有 6 种不同的形式，分别是 "cbggbc"，"vggbc"，"vggm"，"cbggm"，"cqggbc" 和 "cqggm" 
 

提示：
0 <= ciphertext < 231
 