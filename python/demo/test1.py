
import abc
import sys

# 抽象类
class Test1(metaclass=abc.ABCMeta):
	def __init__(self, p1):
		self.p1 = p1

	@abc.abstractmethod
	def read(self):
		print('base abs method:', self.p1)

	def write(self):
		print("normal method")

class B(Test1):
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
	def read(self):
		print('overrite read', self.p1)


if __name__ == '__main__':
	print(sys.version)
	print(sys.argv[0])
	p1 = '中国'#sys.argv[1]
	p2 = '人民'#sys.argv[2]
	bb = B(p1, p2)
	bb.read()
	print('%s'%'xx')

