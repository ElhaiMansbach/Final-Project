import sys
import unittest

sys.path.append("../..")
import datetime

from my_sqlite_database import my_sqlite_database

from src.database.data_handler import data_handler
from src.database.sql_database import SQL_database
from src.server.calculator import Calculator


class Test_calculator(unittest.TestCase):
    # ------------------------------------ Set ups --------------------------------------------------

    @classmethod
    def setUpClass(self):
        self.sqlite = my_sqlite_database()
        self.sqlite.connect()
        self.sqlite.execute_query(
            """CREATE TABLE IF NOT EXISTS Users (user_id INTEGER PRIMARY KEY, first_name, last_name, birth_date , mail,
                    password, gender, is_admin, allowed_to_vote)"""
        )

        # self.db_connector = sqlite3.connect("tests.db")
        # self.cursor = self.db_connector.cursor()
        # self.cursor.execute(
        #     """CREATE TABLE IF NOT EXISTS Users (user_id INTEGER PRIMARY KEY, first_name, last_name, birth_date , mail,
        #             password, gender, is_admin, allowed_to_vote)"""
        # )

    @classmethod
    def tearDownClass(self):
        self.sqlite.db.commit()
        self.sqlite.execute_query("DROP TABLE Users")
        self.sqlite.cursor.close()
        self.sqlite.db.close()

    def setUp(self):
        for i in range(0, 100):
            self.sqlite.execute_query(
                f"""INSERT INTO Users (user_id, first_name, last_name, birth_date, mail, password, gender, is_admin,
                    allowed_to_vote) VALUES ({i}, "ofir", "ovadia", "01/01/1990", "ofir_ovadia@example.com",
                    "password123", "male", 0, 1);"""
            )
            # self.cursor.execute(
            #     f"""INSERT INTO Users (user_id, first_name, last_name, birth_date, mail, password, gender, is_admin,
            #         allowed_to_vote) VALUES ({i}, "ofir", "ovadia", "01/01/1990", "ofir_ovadia@example.com",
            #         "password123", "male", 0, 1);"""
            # )

    def tearDown(self):
        self.sqlite.execute_query("DELETE FROM Users")
        # self.cursor.execute("DELETE FROM Users")

    # ----------------------------------- Tests ------------------------------------------

    def test_get_voter_count(self):
        # self.assertEqual(Calculator.get_voter_count(self.db_connector), 0)
        self.assertEqual(Calculator.get_voter_count(self.sqlite), 0)

        self.sqlite.execute_query(
            "UPDATE Users SET allowed_to_vote = 0 WHERE user_id < 50"
        )
        self.assertEqual(Calculator.get_voter_count(self.sqlite), 50)
        # self.cursor.execute("UPDATE Users SET allowed_to_vote = 0 WHERE user_id < 50")
        # self.assertEqual(Calculator.get_voter_count(self.db_connector), 50)

        self.sqlite.execute_query(
            "UPDATE Users SET allowed_to_vote = 0 WHERE user_id = 99"
        )
        self.assertEqual(Calculator.get_voter_count(self.sqlite), 51)
        # self.cursor.execute("UPDATE Users SET allowed_to_vote = 0 WHERE user_id = 99")
        # self.assertEqual(Calculator.get_voter_count(self.db_connector), 51)

    def test_get_voter_count_by_gender(self):
        self.sqlite.execute_query(
            "UPDATE Users SET gender = 'female' WHERE user_id < 50"
        )
        self.assertEqual(
            Calculator.get_voter_count_by_gender(self.sqlite), [0, 0]
        )  # [male,female]
        # self.cursor.execute("UPDATE Users SET gender = 'female' WHERE user_id < 50")
        # self.assertEqual(Calculator.get_voter_count_by_gender(self.db_connector), [0, 0])  # [male,female]

        self.sqlite.execute_query(
            "UPDATE Users SET allowed_to_vote = 0 WHERE user_id < 50"
        )
        self.assertEqual(
            Calculator.get_voter_count_by_gender(self.sqlite), [0, 50]
        )  # [male,female]
        # self.cursor.execute("UPDATE Users SET allowed_to_vote = 0 WHERE user_id < 50")
        # self.assertEqual(Calculator.get_voter_count_by_gender(self.db_connector), [0, 50])  # [male,female]

        self.sqlite.execute_query(
            "UPDATE Users SET allowed_to_vote = 0 WHERE user_id = 99"
        )
        self.assertEqual(
            Calculator.get_voter_count_by_gender(self.sqlite), [1, 50]
        )  # [male,female]
        # self.cursor.execute("UPDATE Users SET allowed_to_vote = 0 WHERE user_id = 99")
        # self.assertEqual(Calculator.get_voter_count_by_gender(self.db_connector), [1, 50])  # [male,female]

    def test_get_voter_count_by_age(self):
        current_time = datetime.datetime.now()
        # [18-25, 26-35, 36-45, 46-55, 56-65, 66+]
        eighteen_years_ago = current_time - datetime.timedelta(days=18 * 365)
        Twentyfive_years_ago = current_time - datetime.timedelta(days=25 * 365)

        Twentysix_years_ago = current_time - datetime.timedelta(days=26 * 365)
        Thirtyfive_years_ago = current_time - datetime.timedelta(days=35 * 365)

        Thirtysix_years_ago = current_time - datetime.timedelta(days=36 * 365)
        fourtyfive_years_ago = current_time - datetime.timedelta(days=45 * 365)

        fourtysix_years_ago = current_time - datetime.timedelta(days=46 * 365)
        fiftyfive_years_ago = current_time - datetime.timedelta(days=55 * 365)

        fiftysix_years_ago = current_time - datetime.timedelta(days=56 * 365)
        sixtyfive_years_ago = current_time - datetime.timedelta(days=65 * 365)

        sixtysix_years_ago = current_time - datetime.timedelta(days=66 * 365)

        self.sqlite.execute_query(
            "UPDATE Users SET birth_date = '"
            + eighteen_years_ago.strftime("%d/%m/%Y")
            + "' WHERE user_id BETWEEN 0 AND 9"
        )

        # self.cursor.execute("UPDATE Users SET birth_date = '"+ eighteen_years_ago.strftime("%d/%m/%Y")
        #                     + "' WHERE user_id BETWEEN 0 AND 9")

        self.sqlite.execute_query(
            "UPDATE Users SET birth_date = '"
            + Twentysix_years_ago.strftime("%d/%m/%Y")
            + "' WHERE user_id BETWEEN 10 AND 24"
        )

        # self.cursor.execute("UPDATE Users SET birth_date = '"+ Twentysix_years_ago.strftime("%d/%m/%Y")
        #                     + "' WHERE user_id BETWEEN 10 AND 24")

        self.sqlite.execute_query(
            "UPDATE Users SET birth_date = '"
            + Thirtysix_years_ago.strftime("%d/%m/%Y")
            + "' WHERE user_id BETWEEN 25 AND 29"
        )

        # self.cursor.execute("UPDATE Users SET birth_date = '"+ Thirtysix_years_ago.strftime("%d/%m/%Y")
        #                     + "' WHERE user_id BETWEEN 25 AND 29")

        self.sqlite.execute_query(
            "UPDATE Users SET birth_date = '"
            + fourtysix_years_ago.strftime("%d/%m/%Y")
            + "' WHERE user_id BETWEEN 30 AND 49"
        )

        # self.cursor.execute("UPDATE Users SET birth_date = '"+ fourtysix_years_ago.strftime("%d/%m/%Y")
        #                     + "' WHERE user_id BETWEEN 30 AND 49")

        self.sqlite.execute_query(
            "UPDATE Users SET birth_date = '"
            + fiftysix_years_ago.strftime("%d/%m/%Y")
            + "' WHERE user_id BETWEEN 50 AND 79"
        )

        # self.cursor.execute("UPDATE Users SET birth_date = '"+ fiftysix_years_ago.strftime("%d/%m/%Y")
        #                     + "' WHERE user_id BETWEEN 50 AND 79")

        self.sqlite.execute_query(
            "UPDATE Users SET birth_date = '"
            + sixtysix_years_ago.strftime("%d/%m/%Y")
            + "' WHERE user_id BETWEEN 80 AND 100"
        )

        # self.cursor.execute("UPDATE Users SET birth_date = '"+ sixtysix_years_ago.strftime("%d/%m/%Y")
        #                     + "' WHERE user_id BETWEEN 80 AND 100")

        self.assertEqual(
            Calculator.get_voter_count_by_age(self.sqlite), [0, 0, 0, 0, 0, 0]
        )
        # self.assertEqual(Calculator.get_voter_count_by_age(self.db_connector), [0, 0, 0, 0, 0, 0])

        self.sqlite.execute_query("UPDATE Users SET allowed_to_vote = 0")
        self.assertEqual(
            Calculator.get_voter_count_by_age(self.sqlite),
            [10, 15, 5, 20, 30, 20],
        )
        # self.cursor.execute("UPDATE Users SET allowed_to_vote = 0")
        # self.assertEqual(Calculator.get_voter_count_by_age(self.db_connector),[10, 15, 5, 20, 30, 20],)


if __name__ == "__main__":
    unittest.main()
