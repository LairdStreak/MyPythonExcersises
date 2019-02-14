#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('.')
from python_Stack_and_Queues import stack_queue as sq

class StackQueueTest(unittest.TestCase):
    def test_queue_size(self):
        test_queue = sq.Queue()
        test_queue.enqueue('a')
        test_queue.enqueue('b')
        self.assertEqual(test_queue.size(), 2)

    def test_queue_deque(self):
        test_queue = sq.Queue()
        test_queue.enqueue('a')
        test_queue.enqueue('b')
        result = str(test_queue.dequeue())
        self.assertEqual(result,'a')

    def test_queue_queue_correct_size(self):
        test_queue = sq.Queue()
        test_queue.enqueue('a')
        lst = test_queue.queue
        self.assertEqual(lst.__len__() ,1)

    def test_stack_size(self):
        test_stack = sq.Stack()
        test_stack.push('a')
        test_stack.push('b')
        self.assertEqual(test_stack.size(), 2)  

    def test_stack_pop(self):
        test_stack = sq.Stack()
        test_stack.push('a')
        test_stack.push('b')
        result = str(test_stack.pop())
        self.assertEqual(result, 'b')      

if __name__ == '__main__':
    unittest.main()        