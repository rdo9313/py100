info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

'+'.join(info.split(':'))
info.replace(':', '+')