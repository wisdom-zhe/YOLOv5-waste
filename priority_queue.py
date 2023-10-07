import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    # 入队元素
    # 第一个参数：添加进的目标序列
    # 第二个参数：将一个元组作为整体添加进序列，目的是为了方便比较
    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        if len(self.queue) > 0:
            # 返回按照-priority 和 index 排序后的第一个元素(是一个元组)的最后一个元素(item)
            return heapq.heappop(self.queue)
        else:
            return None

    def clear(self):
        self.queue = []
        self.index = 0


"""
q = PriorityQueue()
q.push("bar", 2)
q.push("foo", 1)
q.push("gork", 3)
q.push("new", 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

gork  # 优先级最高
bar   # 优先级第二
foo   # 优先级与new相同，比较index，因为先加入，index比new小，所以排在前面
new

"""