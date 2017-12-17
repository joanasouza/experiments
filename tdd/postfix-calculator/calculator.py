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
        if expr_list[2] != '+':
            raise ValueError('Unknown operator: %s' % expr_list[2])
        return int(expr_list[0]) + int(expr_list[1])
    else:
        pos = expr_list.index('+')
        result = postfix_calc(expr_list[pos-2:pos+1])  
        new_expr_list = expr_list[0:pos-2]
        new_expr_list.append(result)
        new_expr_list.extend(expr_list[pos+1:])

        return postfix_calc(new_expr_list)


