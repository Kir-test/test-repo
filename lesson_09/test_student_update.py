from sqlalchemy import text

from db import engine


def test_update_student():
    user_id = 99999

    with engine.connect() as connection:
        connection.execute(
            text(
                """
                INSERT INTO student
                (user_id, level, education_form, subject_id)
                VALUES
                (:user_id, 'Beginner', 'personal', 1)
                """
            ),
            {"user_id": user_id},
        )
        connection.commit()

        connection.execute(
            text(
                """
                UPDATE student
                SET level = 'Advanced'
                WHERE user_id = :user_id
                """
            ),
            {"user_id": user_id},
        )
        connection.commit()

        result = connection.execute(
            text(
                """
                SELECT level
                FROM student
                WHERE user_id = :user_id
                """
            ),
            {"user_id": user_id},
        )

        student_level = result.fetchone()

        assert student_level[0] == "Advanced"

        connection.execute(
            text(
                """
                DELETE FROM student
                WHERE user_id = :user_id
                """
            ),
            {"user_id": user_id},
        )
        connection.commit()
