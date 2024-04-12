import random

class ImprovedCodeGenerator:
    def __init__(self, max_lines=10, max_vars=3):
        self.max_lines = max_lines
        self.max_vars = max_vars
        self.vars_declared = set()  # Use a set to track declared variables
        self.lines = []
        self.var_counter = 0

    def get_var_name(self):
        self.var_counter += 1
        return f"var{self.var_counter}"

    def generate_exp(self):
        # Return "0" if no variables have been declared
        if not self.vars_declared:
            return "0"
        # Otherwise, use a randomly chosen declared variable
        return random.choice(list(self.vars_declared))

    def generate_line(self):
        # Dynamically determine possible actions based on current state
        possible_actions = ['D']  # Declare is always an option, until max_vars is reached
        if self.vars_declared:
            possible_actions.extend(['A', 'O'])  # Assign and Output require at least one declared variable
        if len(self.lines) > 0 and self.vars_declared:
            possible_actions.append('B')  # Branch requires a previous line and at least one declared variable
        if self.vars_declared:
            possible_actions.append('R')  # Remove requires at least one declared variable

        action_type = random.choice(possible_actions)
        
        if action_type == 'D' and len(self.vars_declared) < self.max_vars:
            var_name = self.get_var_name()
            line = f"D TYPE {var_name}"
            self.vars_declared.add(var_name)
        elif action_type == 'A':
            var_name = self.generate_exp()  # Use generate_exp to select a variable
            value = "0"  # Simplification
            line = f"A {var_name} {value}"
        elif action_type == 'B':
            target_line = random.randint(0, len(self.lines) - 1)
            exp = self.generate_exp()
            line = f"B {target_line} {exp}"
        elif action_type == 'O':
            var_name = self.generate_exp()
            line = f"O {var_name}"
        elif action_type == 'R':
            var_name = self.generate_exp()
            line = f"R {var_name}"
            self.vars_declared.remove(var_name)
        else:
            line = None  # This case should theoretically never be reached
        
        return line

    def generate_code(self):
        while len(self.lines) < self.max_lines:
            line = self.generate_line()
            if line:
                self.lines.append(line)

    def display_code(self):
        for i, line in enumerate(self.lines):
            print(f"{i}: {line}")

# Usage
generator = ImprovedCodeGenerator(max_lines=15, max_vars=5)
generator.generate_code()
generator.display_code()