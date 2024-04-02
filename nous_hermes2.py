# Install packages: gpt4all

from gpt4all import GPT4All

# Load the model(ONLY IF YOU NEED TO DOWNLOAD THE MODEL)
model = GPT4All(model_name="Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf")

# Path to file from manually downloading
#local_path="~/nomic.ai/GPT4All/Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"
# Load the model
#model = GPT4All(model_name=local_path)

# Read files
with open("outdated_user_guide.txt", 'r') as file:
    outdated_text = file.read()
with open("new_material.txt", 'r') as file:
    reference_text = file.read()

# Combine the two files
input_text = outdated_text + reference_text

# Hardcoded Prompt
#prompt = f"Please examine both documents. Based on the new content, can you find outdated information in the old user guide?:\n{input_text}"
prompt = f"Based on the new content in the reference material, there are several outdated pieces of information in the old user guide. Can you identify these?\n{input_text}"

# Generate text using Nous-Hermes2(LLM)
with model.chat_session():
    response1 = model.generate(prompt=prompt, temp=0)
    print(model.current_chat_session) # TODO: Change the default prompt template




