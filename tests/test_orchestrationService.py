import os
import unittest
from unittest.mock import patch
import requests
import OrchestrateService 

class TestOrchestrationService(unittest.TestCase):
    
    @patch('requests.get')
    def test_get_userInfo(self, mock_get):
        # Setup mock response for the User Service
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "user_id": "123",
            "first_name": "Andy",
            "last_name": "Bell",
            "email": "andybell@gmail.com"
        }

        service = OrchestrationService(
            URL_USER_SERV="http://localhost:5000",
            URL_SUB_SERV="http://localhost:5002",
            URL_PREF_SERV="http://localhost:5004"
        )

        user_details = service.get_userInfo("12345")
        
        # Assert the mock response is used
        mock_get.assert_called_once_with("http://localhost:5000/user/123")
        self.assertEqual(user_details['user_id'], "123")
        self.assertEqual(user_details['first_name'], "John")

    @patch('requests.get')
    def test_get_userSubInfo(self, mock_get):
        # Setup mock response for Subscription Service
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "paymentMethod": "Visa",
            "status": "active"
        }

        service = OrchestrationService(
            URL_USER_SERV="http://localhost:5000",
            URL_SUB_SERV="http://localhost:5002",
            URL_PREF_SERV="http://localhost:5004"
        )

        subscription_details = service.get_userSubInfo("123")
        
        # Assert the mock response is used
        mock_get.assert_called_once_with("http://localhost:5002/subscription/123")
        self.assertEqual(subscription_details['paymentMethod'], "Visa")
        self.assertEqual(subscription_details['status'], "active")

    @patch('requests.get')
    def test_get_userPrefInfo(self, mock_get):
        # Setup mock response for Preference Service
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "can_email": "false",
            "notify_enabled": 'true'
        }

        service = OrchestrationService(
            URL_USER_SERV="http://localhost:5000",
            URL_SUB_SERV="http://localhost:5002",
            URL_PREF_SERV="http://localhost:5004"
        )

        preferences = service.get_userPrefInfo("123")
        
        # Assert the mock response is used
        mock_get.assert_called_once_with("http://localhost:5004/preference/123")
        self.assertEqual(preferences['can_email'], "false")
        self.assertTrue(preferences['notify_enabled'])

    @patch('requests.get')
    def test_subscription(self, mock_get):
        # Setup all mock responses for the orchestration service
        mock_get.side_effect = [
            # Mock response for get_user_details
            unittest.mock.Mock(status_code=200, json=lambda: {
                "user_id": "123",
                "first_name": "Andy",
                "last_name": "Bell",
                "email": "andybell@gmail.com"
            }),
            # Mock response for get_subscription_details
            unittest.mock.Mock(status_code=200, json=lambda: {
                "paymentMethod": "Visa",
                "status": "active"
            })
           
        ]

        service = OrchestrationService(
            URL_USER_SERV="http://localhost:5000",
            URL_SUB_SERV="http://localhost:5002",
            URL_PREF_SERV="http://localhost:5004"
        )

        user_profile = service.get_user_profile("123")
        
        # Assert that all the mock methods were called
        self.assertEqual(user_profile["user"]["first_name"], "John")
        self.assertEqual(user_profile["subscription"]["status"], "active")
       
        # Check that the requests were made to the correct URLs
        self.assertEqual(mock_get.call_count, 3)
        mock_get.assert_any_call("http://localhost:5000/users/123")
        mock_get.assert_any_call("http://localhost:5001/subscriptions/123")
       
    @patch('requests.get')
    def test_details(self, mock_get):
        # Simulate a failure in one of the services (e.g., subscription service)
        mock_get.side_effect = [
            # Mock response for get_user_details
            unittest.mock.Mock(status_code=200, json=lambda: {
                "user_id": "123",
                "first_name": "Andy",
                "last_name": "Bell",
                "email": "andybell@gmail.com"
            }),
            # Mock response for get_subscription_details (fail)
            unittest.mock.Mock(status_code=500, json=lambda: {}),
            # Mock response for get_user_preferences
            unittest.mock.Mock(status_code=200, json=lambda: {
                 "paymentMethod": "Visa",
                "status": "active"
            }),
            # Mock response for get_user_preferences
            unittest.mock.Mock(status_code=200, json=lambda: {
                "can_email": "false",
                "notify_enabled": 'true'
            })
        ]

        service = OrchestrationService(
            URL_USER_SERV="http://localhost:5000",
            URL_SUB_SERV="http://localhost:5002",
            URL_PREF_SERV="http://localhost:5004"
        )

        # Test that an exception is raised when one service fails
        with self.assertRaises(Exception):
            service.get_user_profile("123")


if __name__ == '__main__':
    unittest.main()
