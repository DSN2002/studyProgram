/*
 * @Author: DSN2002
 * @Date: 2021-11-12 12:34
 * @LastEditTime: 2021-11-12 17:12
 * @LastEditors: DSN2002
 * @Description:
 * 仅供研究使用，请勿用于其他活动
 */

#include<stdlib.h>
#include<stdio.h>
#include<string.h>

char fuhao[]  = {"\""};
char mode11[] = {"you-get -p mpv "};  //*用mpv观看 模式一 youget解析模式
char mode12[] = {"mpv "};             //*用mpv观看 模式一 YouTube-dl解析模式
//*显示视频真url 模式二
char mode2[] = {"you-get -u "};
//*显示视频真url 模式三
char mode31[] = {"you-get -o "};
char mode32[] = {"you-get -c "};
char mode33[] = {" -o "};
//*显示视频真url 模式二
char mode4[]  = {"you-get -i "};
char kongge[] = {" "};
char list[]   = {" --playlist "};
char gang[]   = {"\\"};
void main()
{}
void ygt_w(char url[200])
{//*模式一 youget观看视频
    static char mode[600];
    strcpy(mode,mode11);
    strcat(mode,fuhao);
    strcat(mode,url);
    strcat(mode,fuhao);
    system(mode);
}
void ytb_w(char url[200])
{//*模式一 youtube-dl观看视频
    static char mode[600];
    strcpy(mode,mode12);
    strcat(mode,fuhao);
    strcat(mode,url);
    strcat(mode,fuhao);
    system(mode);
}
void y_u(char url[200])
{//*模式二 youget解析视频url
    static char mode[600];
    strcpy(mode,mode2);
    strcat(mode,fuhao);
    strcat(mode,url);
    strcat(mode,fuhao);
    system(mode);
}
void y_od(char url[200],char path[40])
{//*模式三 youget下载单集视频
    static char mode[600];
    strcpy(mode,mode31);
    strcat(mode,path);
    strcat(mode,kongge);
    strcat(mode,fuhao);
    strcat(mode,url);
    strcat(mode,fuhao);
    system(mode);
}
void y_odc(char url[200],char path[40],char cookie[100])
{//*模式三 youget下载单集视频 需要cookie
    static char mode[600];
    strcpy(mode,mode32);
    strcat(mode,cookie);
    strcat(mode,mode33);
    strcat(mode,path);
    strcat(mode,kongge);
    strcat(mode,fuhao);
    strcat(mode,url);
    strcat(mode,fuhao);
    system(mode);
}
void y_ad(char url[200],char path[40],char fold[20],char cookie[100])
{//*模式三 youget下载全集视频
    static char mode[600];
    strcpy(mode,mode31);
    strcat(mode,path);
    strcat(mode,gang);
    strcat(mode,fold);
    strcat(mode,list);
    strcat(mode,fuhao);
    strcat(mode,url);
    strcat(mode,fuhao);
    system(mode);
}
void y_adc(char url[200],char path[40],char fold[20],char cookie[100])
{//*模式三 youget下载全集视频 需要cookie
    static char mode[600];
    strcpy(mode,mode32);
    strcat(mode,cookie);
    strcat(mode,mode33);
    strcat(mode,path);
    strcat(mode,gang);
    strcat(mode,fold);
    strcat(mode,list);
    strcat(mode,fuhao);
    strcat(mode,url);
    strcat(mode,fuhao);
    system(mode);
}
void y_l(char url[200])
{//*模式四 查看该url下的视频信息
    static char mode[600];
    strcpy(mode,mode4);
    strcat(mode,fuhao);
    strcat(mode,url);
    strcat(mode,fuhao);
    system(mode);
}
