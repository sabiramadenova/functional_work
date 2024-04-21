import asyncio

from aiohttp import web
import json


async def register(request):
    data = await request.json()

    return web.json_response({'message': 'User registered successfully', 'data': data})


async def login(request):
    data = await request.json()

    return web.json_response({'message': 'User logged in successfully', 'data': data})


async def create_post(request):
    data = await request.json()

    return web.json_response({'message': 'Post created successfully', 'data': data})


async def read_post(request):
    post_id = request.match_info['post_id']

    return web.json_response({'message': f'Reading post with ID {post_id}'})


async def init_app():
    app = web.Application()
    app.router.add_post('/register', register)
    app.router.add_post('/login', login)
    app.router.add_post('/posts', create_post)
    app.router.add_get('/posts/{post_id}', read_post)
    return app

if __name__ == '__main__':
    app = asyncio.run(init_app())
    web.run_app(app, host='localhost', port=8080)
