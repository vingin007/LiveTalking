# 全局只需要一个源队列，用于广播（生产者）写入
import asyncio

broadcast_queue = asyncio.Queue()

# 存放所有活跃客户端的独立队列
client_queues = set()