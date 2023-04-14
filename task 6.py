def edit_distance(s1, s2):
    m, n = len(s1), len(s2)

    # Initialize the DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    # Fill in the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    # Traverse the DP table to get the list of operations
    i, j = m, n
    operations = []
    while i > 0 or j > 0:
        if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(('delete', s1[i - 1]))
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            operations.append(('insert', s2[j - 1]))
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(('substitute', s1[i - 1], s2[j - 1]))
            i -= 1
            j -= 1
        else:
            i -= 1
            j -= 1

    operations.reverse()
    num_operations = len(operations)

    return num_operations, operations

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
num_operations, operations = edit_distance(s1, s2)
print(f"{num_operations} operations")
for operation in operations:
    if operation[0] == 'delete':
      print(f"Delete {operation[1]}")
    elif operation[0] == 'insert':
        print(f"Insert {operation[1]}")
    elif operation[0] == 'substitute':
        print(f"Substitute {operation[1]} with {operation[2]}")