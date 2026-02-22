import json

class StyleService:
    def __init__(self, llm):
        self.llm = llm
    
    ## Synthesizes a styleguide based on application samples given. This reduces token use anywhere up to 80% and in the future can give the user better control over the style
    def synthesize_style(self, samples: list[str]):
        system_prompt = "You are a linguistic analyst. Create a 300-word 'Writing Style Guide' based on these samples."
        # This only runs ONCE to create your profile
        style_guide = self.llm.generate(system_prompt, str(samples))
        
        with open("data/style_profile.json", "w") as f:
            json.dump({"style_guide": style_guide}, f)