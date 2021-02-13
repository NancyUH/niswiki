import os
import shutil

# グローバル変数
root_dir = "docs"
sidebar_file = open(f"{root_dir}/_sidebar.md", 'w')
toppage_file = open(f"{root_dir}/README.md", 'a')


# ディレクトリに README.md が存在するか
def is_exist_readme(path):
    path = root_dir + '/' + path
    return os.path.isfile(f"{path}/README.md")


# ルートディレクトリより下層のディレクトリを再帰的に探索する
def search_dir(path):
    # 引数の path のサブディレクトリを取得する
    root_path = root_dir + '/' + path
    files = [d for d in os.listdir(
        root_path) if os.path.isdir(os.path.join(root_path, d))]

    for file in files:
        if file[0] != '_':
            file = file.replace(" ", "%20")
            search_path = path + '/' + file
            step = '  ' * (search_path.count('/') - 1)
            if is_exist_readme(search_path):
                sidebar_file.write(f"{step}- [{file}]({search_path}/README)\n")
                toppage_file.write(f"{step}- [{file}]({search_path}/README)\n")
            else:
                sidebar_file.write(f"{step}- {file}\n")
                toppage_file.write(f"{step}- {file}\n")
            search_dir(search_path)


def main():
    shutil.copyfile('./docs/index.md', './docs/README.md')
    toppage_file.write('\n## 目次\n\n')
    search_dir('')
    sidebar_file.close()
    toppage_file.close()


if __name__ == "__main__":
    main()
