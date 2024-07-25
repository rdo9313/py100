info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
part = info.split(':')
result = '+'.join(part)
print(result)