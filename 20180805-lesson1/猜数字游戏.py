#coding:gbk
'''
1.��һ��100���ڵ�����
2.6�λ���
3.ÿ�β�ʱ���¶��ˣ����ˣ�С��
��ʾ������������ķ���
import random
random.randint(0, 100)

'''

import random

n = 1
num = random.randint(1,100)
while n <= 6:
    n += 1
    _input = int(input('pls input your num: '))
    if _input == num:
        print('{} = {} �¶���'.format(_input,num))
    elif _input >= num:
        print('{} > {} �´���'.format(_input,num))
    else:
        print('{} < {} ��С��'.format(_input,num))