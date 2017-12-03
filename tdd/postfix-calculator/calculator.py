# entrada: "1 2 +"
# saida: 3

# entrada: "1 2 3 + +"
# saida: 6

# entrada: "1 2 3 * +"   (eq: 1 + 2 * 3)
# saida: 7

# entrada: "1 2 3 + *"   (eq: 1 * (2 + 3))
# saida: 6

def postfix_calc(expression):
    expr_list = expression
    if isinstance(expression, str):
        expr_list = expression.split()
    if len(expr_list) == 1:
        return int(expr_list[0])
    elif len(expr_list) == 3:
        return int(expr_list[0]) + int(expr_list[1])
    else:
        if expr_list[3].isdigit():
            result = postfix_calc(expr_list[0:3])  
            return postfix_calc([result, expr_list[3], expr_list[4]])
        else:
            result = postfix_calc(expr_list[1:4])  
            return postfix_calc([expr_list[0], result, expr_list[4]])


