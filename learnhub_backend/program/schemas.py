from typing import Optional, Union
from pydantic import BaseModel, HttpUrl


## Programs
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


## Lessons
class GetLessonResponseModel(BaseModel):
    lesson_id: str
    lesson_num: int
    name: str
    lesson_type: str
    description: str
    src: HttpUrl
    progress: Optional[float]  # TODO: only return progress, If student_id is attached.


class ListLessonsModelBody(BaseModel):
    lesson_id: str
    lesson_num: int
    name: str
    lesson_type: str
    video_length: Optional[int]  # only return if lesson type = 'video'


class ListLessonsResponseModel(BaseModel):
    lessons: list[ListLessonsModelBody]


class PostLessonRequestModel(BaseModel):
    lesson_num: int
    name: str
    description: str
    src: HttpUrl
