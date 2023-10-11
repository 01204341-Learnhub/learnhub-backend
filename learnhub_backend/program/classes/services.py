from pydantic import TypeAdapter

from learnhub_backend.dependencies import (
    GenericOKResponse,
    mongo_datetime_to_timestamp,
    utc_datetime_now,
    utc_datetime,
)

from .database import (
    create_class,
    edit_class,
    query_list_classes,
    get_teacher_by_id,
    query_list_tags_by_id,
    query_class,
    query_list_threads,
    create_thread,
    query_thread,
    edit_thread,
)
from .schemas import (
    ListClassesModelBody,
    ListClassesResponseModel,
    GetClassResponseModel,
    PatchClassRequestModel,
    PostClassRequestModel,
    PostClassResponseModel,
    ListThreadModelBody,
    ListThreadResponseModel,
    PostThreadRequestModel,
    PostThreadResponseModel,
    GetThreadResponseModel,
    PatchThreadRequestModel,
)

from ...dependencies import Exception


# CLASSES
def list_classes_response(skip: int, limit: int) -> ListClassesResponseModel:
    classes_corsor = query_list_classes(skip=skip, limit=limit)
    quried_classes = []
    for class_ in classes_corsor:
        if utc_datetime(class_["registration_ended_date"]) > utc_datetime_now():
            continue  # continue if you can't buy class anymore
        class_["class_id"] = str(class_["_id"])
        class_["teacher"] = get_teacher_by_id(str(class_["teacher_id"]))
        class_["tags"] = query_list_tags_by_id(class_["tags"])
        class_["registration_ended_date"] = mongo_datetime_to_timestamp(
            class_["registration_ended_date"]
        )
        class_["open_date"] = mongo_datetime_to_timestamp(class_["open_date"])
        class_["class_ended_date"] = mongo_datetime_to_timestamp(
            class_["class_ended_date"]
        )
        quried_classes.append(class_)

    ta = TypeAdapter(list[ListClassesModelBody])
    response_body = ListClassesResponseModel(classes=ta.validate_python(quried_classes))
    return response_body


def get_class_response(class_id: str) -> GetClassResponseModel:
    class_ = query_class(class_id=class_id)
    if class_ == None:
        raise Exception.not_found

    class_["class_id"] = str(class_["_id"])
    class_["teacher"] = get_teacher_by_id(str(class_["teacher_id"]))
    class_["tags"] = query_list_tags_by_id(class_["tags"])
    class_["registration_ended_date"] = mongo_datetime_to_timestamp(
        class_["registration_ended_date"]
    )
    class_["open_date"] = mongo_datetime_to_timestamp(class_["open_date"])
    class_["class_ended_date"] = mongo_datetime_to_timestamp(class_["class_ended_date"])
    for i in range(len(class_["schedules"])):
        # print(class_["schedules"][i]["start"])
        class_["schedules"][i]["start"] = mongo_datetime_to_timestamp(
            class_["schedules"][i]["start"]
        )
        class_["schedules"][i]["end"] = mongo_datetime_to_timestamp(
            class_["schedules"][i]["end"]
        )

    return GetClassResponseModel(**class_)


def post_class_request(request: PostClassRequestModel) -> PostClassResponseModel:
    class_id = create_class(request)
    return PostClassResponseModel(class_id=class_id)


def patch_class_request(class_id: str, request: PatchClassRequestModel):
    edit_class(class_id, request)
    return GenericOKResponse


# THREADS
def list_threads_response(class_id: str, skip: int, limit: int):
    thread_cursor = query_list_threads(class_id=class_id, skip=skip, limit=limit)
    threads = []
    for thread in thread_cursor:
        thread["thread_id"] = str(thread["_id"])
        thread["teacher"] = get_teacher_by_id(str(thread["teacher_id"]))
        thread["last_edit"] = mongo_datetime_to_timestamp(thread["last_edit"])
        threads.append(thread)

    ta = TypeAdapter(list[ListThreadModelBody])
    return ListThreadResponseModel(threads=ta.validate_python(threads))


def post_thread_request(class_id: str, thread_body: PostThreadRequestModel):
    thread_id = create_thread(class_id=class_id, thread_body=thread_body)
    return PostThreadResponseModel(thread_id=thread_id)


def get_thread_response(class_id: str, thread_id: str):
    quried_thread = query_thread(class_id=class_id, thread_id=thread_id)
    quried_thread["teacher"] = get_teacher_by_id(str(quried_thread["teacher_id"]))
    quried_thread["last_edit"] = mongo_datetime_to_timestamp(quried_thread["last_edit"])# make timestamp timezone aware that db return utc time
    return GetThreadResponseModel(**quried_thread)


def patch_thread_request(
    class_id: str, thread_id: str, thread_body: PatchThreadRequestModel
):
    edit_thread(class_id=class_id, thread_id=thread_id, thread_body=thread_body)
    return GenericOKResponse
