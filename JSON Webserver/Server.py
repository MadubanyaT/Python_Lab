from aiohttp import web

app = web.Application()

users = [
    {'id': 1, 'name': "Lerato"},
    {'id': 2, 'name': "Tshepang"},
    {'id': 3, 'name': "Thabo"},
    {'id': 4, 'name': "Lesiba"}
]


async def index(req):
    return web.json_response({'status': 'Python Server Running'})

async def get_users(req):
    return web.json_response(users)

async def get_user(req):
    user_id = int(req.match_info['id'])

    for user in users:
        if user_id == user['id']:
            return web.json_response(user)

    return web.json_response({'error': 'User not found'}, status=404)

async def add_user(req):
    name = await req.json()

    n = len(users) + 1
    users.append({'id': n, 'name': name})

    return web.json_response({"message": "User created"})


async def delete_user(req):
    user_id = int(req.match_info['id'])

    for user in users:
        if user_id == user['id']:
            users.remove(user)
            return web.json_response({"message": "User removed successfully"})

    return web.json_response({'error': 'User not found'}, status=404)


app.router.add_get('/', index)
app.router.add_get('/api/users', get_users)
app.router.add_get('/api/user/{id}', get_user)
app.router.add_post('/api/users', add_user)
app.router.add_post('/api/users/{id}', delete_user)


if __name__ == "__main__":
    web.run_app(app)





