from typing import Annotated
from fastapi import APIRouter, Depends

from learnhub_backend.dependencies import (
    GenericOKResponse,
    common_pagination_parameters,
    Exception,
)
from .schemas import (
    GetQuizResponseModel,
    GetQuizResultResponseModel,
    PatchQuizResultRequestModel,
    PatchQuizResultResponseModel,
    PostQuizRequestModel,
    PostQuizResponseModel,
)
from .services import (
    get_quiz_response,
    get_quiz_result_response,
    patch_quiz_result_response,
    post_quiz_request,
)


router = APIRouter(
    prefix="/quizzes",
    tags=["quizzes"],
    dependencies=[
        Depends(common_pagination_parameters),
        Depends(GenericOKResponse),
        Depends(Exception),
    ],
)

common_page_params = Annotated[dict, Depends(router.dependencies[0].dependency)]


@router.post(
    "/",
    status_code=200,
    response_model_exclude_none=True,
    response_model=PostQuizResponseModel,
)
def post_quiz(request_body: PostQuizRequestModel):
    response_body = post_quiz_request(request_body)
    return response_body


@router.get(
    "/{quiz_id}",
    status_code=200,
    response_model_exclude_none=True,
    response_model=GetQuizResponseModel,
)
def get_quiz(quiz_id: str):
    response_body = get_quiz_response(
        quiz_id=quiz_id,
    )
    return response_body


@router.get(
    "/{quiz_id}/result",
    status_code=200,
    response_model_exclude_none=True,
    response_model=GetQuizResultResponseModel,
)
def get_quiz_result(quiz_id: str, student_id: str):
    response_body = get_quiz_result_response(quiz_id=quiz_id, student_id=student_id)
    return response_body


@router.patch(
    "/{quiz_id}/result",
    status_code=200,
    response_model_exclude_none=True,
    response_model=PatchQuizResultResponseModel,
)
def patch_quiz_result(
    quiz_id: str, student_id: str, answers_body: PatchQuizResultRequestModel
):
    response_body = patch_quiz_result_response(
        quiz_id=quiz_id, student_id=student_id, answers_body=answers_body
    )
    return response_body
