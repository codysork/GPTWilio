from openai import Completion


class Engine:
    DAVINCI = 'text-davinci-001'
    CURIE = 'text-curie-001'
    BABBAGE = 'text-babbage-001'
    ADA = 'text-ada-001'


class OpenAIClient:
    """Takes a string as a prompt, and uses the GPT-3 language model
       through the OpenAI API to complete the prompt."""

    def __init__(self, engine: Engine = Engine.ADA, temperature=0.7,
                 max_tokens=40):
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens

    @staticmethod
    def _text(completion: Completion) -> str:
        return completion['choices'][0]['text']

    @staticmethod
    def _stop_sequence(completion: Completion) -> bool:
        return completion['choices'][0]['finish_reason'] == 'stop'

    class InvalidPrompt(Exception):
        pass

    def make_completion(self, prompt: str) -> Completion:
        return Completion.create(
            engine=self.engine,
            prompt=prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens)

    def make_completion_text(self, prompt: str) -> str:
        return self._text(self.make_completion(prompt))

    def make_completion_until_stop(self, prompt: str) -> str:
        completion = self.make_completion(prompt)
        if self._stop_sequence(completion):
            return prompt + self._text(completion)
        else:
            return self.make_completion_until_stop(prompt + self._text(completion))
