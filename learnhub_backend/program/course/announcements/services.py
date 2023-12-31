from pydantic import TypeAdapter
from learnhub_backend.dependencies import (
    GenericOKResponse,
    Exception,
    mongo_datetime_to_timestamp,
)
from .database import (
    create_course_announcement,
    list_course_announcement,
    query_course_announcement,
    remove_course_announcement,
    edit_course_announcement,
    get_teacher_by_id,
)
from .schemas import (
    ListCourseAnnouncementsModelBody,
    ListCourseAnnouncementsResponseModel,
    PostCourseAnnouncementRequestModel,
    PostCourseAnnouncementResponseModel,
    GetCourseAnnouncementResponseModel,
    PatchCourseAnnouncementRequestModel,
)


def list_course_announcements_response(
    course_id: str, skip: int = 0, limit: int = 100
) -> ListCourseAnnouncementsResponseModel:
    quried_announcements = list_course_announcement(course_id, skip, limit)
    ta = TypeAdapter(list[ListCourseAnnouncementsModelBody])
    response_body = ListCourseAnnouncementsResponseModel(
        announcements=ta.validate_python(quried_announcements)
    )
    return response_body


def create_course_announcements_request(
    course_id: str, request_body: PostCourseAnnouncementRequestModel
) -> PostCourseAnnouncementResponseModel:
    created_id = create_course_announcement(
        course_id=course_id, announcement_body=request_body
    )
    response_body = PostCourseAnnouncementResponseModel(announcement_id=created_id)
    return response_body


def get_course_announcement_response(
    course_id: str, announcement_id: str
) -> GetCourseAnnouncementResponseModel:
    response_body = query_course_announcement(
        course_id=course_id, announcement_id=announcement_id
    )
    response_body["announcement_id"] = str(response_body["_id"])
    response_body["teacher"] = get_teacher_by_id(str(response_body["teacher_id"]))
    response_body["last_edit"] = mongo_datetime_to_timestamp(response_body["last_edit"])

    return GetCourseAnnouncementResponseModel(**response_body)


def patch_course_announcement_request(
    course_id: str,
    announcement_id: str,
    request_body: PatchCourseAnnouncementRequestModel,
):
    responese = edit_course_announcement(
        course_id=course_id, announcement_id=announcement_id, request_body=request_body
    )
    return GenericOKResponse


def delete_course_announcement_request(course_id: str, announcement_id: str):
    responese = remove_course_announcement(
        course_id=course_id, announcement_id=announcement_id
    )
    return GenericOKResponse
