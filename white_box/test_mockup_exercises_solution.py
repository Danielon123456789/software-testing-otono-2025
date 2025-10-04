# -*- coding: utf-8 -*-
"""
Unit tests for mock up testing examples.
"""
import subprocess
import unittest
from unittest.mock import mock_open, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestDataFetcher(unittest.TestCase):
    """
    Tests for fetch_data_from_api
    """

    @patch(
        "white_box.mockup_exercises.requests.get"
    )  # vamos a devovler nuestro propio requests.get
    def test_fetch_data_from_api_success(self, mock_get):
        """Should return JSON when API call succeeds"""
        mock_get.return_value.json.return_value = {
            "key": "value"
        }  # fabricamos nuestra respuesta

        result = fetch_data_from_api("https://api.example.com/data")

        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)
        # probamos que se llamo una vez y con los parametros.


class TestReadFile(unittest.TestCase):
    """
    Tests for read_data_from_file
    """

    # creamos el archivo y el contenido.
    @patch("builtins.open", new_callable=mock_open, read_data="file content")
    def test_read_data_from_file_success(self, mock_file):
        """Should read file content successfully"""
        result = read_data_from_file("test.txt")
        self.assertEqual(result, "file content")  # comprobamos contenidos.
        mock_file.assert_called_once_with("test.txt", encoding="utf-8")

    def test_read_data_from_file_not_found(self):
        """Should raise FileNotFoundError if file does not exist"""
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("not_exist.txt")


class TestExecuteCommand(unittest.TestCase):
    """
    Tests for execute_command
    """

    # creamos el mock_run
    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """Should return stdout when command executes successfully"""
        mock_run.return_value.stdout = "command output"
        result = execute_command(["echo", "hello"])
        self.assertEqual(result, "command output")  # comparamos la salida
        mock_run.assert_called_once_with(
            ["echo", "hello"], capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_failure(self, mock_run):
        """Should raise CalledProcessError if command fails"""
        mock_run.side_effect = subprocess.CalledProcessError(1, "cmd")

        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["false"])


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Tests for perform_action_based_on_time
    """

    @patch("white_box.mockup_exercises.time.time", return_value=5)
    def test_perform_action_time_less_than_10(self, mock_time):
        """Should return 'Action A' when time < 10"""
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time", return_value=20)
    def test_perform_action_time_greater_than_10(self, mock_time):
        """Should return 'Action B' when time >= 10"""
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()


if __name__ == "__main__":
    unittest.main()
