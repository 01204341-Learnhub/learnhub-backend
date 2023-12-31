from typing import Union
from pydantic import BaseModel, HttpUrl


## PROGRAMS
class ListProgramsClassModelBody(BaseModel):
    class_id: str
    type: str
    name: str

    model_config = {
        "json_schema_extra": {
            "examples": [{"class_id": "1234", "type": "class", "name": "Discreet Math"}]
        }
    }


class ListProgramsCourseModelBody(BaseModel):
    course_id: str
    type: str
    name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"course_id": "1234", "type": "course", "name": "Intro to Python"}
            ]
        }
    }


class ListProgramsResponseModel(BaseModel):
    programs: list[Union[ListProgramsClassModelBody, ListProgramsCourseModelBody]]


# TAGS
class TagModelBody(BaseModel):
    tag_id: str
    tag_name: str


class ListTagsResponseModel(BaseModel):
    tags: list[TagModelBody]


class PostTagRequestModel(BaseModel):
    tag_name: str


class PostTagResponseModel(BaseModel):
    tag_id: str
