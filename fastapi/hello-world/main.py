from fastapi import FastAPI
from fastapi.responses import FileResponse
#Create an Application Instance
app = FastAPI()

#App decorator for HTTP GET request at ROOT URL "/"
@app.get("/")
def read_root():
    return {"message": "Hello-World"}

@app.get("/new-home")
def read_root():
    return FileResponse("index.html")

@app.get("/users")
def read_root():
    return {"message": "This is user page"}

#Dynamic Route and type validation
@app.get("/users/{id}")
def read_user(id: int):
    return {"message": f"This is user {id} page"}


@app.get("/users/{id}/contact")
def read_user(id: int):
    return {"message": f"This is user {id} contact page. His contact no. is 911"}


@app.get("/contact")
def read_root():
    return FileResponse("contact.html")



# Dynamic Routes
@app.get('/blog/{id}')
def blog(id):
    return {"Type": "blog", 'id': {id} }



#Query Parameters

@app.get('/blog')
def blog(limit: int = 5, published: bool = True, num_comments: Optional[int] = None, sort : Optional[bool]= None):
    return {"Type": "blog", "limit": limit, "Published": published, "no. Of comments": num_comments}



'''
#Add Data-validation logic to function. ID should always be integer
@app.get('/blog/{id}')
def blog(id: int):
    return {"Type": "blog", 'id': {id} }

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {"Type": "Comments", 'Blog-id': {id} }

#***************QUERY-PARAMETERS***********

@app.get('/blog')
def blog(limit: int = 10, unpublished: bool = False, sort: Optional[str] = None):
    return {"Type": "blog", "limit": limit, "unPublished": unpublished}

@app.post('/blog32')
def createBlog(title: str, body: str, id: int, unPublished: bool, sort: Optional[str] = None):
    return {'message': "Blog is saved", 'Title': title, 'Body': body, 'unPublished': 'unpublished', 'id': id}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    id: int

@app.post('/blog')
def createBlog(new_blog: Blog):
    return {'message': "Blog is saved", 'Title': {new_blog.title}, 'Body': {new_blog.body}}
'''