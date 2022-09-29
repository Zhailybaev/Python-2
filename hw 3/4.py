import re
number=['+7 777 621 34 56', '87012345678', '+77078904367', '874556', '+7878904367']
for x in number:
    pattern=re.findall(r'(^\+7|^8)(\s?)(705|708|707|701|747|777)(\s?)[\d]{3}(\s?)[\d]{2}(\s?)[\d]{2}',x)
    if pattern:
        print("YES")
    else:
        print("NO")
