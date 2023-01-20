from compiler.lexer import aw_lexer
from compiler.aw_parser import aw_parser
from compiler.visitor import FormatVisitor, SemanticCheckerVisitor, EvaluatorVisitor
import sys

if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'r') as f:
            data = f.read()
        lexer = aw_lexer()
        parser = aw_parser()
        ast = parser.parse(data)
        formatter = FormatVisitor()
        semantic = SemanticCheckerVisitor()
        evaluator = EvaluatorVisitor()
        errors = semantic.visit(ast)
        if len(errors) > 0:
            for i, error in enumerate(errors):
                print(f'{i}. {error}')
        else:
            evaluator.visit(ast)
            if evaluator.errors:
                for i, error in enumerate(eval_ast.errors):
                    print(error)
    except IndexError:
        print('Please give a <filename>')
        exit()
    except FileNotFoundError:
        print('The path is wrong')
        exit()
