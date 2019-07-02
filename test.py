from fabric import Connection
result = Connection('mdeyoung@10.10.0.102').run('uname -s',hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(result))

