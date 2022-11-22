from eval import Evaluator

if __name__ == '__main__' :
    
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    
    print(Evaluator.zip_evaluate(coefs, words))