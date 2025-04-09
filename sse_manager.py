import asyncio
from aiohttp import web

# 存放所有用户的队列, user_queues[user_id] = queue
user_queues = {}