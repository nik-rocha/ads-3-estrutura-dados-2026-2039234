# 1

class Stack:
    
    def __init__(self):
        self.pages = []
        self.future_pages = []
        
    def isEmpty(self):
        return self.pages == []
    
    def push(self, item):
        self.pages.append(item)
        
    def pop(self):
        return self.pages.pop()
    
    def peek(self):
        return self.pages[len(self.pages)-1]
    
    def size(self):
        return len(self.pages)
    
    def accessPage(self, page):
        previous = self.pop()
        self.future_pages.append(previous)
        return self.push(page)
    
    def returnPage(self):
        self.pop()
