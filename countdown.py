import sys
from datetime import datetime
from colorama import Fore, Style, init
from dateutil import parser

init(autoreset=True)


def countdown(target_date_str):
    try:
        # 將字串轉成日期
        target_date = parser.parse(target_date_str)
        today = datetime.now()
        delta = target_date.date() - today.date()
        days_remaining = delta.days

        # 顯示不同狀態
        if days_remaining > 0:
            print(f"{Fore.GREEN}距離 {target_date_str} 還有 {days_remaining} 天 ✨")
        elif days_remaining == 0:
            print(f"{Fore.YELLOW}今天就是 {target_date_str}！🎉")
        else:
            print(f"{Fore.RED}{target_date_str} 已經過了 {-days_remaining} 天 🕒")
    except ValueError:
        print(f"{Fore.RED}⚠️ 日期格式錯誤，請用 YYYY-MM-DD，例如 2025-12-31 或 12/31/2025")


def usage():
    print(f"{Fore.CYAN}用法: python countdown.py YYYY-MM-DD")
    print(f"範例: python countdown.py 2025-12-31")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    else:
        countdown(sys.argv[1])
