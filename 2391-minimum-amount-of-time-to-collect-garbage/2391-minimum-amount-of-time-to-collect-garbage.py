class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        cglass, cpaper, cmetal = 0, 0, 0
        mglass, mpaper, mmetal = -1, -1, -1
        N = len(garbage)
        for i, house in enumerate(garbage):
            if 'G' in house:
                mglass = i
                cglass += house.count('G')
            if 'P' in house:
                mpaper = i
                cpaper += house.count('P')
            if 'M' in house:
                mmetal = i
                cmetal += house.count('M')
        
        # print(cglass, cpaper, cmetal)
        # print(mglass, mpaper, mmetal)
        
        #prefix
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        
        res += cglass + cpaper + cmetal
        
        if mglass > 0:
            res += travel[mglass - 1]
        if mmetal > 0:
            res += travel[mmetal - 1]
        if mpaper > 0:
            res += travel[mpaper - 1]
        
        return res
            
                
            
            