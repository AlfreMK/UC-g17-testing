import unittest
from tarea_1.model import *
from tarea_1.parser import *
from tarea_1.metrics import *
# en metrics y parser salta un error de importacion, para solucionarlo se coloca "from .model" en vez de "from model"
# lo dejo como "from model" pq así nos lo dieron.

class TestParser(unittest.TestCase):
    # test para la tarea
    # debe agregar las clases y modificar los metodos necesarios
    # para que los siguientes test compilen y pasen
    # usted puede agregar mas tests
    def test_pp(self):
        ast1 = PlusPlusNode(NumberNode(2))
        ast2 = parser("(++ 2)")
        self.assertEqual(ast1, ast2)

    def test_pp_eval(self):
        ast = parser("(++ 2)")
        result = ast.eval()
        self.assertEqual(result, 3)

    def test_mm_eval(self):
        ast = parser("(-- 3)")
        result = ast.eval()
        self.assertEqual(result, 2)
    def test_mm(self):
        ast1 = MinusMinusNode(NumberNode(2))
        ast2 = parser("(-- 2)")
        self.assertEqual(ast1, ast2)

    def test_mix(self):
        ast = parser("(+ (++ 1) (++ 1))")
        result = ast.eval()
        self.assertEqual(result, 4)
    
    def test_to_string2(self):
        ast1 = PlusPlusNode(MinusMinusNode(NumberNode(2)))
        self.assertEqual(ast1.to_string(), "(++ (-- 2))")

    def test_to_string3(self):
        ast1 = AdditionNode(PlusPlusNode(NumberNode(1)),MinusMinusNode(NumberNode(2)))
        self.assertEqual(ast1.to_string(), "(+ (++ 1) (-- 2))")
    
    def test_unary_counter(self):
        visitor = UnaryOperatorCounter()
        ast = parser("(+ (+ (++ 1) (++ 1)) (- 2 (-- 3)))")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 3)

    def test_unary_counter2(self):
        visitor = UnaryOperatorCounter()
        ast = parser("(++ 1)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 1)

    # new tests
    def test_unary_counter3(self):
        visitor = UnaryOperatorCounter()
        ast = parser("(- (+ (+ (++ 1) (++ 1)) (- 2 (-- 3))) (+ (++ 1) (-- 2)))")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 5)
    def test_eval_1(self):
        ast = parser("(+ (++ 1) (-- 2))")
        result = ast.eval()
        self.assertEqual(result, 3)
    def test_eval_2(self):
        ast = parser("(+ (+ (++ 1) (++ 1)) (- 2 (-- 3)))")
        result = ast.eval()
        self.assertEqual(result, 4)
    def test_eval_3(self):
        ast = parser("(++ (-- (++ (-- (++ (-- (++ (-- 4))))))))")
        result = ast.eval()
        self.assertEqual(result, 4)
    def test_eval_4(self):
        ast = parser("(+ 1 (++ 3))")
        result = ast.eval()
        self.assertEqual(result, 5)
    def test_eval_5(self):
        ast = AdditionNode(PlusPlusNode(NumberNode(10)),MinusMinusNode(NumberNode(2)))
        self.assertEqual(ast.to_string(), "(+ (++ 10) (-- 2))")
    def test_eval_6(self):
        ast = parser("(+ (++ 10) (-- 2))")
        result = ast.eval()
        self.assertEqual(result, 12)
    def test_eval_7(self):
        ast = parser("(+ 11 5)")
        result = ast.eval()
        self.assertEqual(result, 16)
    def test_eval_8(self):
        ast = parser("(+ (-- 11) 5)")
        result = ast.eval()
        self.assertEqual(result, 15)
    def test_eval_9(self):
        ast = parser("(+ (-- 105) 302)")
        result = ast.eval()
        self.assertEqual(result, 406)
    def test_eval_10(self):
        ast = parser("(+ (-- 05) 02)")
        result = ast.eval()
        self.assertEqual(result, 6)
    def test_eval_11(self):
        ast = parser("(+ (++ 0001) 02)")
        result = ast.eval()
        self.assertEqual(result, 4)
    def test_unary_counter3(self):
        visitor = UnaryOperatorCounter()
        ast = parser("(+ (+ (++ 1132) (++ 13232)) (- 2434 (-- 3555)))")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 3)
    def test_eval_12(self):
        ast = AdditionNode(PlusPlusNode(NumberNode(4343212)),MinusMinusNode(NumberNode(4021)))
        self.assertEqual(ast.to_string(), "(+ (++ 4343212) (-- 4021))")
    def test_eval_12(self):
        ast = parser("(+ (++ 0000) 000)")
        result = ast.eval()
        self.assertEqual(result, 1)
    def test_eval_13(self):
        ast = parser("(+ (++ -3) -4)")
        result = ast.eval()
        self.assertEqual(result, -6)
    def test_eval_14(self):
        ast = parser("-6")
        result = ast.eval()
        self.assertEqual(result, -6)
    def test_eval_15(self):
        ast = parser("(++ (+ 11 5))")
        result = ast.eval()
        self.assertEqual(result, 17)
    def test_eval_16(self):
        ast = NumberNode(-42)
        result = ast.eval()
        self.assertEqual(result, -42)
    def test_eval_17(self):
        ast = parser("5.4")
        result = ast.eval()
        self.assertEqual(result, 5.4)
    def test_eval_18(self):
        ast = parser("(++ (+ 1.5 1.5))")
        result = ast.eval()
        self.assertEqual(result, 4.0)
    def test_eval_19(self):
        ast = parser(".4")
        result = ast.eval()
        self.assertEqual(result, 0.4)
    def test_eval_20(self):
        ast = AdditionNode(PlusPlusNode(NumberNode(4343.212)),MinusMinusNode(NumberNode(402.1)))
        self.assertEqual(ast.to_string(), "(+ (++ 4343.212) (-- 402.1))")
    def test_eval_21(self):
        ast = NumberNode(-42.5)
        result = ast.eval()
        self.assertEqual(result, -42.5)
    def test_eval_22(self):
        ast = AdditionNode(PlusPlusNode(NumberNode(-4343.212)),MinusMinusNode(NumberNode(-402.1)))
        self.assertEqual(ast.to_string(), "(+ (++ -4343.212) (-- -402.1))")
    def test_eval_23(self):
        ast = AdditionNode(PlusPlusNode(NumberNode(-4343.212)),MinusMinusNode(NumberNode(402)))
        self.assertEqual(ast.to_string(), "(+ (++ -4343.212) (-- 402))")
    def test_eval_24(self):
        ast = MinusMinusNode(AdditionNode(PlusPlusNode(NumberNode(-4343.212)),MinusMinusNode(NumberNode(402))))
        self.assertEqual(ast.to_string(), "(-- (+ (++ -4343.212) (-- 402)))")
    
    
if __name__ == '__main__':
    unittest.main()
