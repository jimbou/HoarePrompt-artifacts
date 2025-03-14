def simulate_game(n, k, PB, PS, p, a):
    def calculate_score(start_pos):
        score = 0
        current_pos = start_pos
        steps = 0
        
        # To handle large k and cycles
        visited = {}
        cycle_start = -1
        while steps < k:
            if current_pos in visited:
                cycle_start = visited[current_pos]
                break
            visited[current_pos] = steps
            score += a[current_pos - 1]
            steps += 1
            if steps >= k:
                return score
            current_pos = p[current_pos - 1]
        
        # If a cycle is detected
        if cycle_start != -1:
            cycle_length = steps - cycle_start
            cycle_score = 0
            cycle_pos = current_pos
            for _ in range(cycle_length):
                cycle_score += a[cycle_pos - 1]
                cycle_pos = p[cycle_pos - 1]
 
            remaining_steps = k - steps
            full_cycles = remaining_steps // cycle_length
            remainder_steps = remaining_steps % cycle_length
 
            score += full_cycles * cycle_score
 
            for _ in range(remainder_steps):
                score += a[current_pos - 1]
                current_pos = p[current_pos - 1]
 
        return score
 
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    
    if bodya_score > sasha_score:
        return "Bodya"
    elif sasha_score > bodya_score:
        return "Sasha"
    else:
        return "Draw"
 
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        PB = int(data[index + 2])
        PS = int(data[index + 3])
        index += 4
        
        p = list(map(int, data[index:index + n]))
        index += n
        
        a = list(map(int, data[index:index + n]))
        index += n
        
        result = simulate_game(n, k, PB, PS, p, a)
        results.append(result)
    
    for result in results:
        print(result)
 
if __name__ == "__main__":
    main()