import asyncio

import aiohttp


def create_tasks(session: aiohttp.ClientSession):
    url = 'http://127.0.0.1:5000/file/{}/'

    tasks = []

    files = ['file1.json', 'file2.json', 'file3.json']

    for file in files:
        tasks.append(asyncio.create_task(session.get(url.format(file))))
        print(f'{file} has loaded')

    return tasks


async def get_data():
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = create_tasks(session)

        response = await asyncio.gather(*tasks)

        for item in response:
            results += await item.json()

    return sorted(results, key=lambda k: k['id'])
