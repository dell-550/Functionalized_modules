#!/bin/bash


DEFAULT_SINCE="2024-01-01"
DEFAULT_UNTIL="2024-12-31"
# 默认参数值
AUTHOR=""
SINCE=""
UNTIL=""

FILEDIR2="./sites/*/spiders/*" 
FILEDIR1="./sites/*/parser/*"
# 使用命名参数解析命令行输入
while [ "$#" -gt 0 ]; do
  case "$1" in
    -a|--author)
      AUTHOR="$2"
      shift 2
      ;;
    -s|--since)
      SINCE="$2"
      shift 2
      ;;
    -u|--until)
      UNTIL="$2"
      shift 2
      ;;
    *)
      echo "Unknown parameter passed: $1"
      echo "Usage: $0 -a <author> -s <since_date> -u <until_date>"
      echo "Example: $0 -a 'luorenjie' -s '2024-06-01' -u '2024-08-31'"
      exit 1
      ;;
  esac
done

# 检查必要的参数是否已提供
if [ -z "$AUTHOR" ]; then
  echo "Missing required parameters."
  echo "Usage: $0 -a <author>"
  exit 1
fi

SINCE="${SINCE:-$DEFAULT_SINCE}"
UNTIL="${UNTIL:-$DEFAULT_UNTIL}"



# 执行git log命令并统计行数
echo "查询时间：$SINCE  到 $UNTIL"
git log --author="$AUTHOR" --since="$SINCE" --until="$UNTIL" --pretty=tformat: --numstat -- "$FILEDIR1" "$FILEDIR2" | \
awk '{ add += $1 ; subs += $2 ; loc += $1 - $2 }
 END { printf "新增代码行数: %s\n删除代码行数: %s\n共计代码行数: %s\n", add, subs, loc }'

