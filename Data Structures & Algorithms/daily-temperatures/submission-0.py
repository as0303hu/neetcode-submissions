class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result =[0]*len(temperatures)
        m_s =[]

        for i in range(len(temperatures)):
            if len(m_s) and temperatures[m_s[-1]]<temperatures[i]:
                while len(m_s) and temperatures[m_s[-1]]<temperatures[i]:
                    prev_index = m_s.pop()
                    result[prev_index] = i - prev_index
                m_s.append(i)
                   
            else:
                m_s.append(i)
        return result

        