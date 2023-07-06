# Edge Cases:
# 1. if total_count("(") == total_count(")")
#   i.  string is completed ---> do not do anything
#   ii. string is not completed, eg: (())__ ---> add "("
# 2. if total_count("(") > total_count(")")
#   i.  if total_count("(") == n ---> meaning all "(" is over ---> add ")"
#   ii. if total_count("(") < n ---> meaning all "(" is not over ---> 2 choices, either "(" or ")"
