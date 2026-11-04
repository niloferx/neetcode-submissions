class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        res = len(students)
        q = deque(students)

        for sandwich in sandwiches:
            cnt = 0
            while q and cnt < len(q) and q[0]!= sandwich:
                q.append(q.popleft())
                cnt += 1
            
            if q[0] == sandwich:
                q.popleft()
                res-=1
            else:
                break
        
        return res

        """
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s]-=1
            else:
                break

        return res
        """
