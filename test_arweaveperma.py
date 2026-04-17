# test_arweaveperma.py
"""
Tests for ArweavePerma module.
"""

import unittest
from arweaveperma import ArweavePerma

class TestArweavePerma(unittest.TestCase):
    """Test cases for ArweavePerma class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArweavePerma()
        self.assertIsInstance(instance, ArweavePerma)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArweavePerma()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
