import os
import re

# 扫描 target_dir 目录下的 子目录，并将子目录下的 ts 文件列表 合并成 mp4 输入到 out_dir
target_dir = '/Users/voidm/Downloads/'
out_dir = '/Users/voidm/Desktop/'


def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


def merge_in_dir(dir):
    dirs = os.listdir(dir)
    for sub_dir in dirs:
        if os.path.isdir(dir + sub_dir):
            print(f'merge with target sub dir : {sub_dir}')
            merge_body = ""
            for ts in sorted_aphanumeric(os.listdir(dir + sub_dir)):
                if ts.endswith(".ts"):
                    merge_body += f'file {ts}\r\n'
                    print(f'merge add in ts : {ts}')

            if not merge_body == '':
                with open(dir + sub_dir + '/merge.txt', 'w') as f:
                    f.write(merge_body)
                command = f'ffmpeg -f concat -safe 0 -i {dir}{sub_dir}/merge.txt -c copy {out_dir}{sub_dir}.mp4'
                print(f"command:{command}")
                print(os.system(command))


if __name__ == '__main__':
    # ffmpeg -f concat -safe 0 -i merge.txt -c copy out.mp4
    merge_in_dir(target_dir)
