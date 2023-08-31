from fastapi import APIRouter, Depends
from typing import Annotated, Union

from ..dependencies import common_pagination_parameters
from .schemas import ListProgramsResponseModel
from .services import list_programs_response, list_lessons_response, get_lesson_response
from .exceptions import Exception


router = APIRouter(
    prefix="/programs",
    tags=["program"],
    dependencies=[Depends(common_pagination_parameters)],
)

common_page_params = Annotated[dict, Depends(router.dependencies[0].dependency)]


@router.get(
    "/",
    status_code=200,
    response_model=ListProgramsResponseModel,
    response_model_exclude_none=True,
)
def list_programs(common_paginations: common_page_params):
    response_body = list_programs_response(
        common_paginations["skip"], common_paginations["limit"]
    )
    return response_body


@router.get(
    "/courses/{course_id}/chapters/{chapter_id}/lessons",
    status_code=200,
    response_model_exclude_none=True,
)
def list_lessons(
    course_id: str, chapter_id: str, common_paginations: common_page_params
):
    response_body = list_lessons_response(
        common_paginations["skip"], common_paginations["limit"]
    )
    return response_body


@router.get(
    "/courses/{course_id}/chapters/{chapter_id}/lessons/{lesson_id}",
    status_code=200,
    response_model_exclude_none=True,
)
def get_lesson(course_id: str, chapter_id: str, lesson_id: str):
    response_body = get_lesson_response(lesson_id)
    if response_body == None:
        raise Exception.not_found
    return response_body
