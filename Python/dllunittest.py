from doublylinkedlist import *
import unittest

class TestMyFunctions(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMyFunctions, self).__init__(*args, **kwargs)
        
    def test_insert(self):
	dll = linkedList()
	dll.insert(7)
	dll.insert(4)
	dll.insert(8)
	dll.insert(2)    
	self.assertEqual(dll.displayNodes().split(), ['1:2', '2:8', '3:4', '4:7'])
    
    def test_size(self):
	dll = linkedList()
	self.assertEqual(dll.size(), 0)
        dll.insert(1)
	dll.insert(2)
	dll.insert(3)
	dll.insert(4)
        dll.insert(5)
	dll.insert(6)   
	self.assertEqual(dll.size(), 6)

    def test_exists(self):
        dll = linkedList()
	dll.insert(7)
	dll.insert(4)
	dll.insert(8)
	dll.insert(2)
	self.assertTrue(dll.exists(7))
	self.assertTrue(dll.exists(4))
	self.assertTrue(dll.exists(8))
	self.assertTrue(dll.exists(2))
	self.assertFalse(dll.exists(-1))
	self.assertFalse(dll.exists("abcd"))
	
    def test_remove(self):
	dll = linkedList()
	dll.insert(7)
	dll.insert(4)
	dll.insert(8)
	dll.insert(2)	
        dll.delete(8)
	self.assertEqual(dll.displayNodes().split(), ['1:2', '2:4', '3:7'])
	dll.delete(7)
	self.assertEqual(dll.displayNodes().split(), ['1:2', '2:4'])
	dll.delete(2)
	self.assertEqual(dll.displayNodes().split(), ['1:4'])
	dll.delete(4)
        self.assertEqual(dll.displayNodes().split(), [])
	#List empty - Nothing to delete        
	dll.delete(12)
        self.assertEqual(dll.displayNodes().split(), [])
       
if __name__ == "__main__":
    unittest.main(exit=False)

