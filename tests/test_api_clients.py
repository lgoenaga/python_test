import unittest
import requests

from src.api_clients import get_location_info
from unittest.mock import patch

class ApiClientsTest(unittest.TestCase):
  
  @patch('src.api_clients.requests.get')
  def test_get_location_info_expected(self, mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "countryName": "Colombia",
        "cityName": "Medellin",
        "regionName": "Antioquia"
    }
    ip = '181.51.65.190'
    ubicacion = get_location_info(ip)
    self.assertEqual(ubicacion, {
        "country": "Colombia",
        "city": "Medellin",
        "region": "Antioquia"
    })
    
    mock_get.assert_called_once_with(f"https://freeipapi.com/api/json/181.51.65.190")  
    
  @patch('src.api_clients.requests.get')
  def test_get_location_info_side_effect(self, mock_get):
    mock_get.side_effect = [
        requests.exceptions.RequestException('Service unavailable'),
        unittest.mock.Mock(status_code=200, json=lambda: {
            "countryName": "Colombia",
            "cityName": "Medellin",
            "regionName": "Antioquia"
        })    
    ]
    ip = '181.51.65.190'
    
    with self.assertRaises(requests.exceptions.RequestException):
      get_location_info(ip)
      
    ubicacion = get_location_info(ip)
    self.assertEqual(ubicacion, {
        "country": "Colombia",
        "city": "Medellin",
        "region": "Antioquia"
    })
    