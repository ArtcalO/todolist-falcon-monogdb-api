from pydantic import BaseModel, Field, constr
from spectree import ExternalDocs, Response, SpecTree, Tag

class Resp(BaseModel):
    title: str = Field(
        ...,
        max_length=100
    )
    body: str = Field(
        ...,
        max_length=1000
    )


class BadLuck(BaseModel):
    loc: str
    msg: str
    typ: str

class Query(BaseModel):
    title: str = Field(
        ...,
        max_length=100
    )
    body: str = Field(
        ...,
        max_length=1000
    )

class Task(BaseModel):
    title: constr(min_length=2, max_length=40)  # Constrained Str
    body: constr(min_length=2, max_length=40)  # Constrained Str


spec = SpecTree(
    "falcon",
    title="Todo list",
    version="0.1.2",
    description="To do list api demo",
    terms_of_service="https://github.io",
    contact={"name": "ArtcalO", "email": "artcalo@ksquad.dev", "url": "https://github.com/ArtcalO"},
    license={"name": "KSQUAD", "url": "https://ksquad.dev"},
)

demo = Tag(
    name="demo", description="😊", externalDocs=ExternalDocs(url="https://github.com/ArtcalO")
)