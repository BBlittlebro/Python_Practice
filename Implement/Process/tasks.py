from invoke import task

@task
def mytime(ctx):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print("Local time is", time_str)

# 在terminal 可以輸入 invoke mytime 去呼叫函式