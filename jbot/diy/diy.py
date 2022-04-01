"""
要求：
    1、需要具备一定的 python3 知识；
    2、清楚自己需要编辑代码的区域；
    3、清楚自己需要导入的变量的位置和变量名。
"""


from .. import chat_id, jdbot, logger, _LogDir
from telethon import events, Button
from asyncio import exceptions
import requests, re, asyncio, time, sys, os ,json
import datetime, random
"""
如果需要导入 diy 目录内某个文件的变量或函数
from ..diy.xxx import xxx
例如：from ..diy.utils import ql_token
"""

"""
如果需要导入 bot 目录内某个文件的变量或函数
from ..bot.xxx import xxx
例如：from ..bot.utils import myck
"""


"""
如果需要导入其他第三方库
import xxx
例如：import json
"""


async def cmddiy(cmdtext):
    '''定义执行cmd命令'''
    try:
        msg = await jdbot.send_message(chat_id, '开始执行命令')
        p = await asyncio.create_subprocess_shell(
            cmdtext, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        res_bytes, res_err = await p.communicate()
        res = res_bytes.decode('utf-8')
        # if res.find('先登录') > -1:
        #     await jdbot.delete_messages(chat_id, msg)
        #     res, msg = ql_login()
        #     await jdbot.send_message(chat_id, msg)
        #     return
        if len(res) == 0:
            await jdbot.edit_message(msg, '已执行，但返回值为空')
        elif len(res) <= 200:
            await jdbot.delete_messages(chat_id, msg)
            await jdbot.send_message(chat_id, res)
        elif len(res) > 200:
            tmp_log = f'{_LogDir}/bot/{cmdtext.split("/")[-1].split(".js")[0]}-{datetime.datetime.now().strftime("%H-%M-%S")}-{random.randint(0,10)}.log'
            with open(tmp_log, 'w+', encoding='utf-8') as f:
                f.write(res)
            await jdbot.delete_messages(chat_id, msg)
            await jdbot.send_message(chat_id, '执行结果较长，请查看日志', file=tmp_log)
            os.remove(tmp_log)
    except Exception as e:
        await jdbot.send_message(chat_id, f'something wrong,I\'m sorry\n{str(e)}')
        logger.error(f'something wrong,I\'m sorry\n{str(e)}')

async def cmddiyNo(cmdtext):
    '''定义执行cmd命令'''
    try:
        msg = await jdbot.send_message(chat_id, '开始执行命令')
        p = await asyncio.create_subprocess_shell(
            cmdtext, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        res_bytes, res_err = await p.communicate()
        res = res_bytes.decode('utf-8')
        # if res.find('先登录') > -1:
        #     await jdbot.delete_messages(chat_id, msg)
        #     res, msg = ql_login()
        #     await jdbot.send_message(chat_id, msg)
        #     return
        if len(res) == 0:
            await jdbot.edit_message(msg, '已执行，但返回值为空')
        elif len(res) <= 200:
            await jdbot.delete_messages(chat_id, msg)
            await jdbot.send_message(chat_id, res)
        elif len(res) > 200:
            #tmp_log = f'{LOG_DIR}/bot/{cmdtext.split("/")[-1].split(".js")[0]}-{datetime.datetime.now().strftime("%H-%M-%S")}-{random.randint(0,10)}.log'
            #with open(tmp_log, 'w+', encoding='utf-8') as f:
            #    f.write(res)
            await jdbot.edit_message(msg, '执行结果不发送文件')
            await asyncio.sleep(3)
            await jdbot.delete_messages(chat_id, msg)
            #await jdbot.send_message(chat_id, '执行结果较长，请查看日志', file=tmp_log)
            #os.remove(tmp_log)
    except Exception as e:
        await jdbot.send_message(chat_id, f'something wrong,I\'m sorry\n{str(e)}')
        logger.error(f'something wrong,I\'m sorry\n{str(e)}')


async def openCard():
    try:
        """
        try 部分则自由发挥即可
        """

        # 例如下行代码代表在调用且运行此函数时，机器人给你发送一条消息
        # await jdbot.send_message(chat_id, "Hello World") # （注释此行即可）
        msg = await jdbot.send_message(chat_id, "开始开卡有礼")
        await cmddiyNo("task /ql/scripts/jd_open_card_by_shopid.js")
        await jdbot.delete_messages(chat_id,msg)


    except Exception as e:
        await jdbot.send_message(chat_id, 'something wrong,I\'m sorry\n' + str(e))
        logger.error('something wrong,I\'m sorry\n' + str(e))


async def gua_zdjr_new():
    try:
        """
        try 部分则自由发挥即可
        """

        # 例如下行代码代表在调用且运行此函数时，机器人给你发送一条消息
        # await jdbot.send_message(chat_id, "Hello World") # （注释此行即可）
        msg = await jdbot.send_message(chat_id, "开始组队瓜分")
        await cmddiy("task /ql/scripts/gua_zdjr_new.js desi JD_COOKIE 1-20")
        await jdbot.delete_messages(chat_id,msg)


    except Exception as e:
        await jdbot.send_message(chat_id, 'something wrong,I\'m sorry\n' + str(e))
        logger.error('something wrong,I\'m sorry\n' + str(e))


async def jd_ShareGift():
    try:
        """
        try 部分则自由发挥即可
        """

        # 例如下行代码代表在调用且运行此函数时，机器人给你发送一条消息
        # await jdbot.send_message(chat_id, "Hello World") # （注释此行即可）
        msg = await jdbot.send_message(chat_id, "开始人头分享")
        await cmddiy("task /ql/scripts/jd_ShareGift.js")
        await jdbot.delete_messages(chat_id,msg)


    except Exception as e:
        await jdbot.send_message(chat_id, 'something wrong,I\'m sorry\n' + str(e))
        logger.error('something wrong,I\'m sorry\n' + str(e))


async def jd_smiek_luckDraw_activityUrl():
    try:
        """
        try 部分则自由发挥即可
        """

        # 例如下行代码代表在调用且运行此函数时，机器人给你发送一条消息
        # await jdbot.send_message(chat_id, "Hello World") # （注释此行即可）
        msg = await jdbot.send_message(chat_id, "开始抽奖有礼")
        await cmddiyNo("task /ql/scripts/gua_luckDraw.js desi JD_COOKIE 40-55")
        await jdbot.delete_messages(chat_id,msg)


    except Exception as e:
        await jdbot.send_message(chat_id, 'something wrong,I\'m sorry\n' + str(e))
        logger.error('something wrong,I\'m sorry\n' + str(e))