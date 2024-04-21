import asyncio
import aiohttp
from faker import Faker


async def register_user(session, username, password):
    data = {'username': username, 'password': password}
    async with session.post('http://localhost:8080/register', json=data) as response:
        return await response.json()


async def login_user(session, username, password):
    data = {'username': username, 'password': password}
    async with session.post('http://localhost:8080/login', json=data) as response:
        return await response.json()


async def create_post(session, title, content):
    data = {'title': title, 'content': content}
    async with session.post('http://localhost:8080/posts', json=data) as response:
        return await response.json()


async def read_post(session, post_id):
    async with session.get(f'http://localhost:8080/posts/{post_id}') as response:
        return await response.json()


async def main():
    fake = Faker()
    async with aiohttp.ClientSession() as session:

        for _ in range(5):
            username = fake.user_name()
            password = fake.password()
            response = await register_user(session, username, password)
            print(response)

        for _ in range(3):
            username = fake.user_name()
            password = fake.password()
            response = await login_user(session, username, password)
            print(response)

        for _ in range(3):
            title = fake.sentence()
            content = fake.paragraph()
            response = await create_post(session, title, content)
            print(response)

        post_id = fake.random_int(min=1, max=3)  # Предполагается, что у вас есть посты с ID от 1 до 3
        response = await read_post(session, post_id)
        print(response)

if __name__ == '__main__':
    asyncio.run(main())
