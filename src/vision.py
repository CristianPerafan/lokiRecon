import ollama

class Vision():
    def __init__(self,modelName):
        self.modelName = modelName

    def sendImage(self):
        res = ollama.chat(
            model="llava:7b",
            messages=[
                {
                    'role': 'user',
                    'content': 'Describe this image:',
                    'images': ['./img/cover.png']
                }
            ]
        )

        print(res['message']['content'])