def solve_n_queens(n):
    solutions = []
    cols = set()
    pos_diags = set()  
    neg_diags = set()  
    board = [-1] * n

    def backtrack(r):
        if r == n:
            solutions.append(board.copy())
            return
        for c in range(n):
            if c in cols or (r+c) in pos_diags or (r-c) in neg_diags:
                continue
            cols.add(c)
            pos_diags.add(r+c)
            neg_diags.add(r-c)
            board[r] = c
            backtrack(r+1)
            cols.remove(c)
            pos_diags.remove(r+c)
            neg_diags.remove(r-c)
            board[r] = -1

    backtrack(0)
    return solutions

def print_board(sol):
    n = len(sol)
    for r in range(n):
        row = ['.'] * n
        row[sol[r]] = 'Q'
        print("".join(row))
    print()

def main():
    print("--- N-Queens Problem Solver ---")
    while True:
        input_value = input("Enter the size of the chessboard (N), or 'q' to quit: ")

        if input_value.lower() in ['q', 'quit', 'exit']:
            print("Exiting Solver. Have a nice day!")
            break

        try:
            n = int(input_value)
            if n <= 0:
                print("Error: Please enter a positive number for N.")
                continue
            
            if 0 < n < 4:
                 print(f"No solutions exist for N={n}.")
                 continue

        except ValueError:
            print("Error: Invalid input detected.\n Please enter a whole number.")
            continue
        sols = solve_n_queens(n)
        print(f"Found {len(sols)} solutions for N={n}")
        for i, s in enumerate(sols[:10], 1):
            print(f"Solution {i}: {s}")
            print_board(s)
if __name__ == "__main__":
    main()
