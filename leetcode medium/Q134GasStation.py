class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        # Immediate check to see if a complete circuit is possible
        if sum(gas) < sum(cost):
            return -1  # Not enough gas to travel around the circuit
        
        total = 0  # Net gas balance after visiting each station
        start_index = 0  # Potential starting station index
        
        # Traverse through each gas station to find the starting point
        for i in range(len(gas)):
            total += gas[i] - cost[i]  # Update net balance with gas gain or loss
            
            # If net balance is negative, set next station as new start point
            if total < 0:
                total = 0  # Reset net balance
                start_index = i + 1  # Update start index to the next station
        
        # If loop completes, start_index is the correct starting point
        return start_index
