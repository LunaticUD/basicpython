class Stu(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_store(self):
        print('%s: %s' % (self.name, self.score))

a = Stu('www',89)
a.name()