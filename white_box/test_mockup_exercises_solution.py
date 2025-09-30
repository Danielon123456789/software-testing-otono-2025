# -*- coding: utf-8 -*-
"""
Unit tests for fetch_data_from_api function from mockup_exercises module.
"""

import unittest
from unittest.mock import patch

# pylint: disable=import-error
import requests

from white_box.mockup_exercises import fetch_data_from_api


class TestData(unittest.TestCase):
    """Unit tests for fetch_data_from_api covering success and error cases."""

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """Caso exitoso: requests.get devuelve un objeto cuyo .json() devuelve datos."""
        mock_get.return_value.json.return_value = {"key": "value"}

        result = fetch_data_from_api("https://api.example.com/data")

        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_json_error(self, mock_get):
        """Si response.json() lanza ValueError (JSON inválido)."""
        mock_get.return_value.json.side_effect = ValueError("Invalid JSON")

        with self.assertRaises(ValueError):
            fetch_data_from_api("https://api.example.com/bad-json")

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_request_exception(self, mock_get):
        """Si requests.get lanza una excepción de requests (ej. RequestException)."""
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        with self.assertRaises(requests.exceptions.RequestException):
            fetch_data_from_api("https://api.example.com/network-fail")

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_timeout(self, mock_get):
        """Si requests.get lanza Timeout, se propaga esa excepción."""
        mock_get.side_effect = requests.exceptions.Timeout("Timed out")

        with self.assertRaises(requests.exceptions.Timeout):
            fetch_data_from_api("https://api.example.com/timeout")


if __name__ == "__main__":
    unittest.main()
