import os
import sys

import mysql.connector

sys.path.append("..")
import csv
import json
import logging

import pandas
from sql_database import SQL_database

from server.node import Node
from server.tree import Tree


class SQL_init:

    """A class that initializes the database"""

    # Static var
    data_base_name = "db_budget_system"

    @staticmethod
    def connect_database():
        db = mysql.connector.connect(
            host="localhost",
            user=os.environ.get("user_budget_system"),
            password=os.environ.get("system_budget_password"),
            database="db_budget_system",
        )
        return db

    @staticmethod
    def create_database(cursor, database_name: str) -> None:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(
                database_name
            )
        )  # db_budget_system

    @staticmethod
    def create_table(mycursor, table_name: str, table_columns: str) -> None:
        mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({table_columns})")

    @staticmethod
    def delete_table(mycursor, table_name: str) -> None:
        mycursor.execute(f"DROP TABLE IF EXISTS {table_name} ")

    @staticmethod
    def clean_database(cursor) -> None:
        # Clean database
        SQL_init.delete_table(cursor, "CURRENT_BUDGET")
        SQL_init.delete_table(cursor, "USERS_VOTES")
        SQL_init.delete_table(cursor, "USERS")
        SQL_init.delete_table(cursor, "INFORMATION")

    @staticmethod
    def insert_to_current_budget_table(mycursor, node: Node) -> None:
        mycursor.execute(
            """INSERT INTO CURRENT_BUDGET (node_id, name, description, parent_id, budget_amount)
                       VALUES (%s, %s, %s, %s, %s)""",
            (
                node.get_id(),
                node.get_name(),
                node.get_description(),
                node.get_parent_id(),
                node.get_allocated_budget_amount(),
            ),
        )
        for child in node.get_children():
            SQL_init.insert_to_current_budget_table(mycursor, child)

    @staticmethod
    def load_and_insert_to_current_budget_table(cursor, db) -> None:
        path = "../../dataset/"
        df = pandas.read_csv(path + "national_budget.csv", encoding="utf-8")
        # remove double quotes from relevant columns
        cols_to_clean = [
            "שם רמה 1",
            "שם רמה 2",
            "שם סעיף",
            "שם תחום",
            "שם תכנית",
            "שם תקנה",
        ]
        df[cols_to_clean] = df[cols_to_clean].apply(lambda x: x.str.replace('"', ""))
        num_rows = len(df)
        for i in range(1, num_rows):
            row = df.iloc[i, :]
            cursor.execute(
                """INSERT INTO CURRENT_BUDGET (kod_one, name_one,
                            kod_two, name_two, kod_three, name_three, kod_four, name_four, kod_five, name_five,
                            kod_six, name_six, takziv)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    int(row[0]),
                    row[1],
                    int(row[2]),
                    row[3],
                    int(row[4]),
                    row[5],
                    int(row[6]),
                    row[7],
                    int(row[8]),
                    row[9],
                    int(row[10]),
                    row[11],
                    str(row[12]),
                ),
            )
        db.commit()

    @staticmethod
    def load_information_to_information_table(cursor, db) -> None:
        path = "../../dataset/"
        df = pandas.read_csv(path + "information.csv", encoding="utf-8")
        num_rows = len(df)
        for i in range(0, num_rows):
            row = df.iloc[i, :]
            cursor.execute(
                """INSERT INTO INFORMATION (name, details)
                        VALUES (%s, %s)""",
                (row[0], row[1]),
            )

        db.commit()

    @staticmethod
    def build_tree_from_csv() -> Tree:
        path = "../../dataset/"
        df = pandas.read_csv(path + "national_budget.csv", encoding="utf-8")

        root = Node(
            id=0, name="root", description="I am root", parent=None, budget_amount=0
        )
        tree = Tree(root)
        num_rows = len(df)
        for i in range(1, num_rows):
            row = df.iloc[i, :]
            row_list = row.tolist()
            node_id = int(row_list[0])
            node_name = row_list[1]
            if not tree.node_exists(int(node_id), node_name):
                node = Node(id=int(node_id), name=node_name, parent=0)
                tree.add_node_by_id_and_name(0, "root", node)

        for i in range(1, num_rows):
            row = df.iloc[i, :]
            row_list = row.tolist()
            node_id = int(row_list[2])
            node_name = row_list[3]
            if not tree.node_exists(int(node_id), node_name):
                node = Node(id=int(node_id), name=node_name, parent=int(row_list[0]))
                parent_id = int(row_list[0])
                parent_name = row_list[1]
                tree.add_node_by_id_and_name(parent_id, parent_name, node)

        for i in range(1, num_rows):
            row = df.iloc[i, :]
            row_list = row.tolist()
            node_id = int(row_list[4])
            node_name = row_list[5]
            if not tree.node_exists(int(node_id), node_name):
                node = Node(id=int(node_id), name=node_name, parent=int(row_list[2]))
                parent_id = int(row_list[2])
                parent_name = row_list[3]
                tree.add_node_by_id_and_name(parent_id, parent_name, node)

        for i in range(1, num_rows):
            row = df.iloc[i, :]
            row_list = row.tolist()
            node_id = int(row_list[6])
            node_name = row_list[7]
            if not tree.node_exists(int(node_id), node_name):
                node = Node(id=int(node_id), name=node_name, parent=int(row_list[4]))
                parent_id = int(row_list[4])
                parent_name = row_list[5]
                tree.add_node_by_id_and_name(parent_id, parent_name, node)

        for i in range(1, num_rows):
            row = df.iloc[i, :]
            row_list = row.tolist()
            node_id = int(row_list[8])
            node_name = row_list[9]
            if not tree.node_exists(int(node_id), node_name):
                node = Node(id=int(node_id), name=node_name, parent=int(row_list[6]))
                parent_id = int(row_list[6])
                parent_name = row_list[7]
                tree.add_node_by_id_and_name(parent_id, parent_name, node)

        for i in range(1, num_rows):
            row = df.iloc[i, :]
            row_list = row.tolist()
            node_id = int(row_list[10])
            node_name = row_list[11]
            if not tree.node_exists(int(node_id), node_name):
                node = Node(
                    id=int(node_id),
                    name=node_name,
                    parent=int(row_list[8]),
                    budget_amount=float(row_list[12]),
                )
                parent_id = int(row_list[8])
                parent_name = row_list[9]
                tree.add_node_by_id_and_name(parent_id, parent_name, node)

        return tree

    @staticmethod
    def write_tree_to_csv(tree, filename):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["node_id", "name", "description", "parent_id", "budget_amount"]
            )
            SQL_init.write_node_to_csv(tree.get_root(), writer)

    @staticmethod
    def write_node_to_csv(node, writer):
        writer.writerow(
            [
                node.get_id(),
                node.get_name(),
                node.get_description(),
                node.get_parent_id(),
                node.get_allocated_budget_amount(),
            ]
        )
        for child in node.get_children():
            SQL_init.write_node_to_csv(child, writer)


if __name__ == "__main__":
    # Connect server
    db = SQL_init.connect_database()
    cursor = db.cursor()

    # Create and build database
    SQL_init.create_database(cursor, SQL_init.data_base_name)
    SQL_init.create_table(
        cursor,
        "CURRENT_BUDGET",
        """kod_one INT, name_one VARCHAR(1000),
                            kod_two INT, name_two VARCHAR(1000), kod_three INT, name_three VARCHAR(1000),
                            kod_four INT, name_four VARCHAR(1000), kod_five INT, name_five VARCHAR(1000),
                            kod_six INT, name_six VARCHAR(1000), takziv VARCHAR(255)""",
    )
    SQL_init.create_table(
        cursor,
        "USERS",
        """user_id INT PRIMARY KEY, first_name VARCHAR(255),
                            last_name VARCHAR(255), birth_date DATE, mail VARCHAR(255), password VARCHAR(255),
                            gender VARCHAR(255), is_admin VARCHAR(255), allowed_to_vote VARCHAR(255)""",
    )
    SQL_init.create_table(
        cursor, "USERS_VOTES", "user_id VARCHAR(255), vote TEXT(4294967295)"
    )
    # SQL_init.create_table(cursor, 'USERS_VOTES', 'id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, level_1 VARCHAR(255), level_2 VARCHAR(255), section VARCHAR(255), domain VARCHAR(255), program VARCHAR(255), regulation VARCHAR(255), total INT')
    SQL_init.create_table(
        cursor, "INFORMATION", "name VARCHAR(50), details VARCHAR(1000)"
    )

    # Load datasets
    SQL_init.load_information_to_information_table(cursor, db)
    SQL_init.load_and_insert_to_current_budget_table(cursor, db)
    # Clean
    # SQL_init.clean_database(cursor)

    #  ###### App (server) example: ###############
    # sql_handler = SQL_database(SQL_database.create_config())
    # sql_handler.connect()
    # result = sql_handler.get_user_full_name(123123123)
    # sql_handler.cursor.execute("SELECT * FROM USERS")
    # result = sql_handler.cursor.fetchall()
    # print(result)

    # vote = {
    #                 "id":0,
    #                 "name":"root",
    #                 "description":"I am root",
    #                 "parent":None,
    #                 "allocated_budget_amount":20592073,
    #                 "children":[
    #                     {
    #                         "id":1,
    #                         "name":"Security and public order",
    #                         "description":"I am Security and public order",
    #                         "parent":0,
    #                         "allocated_budget_amount":20592073,
    #                         "children":[
    #                             {
    #                             "id":2,
    #                             "name":"Security",
    #                             "description":"I am Security",
    #                             "parent":1,
    #                             "allocated_budget_amount":20592073,
    #                             "children":[
    #                                 {
    #                                     "id":3,
    #                                     "name":"Ministry of Defense",
    #                                     "description":"I am Ministry of Defense",
    #                                     "parent":2,
    #                                     "allocated_budget_amount":20592073,
    #                                     "children":[
    #                                         {
    #                                         "id":4,
    #                                         "name":"HR",
    #                                         "description":"I am HR",
    #                                         "parent":3,
    #                                         "allocated_budget_amount":12436481,
    #                                         "children":[
    #                                             {
    #                                                 "id":5,
    #                                                 "name":"Current salary of permanent soldiers",
    #                                                 "description":"I am Current salary of permanent soldiers",
    #                                                 "parent":4,
    #                                                 "allocated_budget_amount":11171083,
    #                                                 "children":[

    #                                                 ]
    #                                             },
    #                                             {
    #                                                 "id":6,
    #                                                 "name":"Current salary of Ministry of Defense employees",
    #                                                 "description":"I am Current salary of Ministry of Defense employees",
    #                                                 "parent":4,
    #                                                 "allocated_budget_amount":1265398,
    #                                                 "children":[

    #                                                 ]
    #                                             }
    #                                         ]
    #                                         },
    #                                         {
    #                                         "id":7,
    #                                         "name":"Pensions",
    #                                         "description":"I am Pensions",
    #                                         "parent":3,
    #                                         "allocated_budget_amount":8155592,
    #                                         "children":[
    #                                             {
    #                                                 "id":8,
    #                                                 "name":"Permanent soldiers pensions",
    #                                                 "description":"I am Permanent soldiers pensions",
    #                                                 "parent":7,
    #                                                 "allocated_budget_amount":7780739,
    #                                                 "children":[

    #                                                 ]
    #                                             },
    #                                             {
    #                                                 "id":9,
    #                                                 "name":"Retirement grants for permanent soldiers",
    #                                                 "description":"I am Retirement grants for permanent soldiers",
    #                                                 "parent":7,
    #                                                 "allocated_budget_amount":374853,
    #                                                 "children":[
    #                                                     ]
    #                                                 }
    #                                             ]
    #                                         }
    #                                     ]
    #                                 }
    #                             ]
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }

    # user_id = "99999999"
    # vote_str = json.dumps(vote,ensure_ascii=False)
    # is_saved = sql_handler.store_vote(vote=vote_str, user_id=user_id)
    # if is_saved:
    #     print("saved")
    #     print(" ")

    # result = sql_handler.load_user_votes()
    # print(" ")
    # print(" ")
    # print(" ")
    # query = '''SELECT user_id FROM USERS_VOTES'''
    # sql_handler.cursor.execute(query)
    # res = sql_handler.cursor.fetchall()
    # print(type(res))
    # print(res)

    # d = sql_handler.get_information()

    # tree = sql_handler.build_tree_from_current_budget()
    # tree.print_tree()

    ###### App (server) example:

    # sql_handler = SQL_database(SQL_database.create_config())
    # sql_handler.connect()
    # tree = sql_handler.build_tree_from_current_budget()
    # dictionary = tree.to_dict()
    # from algorithms import _calculate_totals
    # _calculate_totals(dictionary)
    # json_tree = json.dumps(dictionary, ensure_ascii=False)
    # print(json_tree)
    # counter = 0
    # SQL_init.modify_id(dictionary,counter)

    # tree = sql_handler.build_tree_from_current_budget()
    # tree.print_tree()

    # dictionary = tree.to_dict()
    # print(dictionary)
    # json_tree = json.dumps(dictionary,ensure_ascii=False)
    # print(json_tree)