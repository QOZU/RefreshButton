# test_refreshbutton.py
"""
Tests for RefreshButton module.
"""

import unittest
from refreshbutton import RefreshButton

class TestRefreshButton(unittest.TestCase):
    """Test cases for RefreshButton class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RefreshButton()
        self.assertIsInstance(instance, RefreshButton)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RefreshButton()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
