# entrada: "1 2 +"
# saida: 3

# entrada: "1 2 3 + +"
# saida: 6

# entrada: "1 2 3 * +"   (eq: 1 + 2 * 3)
# saida: 7

# entrada: "1 2 3 + *"   (eq: 1 * (2 + 3))
# saida: 6

def postfix_calc(expression):
    expr_list = expression.split()
    if len(expr_list) == 1:
        return int(expr_list[0])
    else:
        result = int(expr_list[0]) + int(expr_list[1])
        if len(expr_list) > 3:
            result += int(expr_list[2])
        return result


