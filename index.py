import re

def arithmetic_arranger(problems, evaluate=False):

  arranged_problem_list_rows = [[], [], []]
  if evaluate: arranged_problem_list_rows = [[], [], [], []]
  longest_problem = 0
  problem_1 = ""
  problem_2 = ""
  problem_3 = ""

  #Check for max problems
  if len(problems) > 5: return "Error: Too many problems."

  for problem in problems:
      # split problems into 3 sections

      #after this, test for length
      problem_1 = re.search("[^\s]*", problem).group()
      problem_2 = re.search("[^\s]*$", problem).group()
      problem_3 = re.search(" (.*) ", problem).group().strip()

      #check for invalid characters in problems 1 & 2
      if (re.search("[^0-9]", problem_1) is not None): 
        return "Error: Numbers must only contain digits."
      if (re.search("[^0-9]", problem_2) is not None): return "Error: Numbers must only contain digits."

      #check for >4 characters in problems 1 & 2
      if (len(problem_1) > 4) or (len(problem_2) > 4): return "Error: Numbers cannot be more than four digits."

      #check for invalid operands
      if (problem_3 != "+" and problem_3 != "-"): return "Error: Operator must be '+' or '-'."

      #find longest problem
      longest_problem = len(problem_1)
      if (len(problem_2) > len(problem_1)): longest_problem = len(problem_2)

      #add spaces to the first section
      arranged_problem_list_rows[0].append(" "*(longest_problem+2-len(problem_1))+problem_1)

      #add operand and spaces to the second section
      arranged_problem_list_rows[1].append(problem_3+" "*(longest_problem+1-len(problem_2))+problem_2)

      #add barrier
      arranged_problem_list_rows[2].append("-"*(longest_problem+2))

      #evaluate if needed
      if (evaluate):
          if (problem_3 == "+"):
              evaluated_problem = str(int(problem_1) + int(problem_2))
          if (problem_3 == "-"):
              evaluated_problem = str(int(problem_1) - int(problem_2))
          arranged_problem_list_rows[3].append(" "*(longest_problem+2-len(evaluated_problem))+evaluated_problem)

  #Format arranged_problem_list_rows to string
  if evaluate:
      arranged_problems = "    ".join(arranged_problem_list_rows[0])+"\n"+"    ".join(arranged_problem_list_rows[1])+"\n"+"    ".join(arranged_problem_list_rows[2])+"\n"+"    ".join(arranged_problem_list_rows[3])

  #Or format arranged_problem_list_rows to string and add evaluated row
  else:
      arranged_problems = "    ".join(arranged_problem_list_rows[0])+"\n"+"    ".join(arranged_problem_list_rows[1])+"\n"+"    ".join(arranged_problem_list_rows[2])
 
  return arranged_problems


print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], evaluate=False))