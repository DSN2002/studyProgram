# -*- coding: utf-8 -*-
# Author: DSN2002
# Date: 2021-11-12 14:31
# LastEditTime: 2021-11-12 14:33
# LastEditors: DSN2002
# Description:
# 仅供研究使用，请勿用于其他活动
#
from subprocess import getstatusoutput

g = getstatusoutput('pip list --outdated -i https://pypi.mirrors.ustc.edu.cn/simple')

if g[0] != 0:
    print('获取更新列表失败，请重新运行！')
    exit(0)

else:
    if len(g[1]) == 0:
        print('所有的库都是最新的，无需更新。')
        exit(0)

    else:
        print('过期的库有：\n', g[1])
        past_list = []
        g_list = g[1].split('\n')
        for i in g_list[2:]:
            past_list.append(i.split(' ')[0])

        fail_list = []
        for i in past_list:
            try:
                print(f'开始更新库：{i}……')
                update = getstatusoutput(f'pip install --upgrade {i} -i https://pypi.mirrors.ustc.edu.cn/simple')
                if update[0] == 0:
                    print(f'{i}:已更新完成。')
                else:
                    print(f'{i}:更新失败！')
                    fail_list.append(i)
            except Exception:
                pass

        if len(fail_list) == 0:
            print('所有库已全部更新')
        else:
            print('以下库更新失败，请重新运行程序，或手动更新。\n', fail_list)
