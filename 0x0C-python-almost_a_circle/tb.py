#!/usr/bin/python3
"""test module for base class"""

from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Test class for base class"""
    def test_id(self):
        """verify if proper id is set when no id value
        is passed to the constructor for 100 objects
        """
        # verify id None 
        for i in range(1,100):
            new_base = Base()
            self.assertEqual(new_base.id,i)

        # verify id with value passed in constructor
        for i in range(1,100):
            new_base = Base(i)
            self.assertEqual(new_base.id,i)
        
        # verify id with mix
        b1 = Base(1)
        self.assertEqual(b1.id,1)
        b2 = Base()
        self.assertEqual(b2.id,100)
        b2 = Base()
        self.assertEqual(b2.id,101)
        
        #verify if two objects can have same id
        b1 = Base()
        self.assertEqual(b1.id,102)
        b2 = Base(102)
        self.assertEqual(b2.id,102)
        self.assertEqual(b1.id,b2.id)
    

    def test_to_json_string(self):
        """testing the method to json string"""
        b = Base()
        self.assertEqual(b.to_json_string([]), "[]")
        self.assertEqual(b.to_json_string(None), "[]")
        self.assertEqual(b.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')
        self.assertIsInstance(b.to_json_string([{'id': 32}]), str)
        
        
    def test_from_json_string(self):
        """testing from json string method"""
        b = Base(200)
        self.assertEqual(b.from_json_string("[]"),[])
        self.assertEqual(b.from_json_string(None),[])
        self.assertEqual(b.from_json_string('[{ "id": 89 }]'), [{ "id": 89 }])
        self.assertIsInstance(b.from_json_string('[{ "id": 89 }]'), list)
        
    