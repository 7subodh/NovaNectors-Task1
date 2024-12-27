import re

# Calculator class to handle operations
class Calculator:
    def evaluate(self, expression: str) -> float:
        try:
            # Validate input
            if not self._is_valid_expression(expression):
                raise ValueError("Invalid expression")
            
            # Calculate the result
            result = eval(expression)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception as e:
            return f"Error: {str(e)}"

    def _is_valid_expression(self, expression: str) -> bool:
        # Allow numbers, basic operators, and whitespace
        return bool(re.match(r'^[0-9+\-*/(). ]+$', expression))

# Command-line interface
if __name__ == "__main__":
    calculator = Calculator()

    print("Text-based Calculator (type 'exit' to quit)")
    while True:
        expression = input("Enter expression: ").strip()
        
        if expression.lower() == 'exit':
            print("Goodbye!")
            break
        
        result = calculator.evaluate(expression)
        print(f"Result: {result}")
