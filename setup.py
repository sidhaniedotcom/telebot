import os
os.system("pip install requests");os.system("pip install telethon");os.system("pip install colorama");os.system("pip install cython")
os.system("pkg install termux-elf-cleaner")
os.system("pkg install clang")
os.system("gcc `python-config --cflags --ldflags` -o bot bot.c `python-config --libs`")
os.remove("bot.c")
os.system("termux-elf-cleaner bot")
os.system("chmod +x bot")
print("✔ Setup Success")
