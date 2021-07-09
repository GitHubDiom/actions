import subprocess
import glob
dir_list = glob.glob('*/')

def add_action():
    pass



for d in dir_list:
    path = f"{d}__main__.py"
    # args = ["wsk", "action", "update", url, path, "--web", "true", "--memory", str(memory), "--kind", container]

    print(path)