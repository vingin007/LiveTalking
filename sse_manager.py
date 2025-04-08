sse_queues = {}

# 如果你想包装个方法来安全地放消息
async def put_sse(sessionid: int, message: str):
    if sessionid not in sse_queues:
        return
    await sse_queues[sessionid].put(message)

# 也可以加更多辅助函数