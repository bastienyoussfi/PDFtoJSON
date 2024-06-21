import ollama

class AIagent:
    def __init__(self, model):
        self.model = model
        self.history = [{"role": "", "content": ""}]

    def get_name(self):
        return self.model

    def generate_response(self, input: str, include = False) -> str:
        # Prepares the prompt with the memory of the conversation
        prompt = ""
        if include:
            self.history.append({"role": "user", "content": input})
            
        for message in self.history:
            prompt += f"{message['role']}: {message['content']}\n"

        # Generates a response from the model
        response = ollama.generate(self.model, prompt)

        # Updates the memory of the conversation with the new response
        if include:
            self.history.append({"role": "model", "content": response})
        
        return response['response']
    
    def reset(self):
        self.history = [{"role": "", "content": ""}]