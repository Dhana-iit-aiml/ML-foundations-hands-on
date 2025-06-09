
def legacysupport(x):
    def executor(*args, **kwargs):
        if len(args) == 1:
            args = list(args)
            args.extend(["prathik","secret"])
        return x(*args, **kwargs)
    return executor
@legacysupport
def connect(url, username="", password=""):
    print(url, username, password)
connect("localhost")