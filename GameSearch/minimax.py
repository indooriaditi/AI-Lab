
import math

def minimax (cDepth, nIndex,
			maxTurn, points,
			tDepth):

	# base case : tDepth reached
	if (cDepth == tDepth):
		return points[nIndex]
	
	if (maxTurn):
		return max(minimax(cDepth + 1, nIndex * 2,
					False, points, tDepth),
				minimax(cDepth + 1, nIndex * 2 + 1,
					False, points, tDepth))
	
	else:
		return min(minimax(cDepth + 1, nIndex * 2,
					True, points, tDepth),
				minimax(cDepth + 1, nIndex * 2 + 1,
					True, points, tDepth))
	
points = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(points), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, points, treeDepth))

