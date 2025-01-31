import sys

def calcular_volumes(L, W):
    limite_max = min(L / 2, W / 2)

    limite_min = 0
    

    def volume(x):
        if x <= 0 or x >= L / 2 or x >= W / 2:
            return 0 
        
        return (L - 2 * x) * (W - 2 * x) * x
    
    low, high = limite_min, limite_max
    max_x = 0
    max_volume = 0
    
    for i in range(200):  
        mid = (low + high) / 2
        v1 = volume(mid)
        v2 = volume(mid + 1e-12)
        if v1 < v2:
            low = mid
        else:
            high = mid
        if v1 > max_volume:
            max_volume = v1
            max_x = mid
        if abs(high - low) < 1e-12:  
            max_x = (low + high) / 2
            break


    min_x1 = limite_max

    min_x2 = limite_min
    
    return max_x, min_x1, min_x2

if __name__ == "__main__":
    for line in sys.stdin:
        try:
            L, W = map(float, line.split())
            max_x, min_x1,  min_x2 = calcular_volumes(L, W)
            print(f"{max_x:.3f} {min_x2:.3f} {min_x1:.3f}")
        except ValueError:
            break
