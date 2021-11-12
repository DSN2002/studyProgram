/*
 * @Author: DSN2002
 * @Date: 2021-11-12 17:33
 * @LastEditTime: 2021-11-12 19:13
 * @LastEditors: DSN2002
 * @Description:
 * 仅供研究使用，请勿用于其他活动
 */

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
void main(){}
char mode[600];
char dian[]={"\""};
char jiexi[]={"you-get -p mpv "};
int add(int x ,int y)
{
    x += y;
    return x;
}
int sum(int num)
{
    int n=0,i;
    for(i=1;i<num;i++)
        {
        n = n +i;
        }
    return n;
}
void url(char str[400])
{
    strcpy(mode,jiexi);
    printf("%s\n",mode);
    strcat(mode,dian);
    printf("%s\n",mode);
    strcat(mode,str);
    printf("%s\n",mode);
    strcat(mode,dian);
    printf("%s\n",mode);
    system(mode);
}
