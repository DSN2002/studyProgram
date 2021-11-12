/*
 * @Author: DSN2002
 * @Date: 2021-11-12 12:34
 * @LastEditTime: 2021-11-12 14:02
 * @LastEditors: DSN2002
 * @Description:
 * 仅供研究使用，请勿用于其他活动
 */

#include<stdlib.h>
#include<stdio.h>
#include<string.h>
char url[200];
char mode[600];
char path[40];
char cookie[100];
char fuhao[]  = {"\""};
char mode11[] = {"you-get -p mpv "};  //*用mpv观看 模式一 youget解析模式
char mode12[] = {"mpv "};             //*用mpv观看 模式一 YouTube-dl解析模式
char mode2[]  = {"you-get -u "};      //*显示视频真url 模式二
//*显示视频真url 模式二
char mode3[]  = {"you-get -o "};
char mode31[] = {" -o "};
//*显示视频真url 模式二
char mode4[]  = {"you-get -i "};
void main()
{
    scanf("%s",url);
    strcpy(mode,mode12);
    strcat(mode,fuhao);
    strcat(mode,url);
    strcat(mode,fuhao);
    printf("%s\n",mode);
    system(mode);
}
char yougetwatch(char 1,char 2)
{

}
char yougetwatch(char 1,char 2)
{

}
char yougetwatch(char 1,char 2)
{

}
char yougetwatch(char 1,char 2)
{

}
char yougetwatch(char 1,char 2)
{

}
char yougetwatch(char 1,char 2)
{

}
char yougetwatch(char 1,char 2)
{

}
