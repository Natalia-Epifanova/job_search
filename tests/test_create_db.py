from unittest.mock import MagicMock, patch

from src.create_db import CreateDB


@patch("src.create_db.psycopg2.connect")
def test_create_database(mock_connect):
    """Тест на успешное создание базы данных"""
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    db = CreateDB(database_name="test_db", params={"user": "user", "password": "password"})
    db.create_database()
    mock_connect.assert_called_with(dbname="postgres", user="user", password="password")
    mock_conn.autocommit = True
    mock_conn.cursor.assert_called_once()
    mock_conn.close.assert_called_once()


@patch("src.create_db.CreateDB._execute_query")
def test_create_tables_in_the_database(mock_execute_query):
    """Тест на успешное создание таблиц в базе данных"""
    db = CreateDB(database_name="test_db", params={})
    db.create_tables_in_the_database()

    mock_execute_query.assert_called_once()
