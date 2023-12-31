from starlette.config import Config

# Load environment variables from .env file
config = Config(".env")

# Get a value from .env file
MONGODB_URI = config(
    "MONGODB_URI",
    default="mongodb://root:verystrongrootpassword@localhost:27017/?authMechanism=DEFAULT",
)
MONGODB_DB_NAME = config("MONGODB_DB_NAME", default="LearnHub")

DB_COURSE_COLLECTION = config("DB_COURSE_COLLECTION", default="courses")
DB_CHAPTER_COLLECTION = config("DB_CHAPTER_COLLECTION", default="chapters")
DB_LESSON_COLLECTION = config("DB_LESSON_COLLECTION", default="lessons")
DB_ANNOUNCEMENT_COLLECTION = config(
    "DB_ANNOUNCEMENTS_COLLECTION", default="announcements"
)
DB_COURSE_PROGRESS_COLLECTION = config(
    "DB_COURSE_PROGRESS", default="course_progresses"
)
DB_COURSE_REVIEW_COLLECTION = config("DB_COURSE_COLLECTION", default="course_reviews")

DB_CLASS_COLLECTION = config("DB_CLASS_COLLECTION", default="classes")

DB_TAG_COLLECTION = config("DB_TAG_COLLECTION", default="tags")
DB_TRANSACTION_COLLECTION = config("DB_TRANSACTION_COLLECTION", default="transactions")

DB_USER_COLLECTION = config("DB_USER_COLLECTION", default="users")
DB_ASSIGNMENT_COLLECTION = config("DB_ASSIGNMENT_COLLECTION", default="assignments")
DB_ASSIGNMENT_SUBMISSIONS_COLLECTION = config(
    "DB_ASSIGNMENT_SUBMISSIONS_COLLECTION", default="assignment_submissions"
)
DB_QUIZ_COLLECTION = config("DB_QUIZ_COLLECTION", default="quizzes")
DB_QUIZ_RESULT_COLLECTION = config(
    "DB_QUIZ_RESULT_COLLECTION", default="quizzes_result"
)
DB_THREAD_COLLECTION = config("DB_THREAD_COLLECTION", default="threads")
DB_THREAD_REPLY_COLLECTION = config(
    "DB_THREAD_REPLY_COLLECTION", default="thread_replies"
)
DB_ASSIGNMENT_REPLY_COLLECTION = config(
    "DB_ASSIGNMENT_REPLY_COLLECTION", default="assignment_replies"
)
