from singlylinkedlist import *
import unittest

class TestMyFunctions(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMyFunctions, self).__init__(*args, **kwargs)
        
    def test_insert(self):
	sll = linkedList()
	sll.insert(7)
	sll.insert(4)
	sll.insert(8)
	sll.insert(2)    
	self.assertEqual(sll.displayNodes().split(), ['1:2', '2:8', '3:4', '4:7'])
    
    def test_size(self):
	sll = linkedList()
	self.assertEqual(sll.size(), 0)
        sll.insert(1)
	sll.insert(2)
	sll.insert(3)
	sll.insert(4)
        sll.insert(5)
	sll.insert(6)   
	self.assertEqual(sll.size(), 6)

    def test_exists(self):
        sll = linkedList()
	sll.insert(7)
	sll.insert(4)
	sll.insert(8)
	sll.insert(2)
	self.assertTrue(sll.exists(7))
	self.assertTrue(sll.exists(4))
	self.assertTrue(sll.exists(8))
	self.assertTrue(sll.exists(2))
	self.assertFalse(sll.exists(-1))
	self.assertFalse(sll.exists("abcd"))
	
    def test_remove(self):
	sll = linkedList()
	sll.insert(7)
	sll.insert(4)
	sll.insert(8)
	sll.insert(2)	
        sll.delete(8)
	self.assertEqual(sll.displayNodes().split(), ['1:2', '2:4', '3:7'])
	sll.delete(7)
	self.assertEqual(sll.displayNodes().split(), ['1:2', '2:4'])
	sll.delete(2)
	self.assertEqual(sll.displayNodes().split(), ['1:4'])
	sll.delete(4)
        self.assertEqual(sll.displayNodes().split(), [])
	#Nothing to delete        
	sll.delete(12)
        self.assertEqual(sll.displayNodes().split(), [])
       
if __name__ == "__main__":
    unittest.main(exit=False)

