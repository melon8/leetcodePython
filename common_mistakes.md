## 常见错误

1. python 返回的答案应该是符合条件的下标例如 s[max_len_i:max_len_j+1]，然而返回了 s[i,j+1]

2. 注意自己加括号明确优先级，例如python == 的优先级比大于小于高 （例如 1<3 == False 结果是False，因为相当于 a< (3==False)）