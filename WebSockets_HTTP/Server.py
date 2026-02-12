from aiohttp import web # handles http and runs async event loop
import socketio # real time (live) event communication (listening)

# Implementing a server using socketio and aiohttp. We have combined them together


# creating a socket sever (async) -> e.g http://localhost:8080
# supports: client connections, events, emitting messages, Tracking sockets ID (Session ID)

socket_io = socketio.AsyncServer()
app = web.Application() # creates an aiohttp app/ webserver container
socket_io.attach(app) # VITAL: Attaches socketio to the app / connects Socket.IO to the aiohttp app


# http route handling
async def index(req):
    return web.Response(text=f'Hello {req}, Welcome to website!', content_type='text/html') # http response

async def houses(req):
    name = req.query.get("name", "Guest")
    return web.Response(text=f'Houses {name}', content_type='text/html') # http response



# Annotation: makes the function to listen for massage-type events, it'll be triggered when
#   those event occur (in this case from the Client). In this case the 'message' event
@socket_io.on('message')
async def print_message(socket_id, data):
    print(f"Socket ID: {socket_id}") # Prints the socket identifier (Session ID) of the client
    print(f"Data: {data}")  # Prints the data emitted by the event of the client

# Route
app.router.add_get('/', index) # requesting the root, from index page

# other routes
app.router.add_get('/houses', houses)
# app.router.add_post('/test', testing)

if __name__ == '__main__':
    web.run_app(app) # Starts the server


