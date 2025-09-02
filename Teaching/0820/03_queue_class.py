class Queue:
    def __init__(self, capacity=10):
        # 큐의 최대 용량 설정
        self.capacity = capacity 
        # 큐를 저장할 리스트 초기화 
        self.items = [None] * capacity
        # 큐의 맨 앞 요소 인덱스 (초기 값 -1)
        self.front = -1 
        # 큐의 맨 뒤 요소 인덱스 (초기 값 -1)
        self.rear = -1 

    def is_empty(self):
        # front와 rear가 같으면 큐가 비어 있음 
        return self.front == self.rear 

    def is_full(self):
        # rear가 큐의 최대 인덱스(capacity-1)에 도달하면 큐가 가득참
        return self.rear == self.capacity
    
    def enqueue(self, item):
        # 삽입하기 전에 가득 찼는지 확인 
        if self.is_full():
            raise IndexError('큐가 가득찼습니다.')
        self.rear += 1
        self.items[self.rear] = item

    def dequeue(self):
        # 삭제 전에 큐가 비었는지를 확인
        if self.is_empty():
            raise IndexError('큐가 비었습니다.')
        # front 인덱스가 1증가 
        self.front += 1
        # front가 위치한 항목을 우선 변수에 담아두기 
        item = self.items[self.front]
        # 해당 위치를 None으로 변경(제거)
        self.items[self.front] = None
        return item #front가 이동한 위치에 있던 기존 데이터 반환 
    
    def peek(self):
        if self.is_empty():
            raise IndexError('큐가 비었습니다.')
        return self.items[self.front + 1]

    def get_size(self):
        # 현재 큐에 있는 항목의 개수 계산 
        return self.rear - self.front 


# --- 기본 동작 예시 코드 ---
print("--- 1. 기본 동작 확인 ---")
queue = Queue(5)  # 용량이 5인 큐 생성

# 1. Enqueue (데이터 삽입)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(f"큐의 현재 크기: {queue.get_size()}")  # 3
print(f"큐의 맨 앞 데이터 확인(peek): {queue.peek()}")  # 10
print(f"큐 내부 리스트 상태: {queue.items}\n")  # [10, 20, 30, None, None]

# 2. Dequeue (데이터 추출)
# 가장 먼저 넣은 10이 가장 먼저 나옴 (FIFO)
print(f"Dequeue: {queue.dequeue()}")  # 10
print(f"큐의 현재 크기: {queue.get_size()}")  # 2
print(f"큐의 맨 앞 데이터 확인(peek): {queue.peek()}")  # 20
print(f"큐 내부 리스트 상태: {queue.items}")  # [None, 20, 30, None, None]
