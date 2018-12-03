#!/bin/bash
set -eu

# 当前路径
my_dir=$(cd "$(dirname ${0})";pwd)
root_dir=$(dirname "${my_dir}")

# 运行测试用例
hrun ./case/

# 清理过期reports
if [[ -d ${my_dir}/reports ]];then
    find ${my_dir}/reports/ -maxdepth 1 -type f -mtime 7 -exec rm -rf {} \;
fi